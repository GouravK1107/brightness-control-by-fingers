# 💡 Brightness Control Using Hand Gestures

A real-time Computer Vision project that controls system screen brightness using finger gestures.

This project uses **MediaPipe Hand Landmarker (Tasks API)** and **OpenCV** to detect hand landmarks and dynamically adjust brightness based on the distance between the thumb and index finger.

---

## 🚀 Features

- Real-time hand tracking
- Thumb + Index pinch distance detection
- Dynamic brightness control (0% – 100%)
- Live brightness percentage display
- Mirrored (selfie-style) camera feed
- Press **'q'** to quit safely
- Built using modern MediaPipe Tasks API

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe (Tasks API)
- NumPy
- screen-brightness-control (Windows brightness control)

---

## 📂 Project Structure

```
BRIGHTNESSCONTROLPROJECT/
│
├── brightness_control.py
├── hand_landmarker.task
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

MediaPipe detects 21 hand landmarks.

We use:
- Thumb Tip → Landmark ID 4
- Index Tip → Landmark ID 8

### Logic:

1. Calculate distance between thumb and index finger.
2. Map distance range to brightness range (0–100%).
3. Update system brightness in real time.

Small distance → Low brightness  
Large distance → High brightness  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GouravK1107/brightness-control-by-fingers.git
cd brightness-control-by-fingers
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If needed:

```bash
pip install opencv-python mediapipe numpy screen-brightness-control
```

---

### 4️⃣ Run the Program

```bash
python brightness_control.py
```

Press **'q'** to exit.

---

## 📌 Requirements

- Windows OS (recommended for brightness control support)
- Webcam
- Python 3.10+

---

## 🎯 Learning Outcomes

- Working with MediaPipe Tasks API
- Real-time landmark-based gesture recognition
- Mapping gesture distance to system-level control
- Understanding coordinate interpolation
- Building interactive CV applications

---

## 🔥 Future Improvements

- Add smoothing filter to reduce flickering
- Add on-screen brightness progress bar
- Add gesture activation zone
- Add multi-hand support
- Add GUI interface

---

## 👨‍💻 Author

Gourav K  
BCA Student | Backend & AI Enthusiast  
Focused on Computer Vision, AI, and System-Level Automation.

---

⭐ If you found this project interesting, consider starring the repository!
