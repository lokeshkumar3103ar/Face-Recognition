
# Face Detection AI Project

## Overview
This project implements a face detection and recognition system using OpenCV and Python. It utilizes machine learning techniques to train a model for recognizing faces and can trigger alerts for unknown users. The system is designed to enhance security and automate user identification in real-time.

## Features
- **Face Detection**: Uses Haar cascades for detecting faces in real-time.
- **User Recognition**: Trains a model to recognize multiple users based on face samples.
- **Alert System**: Triggers audio alerts when an unknown user is detected.
- **Real-time Processing**: Captures video feed and processes it for face recognition on-the-fly.
- **User-Friendly Interface**: Displays recognized users with colored indicators.

## Requirements
To run this project, you need:
- Python 
- OpenCV library
- Numpy library
- PIL (Pillow) library
- Pynput library (for mouse control)
- A webcam for capturing video feed

You can install the required libraries using pip:
```bash
pip install opencv-python numpy pillow pynput
```

## Installation
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/lokeshkumar3103ar/Face-Recognition.git
   ```
2. Navigate to the project directory.
3. Ensure you have the required libraries installed (see Requirements).
4. Create folders named dataSet and trainner.
5. Place your Haar cascade file (`haarcascade_frontalface_default.xml`) in the project directory.
6. Prepare your dataset by running the `creator` script to capture face samples.
7. Train the model using the `trainer` script.
8. Run the `homesecurity` script to start the face recognition and alert system.

## Scripts
- **creator.py**: Captures face samples from the webcam and stores them in a dataset folder.
- **trainer.py**: Trains the face recognition model using the captured face samples.
- **homesecurity.py**: Runs the face recognition system, detects faces, and alerts for unknown users.
- **sample.py**: A simple script to check if the camera is working correctly.

## My Contributions
- Improved the original face detection code by adding visual effects and rounded rectangles for a more aesthetic appearance.
- Created a more user-friendly alert system that plays audio for unknown users.
- Updated the code to use the latest versions of libraries, ensuring compatibility and performance.
- Enhanced the project by implementing features like color-coded user recognition and real-time alerts.

## References
This project is based on the original repository found at:  
https://github.com/skanipakala/Machine-Learning-Face-Recognition-using-openCV

