# Importing OpenCV Library
import cv2
import numpy as np
# Relative or absolute path of the input image file
path = "F:/buildclub/image processing/tom.jpeg"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
# Display image in a window
#cv2.imshow("Output",image)

draw = False
p1 = (0,0) # top left cornor point
p2 = p1 # bottom right cornor point
cropped_image = None
# Mouse callback function
def mouseClick(event,xPos,yPos,flags,param):
 # print(event,xPos,yPos,flags,param)
 # Global variables shared between the mouseClick function and rest ofthe code
 # if left click press event, start drawing with p1 as top left cornorpoint coordinates
 global draw,p1,p2 ,cropped_image
 if event==cv2.EVENT_LBUTTONDOWN:
  draw = True
  p1 = (xPos,yPos)
  p2 = p1 # Continuously update bottom right cornor point (p2) of rectangle onmouse move event
 if event==cv2.EVENT_MOUSEMOVE and draw:
  p2 = (xPos,yPos) # if left click release, stop drawing
 if event==cv2.EVENT_LBUTTONUP:
  draw = False 
  cropped_image = crop_image(image, p1, p2)
  cv2.imshow("Cropped Image", cropped_image)
  cv2.waitKey(0)

def crop_image(image, p1, p2): # Ensure p1 is the top-left point and p2 is the bottom-right point
    x1, y1 = min(p1[0], p2[0]), min(p1[1], p2[1])
    x2, y2 = max(p1[0], p2[0]), max(p1[1], p2[1])
    cropped = image[y1:y2, x1:x2]
    return cropped

  # Creating a black image/frame (0 pixel value) of 500x500 size
frame = cv2.imread(path)# Creating an window to display image/frame
cv2.namedWindow('FRAME')  # This function detects every new events and triggers the "mouseClick"function
cv2.setMouseCallback('FRAME',mouseClick)
while True:
  frame = cv2.imread(path)# Creating an window to display image/frame
  rect = cv2.rectangle(frame,p1,p2,(0,0,255),2)
  cv2.imshow('FRAME',frame)
  if cv2.waitKey(1) & 0xff == ord('q'): # to quit press 'q'
   break
cv2.destroyAllWindows()
