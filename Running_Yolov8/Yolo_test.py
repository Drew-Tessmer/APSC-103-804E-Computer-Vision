from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
#
# # Use the model
# model.train(data="config.yaml", epochs=1)  # train the model
#
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format
# print(path)

import cv2
model=YOLO('yolov8n.pt') #this uses a PreTrained model THOMAS ZAMIN << TALK
result=model("runs/detect/train23/weights/results.csv")
cv2.waitkey(0)

from ultralytics import YOLO

# Load a model
model = YOLO('path/to/last.pt')  # load a partially trained model

# Resume training
results = model.train(resume=True)