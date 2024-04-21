
from ultralytics import YOLO

# Load a model
model = YOLO('../runs/detect/train18/weights/best.pt')

# Customize validation settings
validation_results = model.val(data='config.yaml',
                               imgsz=1300,
                               batch=16,
                               conf=0.25,
                               iou=0.6,
                               device='cpu')