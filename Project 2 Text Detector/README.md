# 02 — OCR Text Detection 🔍📝

Automatically detects and extracts text from real-world images using EasyOCR and OpenCV. Draws bounding boxes around detected text with confidence filtering.

---

Output images with bounding boxes are saved in the `./output/` folder.

---

## 🧠 What I Learned

- How OCR engines detect and read text from real world images
- Difference between Tesseract and EasyOCR and when to use each
- Working with bounding box coordinates for text regions
- Filtering detections by confidence score
- Batch processing an entire image dataset automatically
- Understanding why some images fail — blur, angle, low contrast

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| EasyOCR | Deep learning based text detection and recognition |
| OpenCV | Image reading, drawing bounding boxes, saving output |
| NumPy | Bounding box coordinate handling |
| OS | Batch processing folder of images |

---

## 📊 Dataset

- **Source:** Roboflow
- **Format:** COCO JSON
- **Size:** 400 images
- **Split:** Train / Valid / Test
- **Content:** Real world images containing text — signs, labels, storefronts

---

## ⚙️ Setup

```bash
pip install easyocr opencv-python numpy
```

---

## ▶️ How to Run

```bash
python OCR_Text_detection.py
```

Output images with bounding boxes will be saved to the `./output/` folder.

---

## 📈 Results

- Achieved ~80% accurate text detection on test dataset
- Failed cases were primarily low resolution and heavily angled text
- Confidence threshold set at 0.5 to filter uncertain detections

---

## 📂 Project Structure

```
02-OCR-Text-Detection/
├── OCR_Text_detection.py
├── requirements.txt
├── data/
│   ├── train/
│   ├── valid/
│   └── test/
├── output/
└── README.md
```

---

## 🔙 Back to Main Repo

[← 30 CV Projects](../README.md)
