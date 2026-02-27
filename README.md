# 😴 Drowsiness Detection

> Real-time drowsiness detection system using facial landmarks and eye blink analysis — built to help keep drivers safe.

![Python](https://img.shields.io/badge/Python-3.3+-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-008000?style=flat-square)

## 💡 About

This project uses computer vision and facial landmark detection to identify signs of drowsiness in real-time. It monitors the driver's eyes through a webcam and triggers alerts when drowsiness is detected.

Built on the research paper "Real-Time Eye Blink Detection using Facial Landmarks" — the system calculates the **Eye Aspect Ratio (EAR)** to determine if the person's eyes are closing.

### How It Works

```
Camera Feed → Face Detection → Facial Landmarks → Eye Aspect Ratio → Alert System
                (dlib)           (68 points)        (EAR threshold)
```

1. **Face Detection** — Locates faces in the video stream using dlib
2. **Landmark Extraction** — Maps 68 facial landmarks on each detected face
3. **EAR Calculation** — Computes the Eye Aspect Ratio to measure eye openness
4. **Alert Trigger** — When EAR drops below threshold for consecutive frames, an alert fires

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.3+** | Core language |
| **dlib** | Face detection & facial landmarks |
| **OpenCV** | Video capture & image processing |
| **imutils** | OpenCV convenience functions |
| **NumPy** | Numerical computations |
| **SciPy** | Euclidean distance calculations |

## 🚀 Getting Started

### Prerequisites

- Python 3.3 or later
- Webcam

### Installation

```bash
# Clone the repository
git clone https://github.com/matheusmelchiades/drowsiness-detection.git
cd drowsiness-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the detector
python detector.py
```

## 📚 References

- Real-Time Eye Blink Detection using Facial Landmarks (Soukupová & Čech, 2016)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made by <a href="https://github.com/matheusmelchiades">Matheus Maciel</a></p>
