# 🔤 Project 02 — OCR Text Detection

> An automated text detection pipeline that processes real-world images — storefronts, signs, and product labels — using EasyOCR and OpenCV.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![EasyOCR](https://img.shields.io/badge/EasyOCR-1.7-red.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 LinkedIn Post

[Read the full story on LinkedIn →](https://www.linkedin.com/posts/jan-ali-jagirani-a364022b7_computervision-ocr-easyocr-activity-7431782786778370048-Ymy5)

---

## 📸 What It Does

Automatically processes a dataset of real-world images, detects all text regions, draws bounding boxes around them, and saves annotated results to an output folder — fully automated, no manual work needed.

---

## ✨ Features

- Processes entire folder of images automatically
- Detects text in real world uncontrolled images
- Confidence based filtering — threshold 0.5
- Draws precise bounding boxes and text labels
- Saves all annotated results to output folder
- Achieved ~80% accuracy on 400 real-world images

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| EasyOCR | Deep learning based text detection |
| OpenCV | Drawing bounding boxes and saving results |
| NumPy | Array operations |

---

## 📁 Project Structure

```
02-OCR-Text-Detection/
├── ocr_text_detection.py ← main script
├── requirements.txt      ← dependencies
├── output/               ← sample annotated results
└── README.md             ← this file
```

---

## ⚙️ Run Locally

```bash
git clone https://github.com/Jan-E-ali110/30-ComputerVision-Projects.git
cd "30-ComputerVision-Projects/02-OCR-Text-Detection"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python ocr_text_detection.py
```

---

## 📊 Results

- Dataset: 400 real-world images — storefronts, signs, product labels
- Accuracy: ~80% on uncontrolled real-world images
- Failure cases documented: blur, low contrast, extreme text angles

---

## 🧠 What I Learned

- Difference between Tesseract, EasyOCR, and AWS Textract
- Why EasyOCR outperforms Tesseract on real world images
- Confidence based filtering to improve output quality
- Batch processing entire image folders automatically
- Understanding and documenting model failure cases

---

## 🔗 Links

- **LinkedIn Post:** https://www.linkedin.com/posts/jan-ali-jagirani-a364022b7_computervision-ocr-easyocr-activity-7431782786778370048-Ymy5
- **Main Repo:** https://github.com/Jan-E-ali110/30-ComputerVision-Projects

---

*Built by [Jan Ali](https://www.linkedin.com/in/jan-ali-jagirani-a364022b7/) — BSAI Student @ Sindh Madressatul Islam University, Karachi*
