# 01 — Face Anonymizer 👤🚫

Automatically detects and blurs faces in images, videos, and live webcam feed using MediaPipe and OpenCV.

---

## 🧠 What I Learned

- How MediaPipe's face detection pipeline works under the hood
- Converting relative bounding boxes to pixel coordinates
- Processing video frame by frame with OpenCV
- Building a tool that works across 3 different input modes

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| OpenCV | Image/video reading, blurring, display |
| MediaPipe | Face detection model |
| argparse | CLI argument handling |

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
pip install opencv-python
```

---

## ▶️ How to Run

**Image mode:**
```bash
python face_anonymizer.py --mode image --filePath path/to/image.jpg
```

**Video mode:**
```bash
python face_anonymizer.py --mode video --filePath path/to/video.mp4
```

**Webcam mode:**
```bash
python face_anonymizer.py --mode webcam
```
> Press `Q` to quit webcam mode.

Output is saved to the `./output/` folder.

---

## 📂 Project Structure

```
01-Face-Anonymizer/
├── face_anonymizer.py
├── requirements.txt
└── README.md
```

---

## 🔙 Back to Main Repo

[← 30 CV Projects](../README.md)
