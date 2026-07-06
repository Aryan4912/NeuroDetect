<div align="center">

# 🧠 NeuroDetect

**An AI-powered brain tumor detection system using deep learning and attention-enhanced convolutional neural networks.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![IEEE](https://img.shields.io/badge/Publication-IEEE-00629B?style=for-the-badge)](https://ieeexplore.ieee.org/document/11379975/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#license)

</div>

---

## 📖 Overview

Manual review of MRI scans for brain tumor detection is time-intensive and dependent on specialist availability. **NeuroDetect** replaces the guesswork with a deep learning pipeline that classifies brain tumors directly from MRI images — flagging **glioma, meningioma, pituitary tumor, or no tumor** through a simple web upload, backed by a research-validated model architecture instead of ad-hoc heuristics.

Built as a full-stack ML project combining a **CBAM-enhanced InceptionV3 architecture** with a practical Flask web interface, resulting in a peer-reviewed publication on IEEE Xplore.

---

## ✨ Features

### 🧠 For Users
- Upload an MRI brain scan image directly through the web interface
- Real-time classification via Flask — no local model setup required
- Clear prediction output with confidence score (e.g. `Glioma Tumor — 96.3%`)
- Supports four classes: Glioma, Meningioma, Pituitary Tumor, No Tumor

### 🔬 For Researchers / Developers
- CBAM-enhanced InceptionV3 architecture with transfer learning
- Full training pipeline included via Jupyter notebook
- Model evaluation with accuracy, precision, recall, and F1 metrics
- Configurable training via CLI (`--epochs`, `--batch_size`)

### 📄 Research Credentials
- Published on **IEEE Xplore**: *Attention Mechanism Enhanced InceptionV3: A Hybrid Deep Learning Approach to Brain Tumor Classification*
- Demonstrates applied deep learning for medical image analysis

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Model / ML** | PyTorch, InceptionV3, CBAM Attention Mechanism |
| **Backend** | Python, Flask |
| **Frontend** | HTML, CSS, Bootstrap, JavaScript |
| **Data Tools** | NumPy, Pandas |

---

## 🤖 Model Architecture

The core model integrates **InceptionV3** with a **CBAM (Convolutional Block Attention Module)** for improved feature focus on tumor regions:

```
MRI Image
   ↓
Image Preprocessing
   ↓
InceptionV3 Backbone
   ↓
CBAM Attention Module
   ↓
Fully Connected Layer
   ↓
Softmax Classification
```

**Techniques used**: transfer learning, attention mechanisms (CBAM), data augmentation, deep CNN feature extraction.

---

## 📊 Dataset & Performance

Trained on MRI brain tumor datasets (Kaggle), with images resized, normalized, and augmented across four classes:

| Class | Description |
|---|---|
| Glioma | Brain tumor originating in glial cells |
| Meningioma | Tumor arising from the meninges |
| Pituitary | Tumor in the pituitary gland |
| No Tumor | Normal MRI scan |

**Example evaluation metrics:**
```
Accuracy: 96%
Precision: 94%
Recall: 95%
F1 Score: 94.5%
```

---

## 📁 Project Structure

```
NeuroDetect/
├── app.py                      # Flask application — routes, inference
├── model/
│   ├── inception_cbam.py       # CBAM-enhanced InceptionV3 architecture
│   └── model_weights.pth       # Trained model weights
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── dataset/                     # Training/validation MRI images
├── notebooks/
│   └── training_pipeline.ipynb  # Full training pipeline
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PyTorch
- Flask

### 1. Clone the repository
```bash
git clone https://github.com/Aryan4912/NeuroDetect.git
cd NeuroDetect
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

### 4. (Optional) Train the model
```bash
python train_model.py --epochs 50 --batch_size 32
```

---

## 📖 Usage

1. Upload an MRI brain scan image through the web interface
2. The system preprocesses and runs the image through the model
3. View the predicted tumor type and confidence score

```python
Prediction: Glioma Tumor
Confidence: 96.3%
```

---

## 📄 Research Publication

**Attention Mechanism Enhanced InceptionV3: A Hybrid Deep Learning Approach to Brain Tumor Classification**
Published on IEEE Xplore — 🔗 [ieeexplore.ieee.org/document/11379975](https://ieeexplore.ieee.org/document/11379975/)

---

## 🧭 Roadmap

- [ ] Expand dataset to include additional tumor subtypes
- [ ] Add Grad-CAM visualization for model interpretability
- [ ] REST API layer for external integration
- [ ] Dockerized deployment setup

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page or open a pull request.

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**. It is **not intended to replace professional medical diagnosis** — always consult qualified medical professionals for clinical decisions.

---

## 📄 License

This project is licensed under the MIT License — feel free to use it as a learning reference or a base for your own medical imaging project.

---

<div align="center">

**Built by [Aryan Ravindra Pawar](https://github.com/Aryan4912)**

[![GitHub](https://img.shields.io/badge/GitHub-Aryan4912-181717?style=flat-square&logo=github)](https://github.com/Aryan4912)

</div>
