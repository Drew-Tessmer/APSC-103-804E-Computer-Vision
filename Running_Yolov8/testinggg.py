import os
import cv2
from ultralytics import YOLO

# Define the directory path
VIDEO_DIR = r'C:\Users\santo\Downloads\Path yolov8\videos'

# Construct the full path to the input video
video_path = os.path.join(VIDEO_DIR, 'video3.mp4')

# Construct the output video path
video_path_out = '{}_out.mp4'.format(os.path.splitext(video_path)[0])

# Open the input video
cap = cv2.VideoCapture(video_path)

# Check if the video capture object is opened successfully
if not cap.isOpened():
    print("Error: Failed to open video '{}'.".format(video_path))
    exit()

# Read the first frame
ret, frame = cap.read()

# Check if the frame is read successfully
if not ret or frame is None:
    print("Error: Failed to read frame from video '{}'.".format(video_path))
    exit()

# Get the height and width of the frame
H, W, _ = frame.shape

# Create a VideoWriter object to write the output video
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Path to the YOLO model
model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

# Load the YOLO model
model = YOLO(model_path)

# Detection threshold
threshold = 0.5

# Loop through each frame in the video
while ret:
    # Perform object detection on the frame
    results = model(frame)[0]

    # Loop through each detected object
    for result in results.xyxy:
        x1, y1, x2, y2, score, class_id = result

        # If the confidence score is above the threshold, draw the bounding box and label
        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Write the frame with detections to the output video
    out.write(frame)

    # Read the next frame
    ret, frame = cap.read()

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()
