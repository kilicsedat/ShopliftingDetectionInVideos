# -*- coding: utf-8 -*-
"""video_capture and framing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DH71Z3KC4kJvOJYz0TjnKI49g5QJ1AlE
"""

from google.colab import drive
drive.mount('/content/gdrive')

import cv2
import os
from google.colab.patches import cv2_imshow

filen = '/content/gdrive/MyDrive/sample data/Annotations_for_shoplifting.txt'
with open (filen, 'r')as f:
  lines = f.read().splitlines(keepends=False)
  print(lines[0])
  for line in lines: 
    line = line.split()
    print(line[0], line[2])

path_to_videos = '/content/gdrive/MyDrive/sample data/Shoplifting_videos'
print(os.path.join(path_to_videos, line[0]))
vid = cv2.VideoCapture(str(os.path.join(path_to_videos, line[0])))
font = cv2.FONT_HERSHEY_SIMPLEX
org=(5,25)
fontScale = 1
color = (255, 125, 125)
thickness = 2

while(True):
  ret, frame = vid.read()
  frame_no = vid.get(cv2.CAP_PROP_POS_FRAMES)
  if (int(line[2])-500) < int(frame_no) < int(line[2]):
    frame_no = str(frame_no)
    cv2.putText(frame, frame_no, org, font, fontScale, color, thickness)
    cv2_imshow(frame)
  elif int(frame_no) >= int(line[2]):
    break
  else:
    continue

cv2.waitKey(1)
