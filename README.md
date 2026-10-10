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

## 📸 Project Gallery

### 1. Hardware Setup
![Hardware Setup](docs/images/hardware-setup.jpg)

### 2. System Ready
![System Ready](docs/images/sys%20ready%20hardware.jpg)

### 3. Driver Awake — Python Detection
![Driver Awake](docs/images/py%20awake.png)

### 4. Drowsiness Detected — Python
![Drowsiness Detected](docs/images/py%20drowsy.png)

### 5. Driver Awake — Hardware Display
![Awake Hardware](docs/images/awake%20hardware.jpg)

### 6. Drowsiness Warning — Hardware Display
![Drowsy Hardware](docs/images/drowsy%20hardware.jpg)

### 7. Face Not Detected — Python
![Face Not Detected](docs/images/py%20no%20face.png)

### 8. Face Not Detected — Hardware
![Face Not Detected Hardware](docs/images/face%20not%20found%20hardware.jpg)


## ⚙️ System Architecture

The system combines Python-based AI vision processing with an Arduino-controlled warning system.

```text
          LAPTOP WEBCAM
                |
                v
       PYTHON + OPENCV
                |
                v
    MEDIAPIPE FACE LANDMARKS
                |
                v
       EYE ASPECT RATIO
                |
                v
     DROWSINESS DETECTION
                |
        USB SERIAL (COM3)
                |
                v
       ARDUINO MEGA 2560
          /           \
         v             v
     16×2 LCD      ISD1820 MODULE
   AWAKE/DROWSY      + SPEAKER
                         |
                         v
                  VOICE WARNING
```

### How It Works

1. The laptop webcam captures the driver's face.
2. Python processes the video using OpenCV and MediaPipe.
3. Eye landmarks are used to calculate the Eye Aspect Ratio (EAR).
4. If the eyes remain closed for approximately 2 seconds, the system detects possible drowsiness.
5. Python sends the detection status to the Arduino Mega through serial communication.
6. The Arduino updates the LCD and triggers the ISD1820 module to play the recorded voice warning.
7. When the eyes reopen, the system returns to the awake state.

**Note:** The AI vision processing runs on the laptop. The Arduino handles the LCD and voice-warning hardware.

## © Copyright

Copyright © 2026. All rights reserved.

This project is shared for viewing and educational reference only. No permission is granted to copy, modify, redistribute, or use this code without prior written permission from the author.
