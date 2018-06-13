#!/usr/bin/python3
# coding: utf-8
#

import numpy as np
import cv2

cap = cv2.VideoCapture('./data/costco_2.mp4')

while(True):
    ret, frame = cap.read()
    if not ret:
      break
  
    # resize the frame to a future magic number
    frame = cv2.resize(frame,(224,224))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,254,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    thresh = cv2.bitwise_not(thresh)

    # block out the edges of the screen
    cv2.circle(thresh,(113,113), 165, (0,0,0), 100) 
    thresh = cv2.inRange(thresh,254,255)

    # find the contours in the selected area
    _,cnts,_ = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
      # find the first contour that includes the point directly overhead
      if cv2.pointPolygonTest(cnt, (112,112), True) > 0:
        # winner: this contour defines the area we want to gist against
        cv2.drawContours(frame, [cnt], -1, (0,255,0), 3)
        break

    # display the green contour against the proper frame
    cv2.imshow('frame',frame)

    key = cv2.waitKey(1)
    if 'q' == chr(key & 255):
      break

cap.release()
cv2.destroyAllWindows()
