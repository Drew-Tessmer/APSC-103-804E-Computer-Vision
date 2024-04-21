import os
import time

from ultralytics import YOLO
import cv2
import numpy as np

VIDEOS_DIR = os.path.join('.','videos')

video_path = os.path.join(VIDEOS_DIR, 'video1.mp4')
video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        assert not isinstance(frame,type(None)), 'frame not found'


model_path = os.path.join('.', 'models', 'yolov8n.pt')

#load a model
model = YOLO(model_path)

threshold = 0.5

