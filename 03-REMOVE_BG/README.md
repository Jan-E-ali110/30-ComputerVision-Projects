# 🖼️ Project 03 — Remove Bg

> Free AI-powered background remover — upload any image and remove the background instantly. No Photoshop, no subscriptions, completely free.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.41-red.svg)
![rembg](https://img.shields.io/badge/rembg-2.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Live Demo

**👉 [Try it here — completely free!](https://removebg-4rwpzsfhiprwtjsap2bwzf.streamlit.app/)**

---

## 📌 LinkedIn Post

[Read the full story on LinkedIn →](https://www.linkedin.com/posts/jan-ali-jagirani-a364022b7_python-computervision-streamlit-activity-7435019752214794240-bmVP)

---

## 📸 What It Does

Upload any image → AI removes the background → Download the result instantly. Built as a fully deployed web app accessible from anywhere in the world.

---

## ✨ Features

- One click background removal using AI
- Supports PNG, JPG, JPEG input
- Download as PNG, WebP or JPG
- Quality control slider
- Before and After preview side by side
- Live deployed — accessible from anywhere

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| rembg | AI background removal using U2Net pretrained model |
| Streamlit | Entire web UI in pure Python |
| Pillow | Image processing and format conversion |
| Streamlit Cloud | Free deployment |

---

## 📁 Project Structure

```
03-Remove-Bg/
├── app.py              ← Streamlit web interface
├── remover.py          ← background removal logic
├── requirements.txt    ← dependencies
└── README.md           ← this file
```

---

## ⚙️ Run Locally

```bash
git clone https://github.com/Jan-E-ali110/30-ComputerVision-Projects.git
cd "30-ComputerVision-Projects/03-Remove-Bg"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 What I Learned

- Using pretrained AI models without training from scratch
- Building complete web apps in pure Python using Streamlit
- Image format handling — PNG supports transparency, JPG does not
- Deploying Python web apps to Streamlit Cloud
- Debugging deployment issues across different cloud platforms

---

## 🔗 Links

- **Live App:** https://removebg-4rwpzsfhiprwtjsap2bwzf.streamlit.app/
- **LinkedIn Post:** https://www.linkedin.com/posts/jan-ali-jagirani-a364022b7_python-computervision-streamlit-activity-7435019752214794240-bmVP
- **Main Repo:** https://github.com/Jan-E-ali110/30-ComputerVision-Projects

---

*Built by [Jan Ali](https://www.linkedin.com/in/jan-ali-jagirani-a364022b7/) — BSAI Student @ Sindh Madressatul Islam University, Karachi*
