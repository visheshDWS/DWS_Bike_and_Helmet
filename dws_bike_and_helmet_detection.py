# -*- coding: utf-8 -*-
"""DWS_Bike_and_Helmet_Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-ddNogOIRfKgSD6abazkKtsfNiJ5Qvc

#Install Dependencies

_(Remember to choose GPU in Runtime if not already selected. Runtime --> Change Runtime Type --> Hardware accelerator --> GPU)_
"""

# clone YOLOv5 repository
!git clone https://github.com/ultralytics/yolov5  # clone repo

!git reset --hard fbe67e465375231474a2ad80a4389efc77ecff99

!git clone https://github.com/visheshDWS/YoloV5BikeHelmet.git

!git clone https://github.com/visheshDWS/SamplePicsYoloBikeHelmet.git

# Commented out IPython magic to ensure Python compatibility.
# %cd yolov5

# install dependencies as necessary
!pip install -qr requirements.txt  # install dependencies (ignore errors)
import torch

from IPython.display import Image, clear_output  # to display images
from utils.downloads import attempt_download  # to download models/datasets

# clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/yolov5

"""#Run Inference  With Trained Weights
Run inference with a pretrained checkpoint on contents of `test/images` folder downloaded from Roboflow.
"""

pwd

# Commented out IPython magic to ensure Python compatibility.
# when we ran this, we saw .007 second inference time. That is 140 FPS on a TESLA P100!
# use the best weights!
# %cd /content/yolov5/
!python detect.py --weights /content/YoloV5BikeHelmet/BikeYoloV5.pt --img 416 --conf 0.4 --source /content/SamplePicsYoloBikeHelmet --line-thickness 1

# Commented out IPython magic to ensure Python compatibility.
# when we ran this, we saw .007 second inference time. That is 140 FPS on a TESLA P100!
# use the best weights!
# %cd /content/yolov5/
!python detect.py --weights /content/YoloV5BikeHelmet/helmetYoloV5.pt --img 416 --conf 0.4 --source /content/yolov5/runs/detect/exp --line-thickness 1

#display inference on ALL test images
#this looks much better with longer training above

import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp2/*.png'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")