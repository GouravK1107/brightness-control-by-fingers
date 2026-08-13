# 💡 Brightness Control Using Hand Gestures

A real-time Computer Vision project that controls your system's screen brightness using nothing but a **thumb-and-index-finger pinch**. Built with the **MediaPipe Hand Landmarker (Tasks API)** and **OpenCV**, it tracks hand landmarks live and dynamically maps pinch distance to brightness level.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Tasks%20API-0097A7?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

## 🚀 Features

- ✋ Real-time hand tracking
- 🤏 Thumb + index pinch-distance detection
- 💡 Dynamic brightness control (0%–100%)
- 📊 Live brightness percentage display on screen
- 🪞 Mirrored (selfie-style) camera feed
- ⌨️ Press **'q'** to quit safely
- 🧩 Built on the modern MediaPipe Tasks API

---

## 🧠 How It Works

MediaPipe detects 21 hand landmarks per hand. This project uses just two of them:

- **Thumb Tip** → Landmark ID 4
- **Index Tip** → Landmark ID 8

**Logic:**
1. Calculate the distance between the thumb tip and index fingertip
2. Map that distance range to a brightness range (0–100%)
3. Update system brightness in real time

> Small pinch distance → low brightness
> Large pinch distance → high brightness

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe (Tasks API)
- NumPy
- `screen-brightness-control` (for Windows brightness control)

---

## 📂 Project Structure

```
brightness-control-by-fingers/
│
├── brightness_control.py     # Main application logic
├── hand_landmarker.task       # MediaPipe hand landmark model
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

**1️⃣ Clone the repository**
```
git clone https://github.com/GouravK1107/brightness-control-by-fingers.git
cd brightness-control-by-fingers
```

**2️⃣ Create a virtual environment (recommended)**
```
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux / macOS
```

**3️⃣ Install dependencies**
```
pip install -r requirements.txt
```
If needed, install directly:
```
pip install opencv-python mediapipe numpy screen-brightness-control
```

**4️⃣ Run the program**
```
python brightness_control.py
```
Press **'q'** to exit.

---

## 📌 Requirements

- Windows OS (recommended — best `screen-brightness-control` support)
- A webcam
- Python 3.10+

---

## 🎯 Learning Outcomes

- Working hands-on with the MediaPipe Tasks API
- Real-time landmark-based gesture recognition
- Mapping a physical gesture to system-level control
- Coordinate interpolation between two ranges
- Building interactive, responsive CV applications

---

## 🔥 Future Improvements

- 🎚️ Smoothing filter to reduce flickering
- 📊 On-screen brightness progress bar
- 🎯 Defined gesture activation zone
- 👐 Multi-hand support
- 🖥️ GUI interface

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Fork → create a branch → commit → push → open a pull request.

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Gourav R**
Backend Developer | Applied AI Developer — exploring Computer Vision & system-level automation

GitHub: https://github.com/GouravK1107
Portfolio: https://gouravk1107.github.io/my-portfolio/

---

Made with ❤️ and a well-calibrated pinch.
