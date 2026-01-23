# Driver Behaviour Analysis

## Overview
This project implements a hybrid computer vision system that analyzes driving behavior using a live camera feed. The system performs real time vehicle detection and tracking, extracts motion-based features, infers driving behavior, and generates a post drive driver skill report.

---

## Key Features
- Real time vehicle detection using YOLOv8
- Multi object tracking with persistent vehicle IDs
- Motion feature extraction (speed, acceleration, lane stability)
- Rule based driving behavior analysis
- Risk aware real-time visualization
- Post drive driver skill scoring and report generation
- Camera only solution (no vehicle sensors required)

---

## System Pipeline
Camera / Video Feed  
→ Object Detection (YOLOv8)  
→ Object Tracking  
→ Motion Feature Extraction  
→ Behavior Analysis  
→ Live Monitoring + Data Logging  
→ Post-Drive Driver Report  

---

## Usage
Run with live camera:
```bash
python src/main.py
```

Run with video file:
```bash
python src/main.py --source data/input_videos/sample.mp4
```

---

## Output
- Real time annotated video feed  
- Logged driving behavior data  
- Post drive driver skill report  

---

## Use Cases
- Fleet driver performance evaluation  
- Driving school feedback systems  
- Smart city traffic behavior analysis  
- Insurance risk assessment research  

---

## Limitations
- Relative speed estimation (no real world calibration)  
- Rule based behavior inference  
- Camera angle dependency  

---

## Future Enhancements
- Speed calibration using camera geometry  
- ML based behavior classification  
- Multi camera fusion  

