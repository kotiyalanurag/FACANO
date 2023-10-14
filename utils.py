import os
import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

def blur_pipeline(file, face_detection, kernel):    
    '''
    this function reads an input image and detects faces in the given
    image after which we apply normal blurring using opencv for the
    detected region in the image
    '''
    H, W, _ = file.shape # file shape in height, width format
   
    results = face_detection.process(cv2.cvtColor(file, cv2.COLOR_BGR2RGB))
   
    if results.detections is not None:
        
        for detection in results.detections:
            # print(detection)
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            
            # storing bounding box coordinates of face detection (values normalised between 0 & 1)
            x_min = bbox.xmin
            y_min = bbox.ymin
            w = bbox.width
            h = bbox.height

            # getting actual coordinates by multiplying normalized values with image dimensions
            x_min = int(x_min * W)
            y_min = int(y_min * H)
            w = int(w * W)
            h = int(h * H)
            
            # applying normal blurring to detected region
            file[y_min:y_min+h, x_min:x_min+w, :] = cv2.blur(
                file[y_min:y_min+h, x_min:x_min+w, :], (kernel, kernel))
         
    return file