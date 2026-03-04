# 🎭 Project 01 — Face Anonymizer

> A real-time face detection and anonymization tool that automatically detects and blurs faces in images, videos, and live webcam feed.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 LinkedIn Post

[Read the full story on LinkedIn →](https://www.linkedin.com/posts/jan-ali-jagirani-a364022b7_computervision-opencv-python-activity-7430890120649711616-NtNo)

---

## 📸 What It Does

Detects faces in any image, video, or live webcam feed and automatically blurs them to protect privacy — all in real time with a single unified script.

---

## ✨ Features

- Detects and blurs faces automatically
- Supports 3 input modes — image, video, live webcam
- Implements coordinate transformation from relative bounding boxes to pixel precision
- Preserves original video FPS
- Saves anonymized output files automatically

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| OpenCV | Image and video processing, blurring |
| MediaPipe | Face detection model |

---

## 📁 Project Structure

```
01-Face-Anonymizer/
├── face_anonymizer.py    ← main script
├── requirements.txt      ← dependencies
└── README.md             ← this file
```

---

## ⚙️ Run Locally

```bash
git clone https://github.com/Jan-E-ali110/30-ComputerVision-Projects.git
cd "30-ComputerVision-Projects/01-Face-Anonymizer"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python face_anonymizer.py
```

---

## 🧠 What I Learned

- How MediaPipe detects faces using relative bounding box coordinates
- Converting relative coordinates to pixel level precision
- Processing video frame by frame with correct FPS preservation
- Handling 3 different input modes from a single unified codebase
- Clean resource management with cv2.destroyAllWindows()

---

## 🔗 Links

- **LinkedIn Post:** https://www.linkedin.com/posts/jan-ali-jagirani-a364022b7_computervision-opencv-python-activity-7430890120649711616-NtNo
- **Main Repo:** https://github.com/Jan-E-ali110/30-ComputerVision-Projects

---

*Built by [Jan Ali](https://www.linkedin.com/in/jan-ali-jagirani-a364022b7/) — BSAI Student @ Sindh Madressatul Islam University, Karachi*
