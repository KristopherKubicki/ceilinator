# ceilinator
Simple python3 and OpenCV method for segmenting the ceiling inside a building

<img src='https://user-images.githubusercontent.com/478212/41077963-76234b1a-69df-11e8-8977-acc955a8c09f.gif'>

A simple, moving fish-eye camera can quickly map an indoor space.  A common intermediate step is to segment the ceiling from other objects in natural video.  This repository offers a simple, fast solution to get started. 

ceilinator works given a few assumptions:
  * The input video or image is recorded with a fish-eye lense facing directly up
  * The ceiling is relatively uniform in color and texture
  * No objects are obstructing the center of the view
  
The script downsizes each frame and converts it to grayscale.  It then detects all regions of the image similar to the region of interest directly overhead.  The largest contour that includes this ROI is then chosen as the ceiling mask.  The script displays the ROI in a viewport, but you'll want to use the contour points for your application. 

Feel free to test with the included videos in the data/ directory
