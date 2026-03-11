import os
import io
import json
from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
from fpdf import FPDF
import torch
from torchvision import transforms
from PIL import Image
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

from reportlab.lib.utils import ImageReader
from PIL import Image


app = Flask(__name__)
app.secret_key = 'your_secret_key'  

UPLOAD_FOLDER = 'uploads'
REPORTS_FOLDER = 'reports'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'dcm'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPORTS_FOLDER'] = REPORTS_FOLDER


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

import torch.nn as nn
import torch
from torchvision.models import inception_v3, Inception_V3_Weights

class CBAM(nn.Module):
    def __init__(self, channels, reduction_ratio=8):
        super(CBAM, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)

        self.shared_mlp = nn.Sequential(
            nn.Conv2d(channels, channels // reduction_ratio, 1, bias=False),
            nn.ReLU(),
            nn.Conv2d(channels // reduction_ratio, channels, 1, bias=False)
        )

        self.sigmoid_channel = nn.Sigmoid()
        self.conv_spatial = nn.Conv2d(2, 1, kernel_size=7, padding=3, bias=False)
        self.sigmoid_spatial = nn.Sigmoid()

    def forward(self, x):
        # Channel Attention
        avg_out = self.shared_mlp(self.avg_pool(x))
        max_out = self.shared_mlp(self.max_pool(x))
        channel_att = self.sigmoid_channel(avg_out + max_out)
        x = x * channel_att

        # Spatial Attention
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        spatial_att = self.sigmoid_spatial(self.conv_spatial(torch.cat([avg_out, max_out], dim=1)))
        x = x * spatial_att

        return x

class InceptionCBAM(nn.Module):
    def __init__(self, num_classes=4):
        super(InceptionCBAM, self).__init__()
        self.backbone = inception_v3(weights=Inception_V3_Weights.DEFAULT, aux_logits=True)
        self.backbone.AuxLogits.fc = nn.Linear(768, num_classes)
        self.backbone.fc = nn.Identity()

        self.cbam = CBAM(2048)
        self.pool = nn.AdaptiveAvgPool2d((1, 1))

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(2048, 256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.backbone.Conv2d_1a_3x3(x)
        x = self.backbone.Conv2d_2a_3x3(x)
        x = self.backbone.Conv2d_2b_3x3(x)
        x = self.backbone.maxpool1(x)
        x = self.backbone.Conv2d_3b_1x1(x)
        x = self.backbone.Conv2d_4a_3x3(x)
        x = self.backbone.maxpool2(x)

        x = self.backbone.Mixed_5b(x)
        x = self.backbone.Mixed_5c(x)
        x = self.backbone.Mixed_5d(x)
        x = self.backbone.Mixed_6a(x)
        x = self.backbone.Mixed_6b(x)
        x = self.backbone.Mixed_6c(x)
        x = self.backbone.Mixed_6d(x)
        x = self.backbone.Mixed_6e(x)
        x = self.backbone.Mixed_7a(x)
        x = self.backbone.Mixed_7b(x)
        x = self.backbone.Mixed_7c(x)

        x = self.cbam(x)
        x = self.pool(x)
        x = self.classifier(x)
        return x

model = InceptionCBAM(num_classes=4)
model.load_state_dict(torch.load('best_model.pth', map_location=device))
model.to(device)
model.eval()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


preprocess = transforms.Compose([
    transforms.Resize((150, 150)),  # Match training, not 299
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])



def predict_image(image_path):
    img = Image.open(image_path).convert('RGB')
    input_tensor = preprocess(img).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]

    classes = ['glioma', 'meningioma', 'notumor', 'pituitary']
    label_map = {
        'glioma': 'Glioma Tumor',
        'meningioma': 'Meningioma Tumor',
        'notumor': 'No Tumor',
        'pituitary': 'Pituitary Tumor'
    }

    pred_idx = probs.argmax()
    class_name = classes[pred_idx]
    prediction_label = label_map[class_name]
    confidence = probs[pred_idx] * 100
    note = "Please consult a medical professional for confirmation." if class_name != "notumor" else "No tumor detected."

    return {
        "prediction": prediction_label,
        "confidence": round(confidence, 2),
        "note": note,
        "class_index": pred_idx
    }




@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

# Route: Info page
@app.route('/info')
def info():
    return render_template('info.html')

# Route: News page
@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'ctscan' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['ctscan']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

    
        result = predict_image(file_path)

    
        global last_prediction_data
        last_prediction_data = {
            "file_path": file_path,
            "prediction": result["prediction"],
            "confidence": result["confidence"],
            "note": result["note"]
        }

    
        prediction_str = (
            f"Prediction: {result['prediction']}\n"
            f"Confidence: {result['confidence']}%\n"
            f"Note: {result['note']}"
        )

        return render_template('index.html', prediction=prediction_str)
    else:
        flash('Allowed file types are png, jpg, jpeg, dcm')
        return redirect(url_for('index'))




@app.route('/download_report', methods=['POST'])
def download_report():
    global last_prediction_data

    if not last_prediction_data:
        flash('No prediction data found. Please upload a scan first.')
        return redirect(url_for('index'))

    file_path = last_prediction_data.get('file_path')
    prediction = last_prediction_data.get('prediction', 'N/A')
    confidence = last_prediction_data.get('confidence', 'N/A')
    note = last_prediction_data.get('note', '')

    prediction_lines = [
        f"Prediction: {prediction}",
        f"Confidence: {confidence}%",
        f"Note: {note}"
    ]

 
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

 
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2.0, height - 50, "🧠 NeuroDetect Diagnostic Report")


    pdf.setFont("Helvetica", 14)
    pdf.drawString(50, height - 100, "Patient Scan Analysis")
    pdf.line(50, height - 105, width - 50, height - 105)

 
    pdf.setFont("Helvetica", 12)
    y_position = height - 140
    for line in prediction_lines:
        pdf.drawString(50, y_position, line)
        y_position -= 25


    try:
        img = Image.open(file_path)
        img_width, img_height = img.size

    
        max_dim = 350
        if img_width > max_dim or img_height > max_dim:
            scale = min(max_dim / img_width, max_dim / img_height)
            img_width = int(img_width * scale)
            img_height = int(img_height * scale)

        img_x = (width - img_width) / 2
        img_y = y_position - img_height - 20 

        pdf.drawImage(ImageReader(img), img_x, img_y, width=img_width, height=img_height)
        y_position = img_y - 30  
    except Exception as e:
        pdf.drawString(50, y_position, "Error displaying image.")
        y_position -= 25

    pdf.setFont("Helvetica-BoldOblique", 16)
    pdf.setFillColorRGB(0.8, 0.8, 0.8)
    pdf.drawRightString(width - 50, 80, "— NeuroDetect —")
    pdf.setFillColorRGB(0, 0, 0)  # Reset color


    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(50, 50, "Disclaimer: This is an AI-generated report and must be reviewed by a certified doctor.")


    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="NeuroDetect_Report.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)

