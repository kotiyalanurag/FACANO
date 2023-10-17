<h1 align=center>:adult: FACANO

![](https://img.shields.io/badge/Python-3.9-blue) ![](https://img.shields.io/badge/opencv-4.8.1.78-blue) ![](https://img.shields.io/badge/Contributions-Welcome-brightgreen) ![](https://img.shields.io/badge/LICENSE-MIT-red)</h1>

<p align = left>Using mediapipe for face detection and anonymizing faces using basic opencv blur.</p>

## Overview

FACANO is capable of detecting and anonymizing faces in three different modes i.e., static images, videos, and live webcam feed. It can detect and anonymize multiple faces at once.

## How to get started?

Open the terminal on your mac and type 
```html
mkdir FACANO
```
Then switch to the new directory using
```html
cd FACANO
```
Now clone the repository on your local machine using
```html
git clone https://github.com/kotiyalanurag/FACANO.git
```
Now create a virtual environment using (assuming you have python installed on your machine)
```html
python -m venv env
```
Switch to your new virtual environment using
```html
source env/bin/activate
```
Now install the requirements for this project using
```html
pip install -r requirements.txt
```
Hyperparameters

Model selection can be set to 1 for images where subject is 5 meters away from camera and 0 for images where subject is 2 meters away from camera. Increasing the minimum detection confidence will lead to more accurate detection but 50% is default.

```python
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
```

## How to run using CLI?

This simple script will help you to run the program using the command line interface.

```python
python3 main.py -m mode -n filename -e fileextension -k kernelsize
```

Acceptable modes are image, video, and webcam with .jpg or .mp4 file extensions.

Have fun playing around with the code.