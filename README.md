<h1 align=center>:adult: FACANO

![](https://img.shields.io/badge/Python-3.9-blue) ![](https://img.shields.io/badge/opencv-4.8.1.78-blue) ![](https://img.shields.io/badge/Contributions-Welcome-brightgreen) ![](https://img.shields.io/badge/LICENSE-MIT-red)</h1>

<p align = left>Using mediapipe for face detection and anonymizing faces using basic opencv blur.</p>

## Overview

FACANO is capable of detecting and anonymizing faces in three different modes i.e., static images, videos, and live webcam feed. It can detect and anonymize multiple faces at once.

## Hyperparameters

Model selection can be set to 1 for images where the subject is 5 meters away from the camera and 0 for images where the subject is 2 meters away. Increasing the minimum detection confidence will lead to more accurate detection but 50% is default.

```python
with mp_face_detection.FaceDetection(model_selection = 0, min_detection_confidence = 0.5) as face_detection:
```

## Result

Given below is an anonymized image that was blurred using a kernel size of 70.
<p align="center">
  <img src="https://github.com/kotiyalanurag/FACANO/blob/main/src/image001.jpg" max-width=100% height='300' />
  <img src="https://github.com/kotiyalanurag/FACANO/blob/main/output/image001_blur_70.jpg" max-width=100% height='300' />
</p>

Here is another result with a kernel size of 90 and 120.
<p align="center">
  <img src="https://github.com/kotiyalanurag/FACANO/blob/main/src/image002.jpg" max-width=100% height='300' />
  <img src="https://github.com/kotiyalanurag/FACANO/blob/main/output/image002_blur_90.jpg" max-width=100% height='300' />
  <img src="https://github.com/kotiyalanurag/FACANO/blob/main/output/image002_blur_120.jpg" max-width=100% height='300' />
</p>

The images used here were taken from [unsplash.com](https://unsplash.com/) and the video was taken from [pexels.com](https://www.pexels.com/).

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

## How to run using CLI?

Use the following script to run this program using a command line interface.

```python
python3 main.py -m mode -n filename -e fileextension -k kernelsize
```

Acceptable modes are image, video, and webcam with .jpg or .mp4 file extensions.

Have fun playing around with the code.
