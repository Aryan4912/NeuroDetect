# NeuroDetect 🧠

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-black.svg)](https://flask.palletsprojects.com/)
[![IEEE](https://img.shields.io/badge/Publication-IEEE-blue.svg)](https://ieeexplore.ieee.org/document/11379975/)

<div align="center">

# NeuroDetect

**An AI-powered brain tumor detection system using deep learning and attention-enhanced convolutional neural networks.**

Detects and classifies brain tumors from MRI scans using a **CBAM-enhanced InceptionV3 architecture**.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Model Architecture](#model-architecture) • [Dataset](#dataset) • [Project Structure](#project-structure)

</div>

---

# 🚀 Overview

**NeuroDetect** is a deep learning-based system designed to assist in **brain tumor detection from MRI images**.

The project combines:

- **InceptionV3 transfer learning**
- **CBAM attention mechanism**
- **PyTorch training pipeline**
- **Flask web interface for predictions**
- **Research-backed model architecture**

The goal of this project is to demonstrate how **deep learning models can support medical image analysis and assist in tumor detection tasks.**

---

# ✨ Features

| Feature | Description |
|-------|-------------|
| 🧠 **Deep Learning Model** | CBAM-enhanced InceptionV3 architecture |
| 🩺 **Medical Image Analysis** | Detects tumors from MRI brain scans |
| 🌐 **Web Interface** | Upload MRI images and receive predictions |
| ⚡ **Fast Inference** | Real-time classification through Flask app |
| 📊 **Model Evaluation** | Includes training metrics and evaluation |
| 📄 **Research Publication** | Model published on IEEE Xplore |

---

# 🛠 Installation

## Prerequisites

- Python 3.8+
- PyTorch
- Flask
- Required Python libraries

---

## Quick Setup

```bash
# Clone the repository
git clone https://github.com/Aryan4912/NeuroDetect.git

cd NeuroDetect

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open in browser
http://localhost:5000
````

---

# 📊 Usage

### Web Interface

1. Upload an **MRI brain scan image**
2. The system processes the image
3. The model predicts the **tumor type**

Possible predictions include:

* Glioma
* Meningioma
* Pituitary Tumor
* No Tumor

---

### Example Prediction

```python
Prediction: Glioma Tumor
Confidence: 96.3%
```

---

# 🤖 Model Architecture

The core model uses **InceptionV3 integrated with a CBAM attention module**.

### Architecture Pipeline

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

### Techniques Used

* Transfer Learning
* Attention Mechanisms (CBAM)
* Data Augmentation
* Deep CNN Feature Extraction

---

# 📊 Dataset

The model was trained using **MRI brain tumor datasets available on Kaggle**.

Dataset contains images categorized into:

| Class      | Description                            |
| ---------- | -------------------------------------- |
| Glioma     | Brain tumor originating in glial cells |
| Meningioma | Tumor arising from meninges            |
| Pituitary  | Tumor in pituitary gland               |
| No Tumor   | Normal MRI scan                        |

Images were **resized, normalized, and augmented** during training.

---

# 🏗 Project Structure

```
NeuroDetect/
│
├── app.py
├── model/
│   ├── inception_cbam.py
│   └── model_weights.pth
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── dataset/
│
├── notebooks/
│   └── training_pipeline.ipynb
│
├── requirements.txt
│
└── README.md
```

---

# 📄 Research Publication

This project resulted in a research paper:

**Attention Mechanism Enhanced InceptionV3: A Hybrid Deep Learning Approach to Brain Tumor Classification**

Published on **IEEE Xplore**

🔗 [https://ieeexplore.ieee.org/document/11379975/](https://ieeexplore.ieee.org/document/11379975/)

---

# 📈 Training

The training pipeline includes:

1. Data preprocessing and augmentation
2. Transfer learning using InceptionV3
3. Integration of CBAM attention module
4. Model training using PyTorch
5. Performance evaluation using validation metrics

Example training command:

```bash
python train_model.py --epochs 50 --batch_size 32
```

---

# 📊 Model Performance

Example metrics:

```
Accuracy: 96%
Precision: 94%
Recall: 95%
F1 Score: 94.5%
```

---

# ⚠️ Disclaimer

This project is developed for **educational and research purposes only**.

It is **not intended to replace professional medical diagnosis**.

Always consult qualified medical professionals for clinical decisions.

---

# 🧰 Built With

<p align="left">
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" height="25">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" height="25">
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" height="25">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" height="25">
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" height="25">
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" height="25">
</p>

---

<div align="center">

### 🧠 AI for Medical Imaging

If you found this project useful, consider giving it a ⭐ on GitHub.

</div>
```

---

### After Adding This

Your GitHub repo will automatically show:

* **Language bar (like in your screenshot)**
* **Badges**
* **Sections**
* **Professional ML project structure**
