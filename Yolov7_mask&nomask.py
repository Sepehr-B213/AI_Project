# -*- coding: utf-8 -*-
"""project_Yolov7 (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hXlGP1Qv2NfvzHYlOCH5bgxcRzm6ajaW
"""

# Commented out IPython magic to ensure Python compatibility.
# Download YOLOv7 repository and install requirements
!git clone https://github.com/WongKinYiu/yolov7
# %cd yolov7
!pip install -r requirements.txt

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="XNLDkGz83sVN1E9iitoB")
project = rf.workspace("joseph-nelson").project("mask-wearing")
dataset = project.version(19).download("yolov7")

# Commented out IPython magic to ensure Python compatibility.
# download COCO starting checkpoint
# %cd /content/yolov7
!wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt

# Commented out IPython magic to ensure Python compatibility.
# run this cell to begin training
# %cd /content/yolov7
!python train.py --batch 16 --cfg cfg/training/yolov7.yaml --epochs 50 --data /content/yolov7/Mask-Wearing-19/data.yaml --weights 'yolov7_training.pt' --device 0

# Run evaluation
!python detect.py --weights runs/train/exp/weights/best.pt --conf 0.1 --source /content/yolov7/Mask-Wearing-19/test/images

#display inference on ALL test images

import glob
from IPython.display import Image, display

i = 0
limit = 10 # max images to print
for imageName in glob.glob('/content/yolov7/runs/detect/exp/*.jpg'): #assuming JPG
    if i < limit:
      display(Image(filename=imageName))
      print("\n")
    i = i + 1

import glob
from IPython.display import Image, display

i = 0
limit = 100 # max images to print
for imageName in glob.glob('/content/yolov7/runs/train/exp/*.png'): #assuming JPG
    if i < limit:
      display(Image(filename=imageName, width=600))
      print("\n")
    i = i + 1

#Image("/content/yolov7/runs/train/exp/confusion_matrix.png")

cp /content/yolov7/Mask-Wearing-19/best.pt /content/sample_data