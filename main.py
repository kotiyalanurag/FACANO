import os
import cv2
import argparse
import mediapipe as mp

from utils import blur_pipeline

# set up parsable arguments for CLI
parser = argparse.ArgumentParser()

parser.add_argument('-m', '--mode', default = 'image', help = 'Enter image, video, or webcam')
parser.add_argument('-n', '--filename', default = 'image001', help = 'Enter file name')
parser.add_argument('-e', '--fileext', default = '.jpg', help = 'Enter file extension .jpg, .MP4')
parser.add_argument('-k', '--kernel', type=int, default = 70, help = 'Enter kernel size for blurring')

args = parser.parse_args()

# set up output directory
output_dir = './output'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# read image or video
file_name = args.filename
file_ext = args.fileext
        
file_path = os.path.join('.', 'src', file_name + file_ext)

# face detection
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    if args.mode == 'image':
        image = cv2.imread(file_path)
        
        # blurring pipeline
        image = blur_pipeline(image, face_detection, args.kernel)
        
        # saving blurred image
        filename_out = os.path.join(output_dir, args.filename + '_blur_' + str(args.kernel) + args.fileext)
        
        if filename_out not in os.listdir(output_dir):
            cv2.imwrite(filename_out, image)

    elif args.mode == 'video': 
        video = cv2.VideoCapture(file_path)
        ret, frame = video.read()
        
        fps = video.get(cv2.CAP_PROP_FPS)
        
        FH, FW = frame.shape[:2]
        
        filename_out = os.path.join(output_dir, args.filename + "_blur_" + str(args.kernel) + args.fileext)   
        video_out = cv2.VideoWriter(filename_out,
                                    cv2.VideoWriter_fourcc(*'mp4v'), 
                                    fps, 
                                    (FW, FH))
            
        while ret:
            # blurring pipeline processes the video frame by frame
            frame = blur_pipeline(frame, face_detection, args.kernel)
            # writing a new video with blurred faces after detection
            video_out.write(frame)
            # reading the next frame and sending it through blurring pipeline
            ret, frame = video.read()

        video.release()
        video_out.release()

    elif args.mode == 'webcam':
        webcam = cv2.VideoCapture(1)
        ret, frame = webcam.read()

        while ret:
            # blurring the webcam input frame by frame
            frame = blur_pipeline(frame, face_detection, args.kernel)

            cv2.imshow('Face Blur Webcam', frame)
            if cv2.waitKey(40) & 0xFF == ord('q'):
                break

            ret, frame = webcam.read()

        webcam.release()
        cv2.destroyAllWindows()