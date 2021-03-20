#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pdb
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys
import pandas as pd

files_name = ["Prototype_organized/c1t1/pic2019.07.15-0528t1_8.jpeg",
              "Prototype_organized/c1t2/pic2019.07.15-2309t2_8.jpeg"]

for filename in files_name:
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
    cv2.imshow("Mask", thresh)
    cv2.imwrite("black_white_"+filename.split("/")[-1], thresh)
    root_percentage = cv2.mean(thresh)[0]/255
    total_image = img.shape[0]*img.shape[1]
    root_area = root_percentage*total_image

    print("Total image area = ", total_image)
    print("Total root area = ", root_area)
    print("Root Percentage = {}%".format(round(root_percentage*100, 2)))
