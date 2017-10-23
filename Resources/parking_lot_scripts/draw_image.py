#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:26:00 2017

@author: griffin
"""

import numpy as np
import cv2 as cv
 
img = cv.imread('/Volumes/1TBHDD/code/repos/5443-Data-Mining/Resources/parking_lot_scripts/UFPRO4_example.jpg')
img = cv.rectangle(img, (250,70), (330,150), (0,255,0), 4)

crop_img = img[0:100, 0:100]
    
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "This one!", (230, 50), font, 0.8, (0, 255, 0), 2, cv.LINE_AA)
           

cv.imshow('Draw01',img)
cv.imshow("cropped", crop_img)
cv.waitKey(0)

