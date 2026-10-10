# 🚗 AI-Based EV Driver Drowsiness Detection System

An AI-assisted driver safety system that detects signs of drowsiness using a laptop webcam and alerts the driver through an LCD display and a voice warning module.

## 📌 Project Overview

Driver drowsiness can reduce reaction time and increase the risk of road accidents. This project combines Python-based facial landmark detection with an Arduino-controlled warning system to demonstrate a low-cost driver alert solution.

## ✨ Features

- Real-time webcam-based eye monitoring
- Facial landmark detection using MediaPipe
- Eye Aspect Ratio (EAR)-based drowsiness detection
- Arduino Mega 2560 integration
- 16×2 LCD status display
- ISD1820 voice warning module
- Serial communication between Python and Arduino

## ⚙️ System Architecture

**Laptop Webcam → Python + MediaPipe → Serial Communication → Arduino Mega 2560 → LCD + Voice Alert**

## 🧰 Hardware Used

- Arduino Mega 2560
- 16×2 LCD
- ISD1820 voice recording/playback module
- Speaker
- Laptop webcam
- Breadboard and jumper wires

## 💻 Software Used

- Python
- OpenCV
- MediaPipe
- pySerial
- Arduino IDE

## 🔄 Working Principle

1. The webcam captures the driver's face.
2. MediaPipe identifies facial landmarks around the eyes.
3. Python calculates the Eye Aspect Ratio to estimate whether the eyes are closed.
4. If the eyes remain closed beyond the configured time threshold, the system identifies a potential drowsiness event.
5. Python sends the status to the Arduino Mega through serial communication.
6. The LCD displays a warning, and the voice module plays an alert.

## 🎯 Applications

- Driver safety demonstrations
- Automotive embedded-system prototypes
- Student projects in AI and electrical engineering
- Learning applications involving computer vision and microcontrollers

## ⚠️ Limitations

This is an educational prototype, not a certified automotive safety device. It can produce false alerts and should not replace proper rest or commercial driver-monitoring systems.

## 👨‍💻 Author

**Mohak Yashpal Lohi (ARST)**

## © Copyright

Copyright © 2026. All rights reserved.

This project is shared for viewing and educational reference only. No permission is granted to copy, modify, redistribute, or use this code without prior written permission from the author.
