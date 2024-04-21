import os

from ultralytics import YOLO
import cv2
# Define the directory path
VIDEO_DIR = r'C:\Users\santo\Downloads\Path yolov8\videos'

# Construct the full path to the input video
video_path = os.path.join(VIDEO_DIR, 'video3.mp4')

# Construct the output video path
video_path_out = '{}_out.mp4'.format(os.path.splitext(video_path)[0])

# Open the input video
cap = cv2.VideoCapture(video_path)

# Open a camera (assuming you want to capture from the webcam)
# If you want to capture from a different video source, change the argument accordingly
# For example, for a secondary camera, use cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        assert not isinstance(frame,type(None)), 'frame not found'

ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (H, W))

model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

while ret:

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()