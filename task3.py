import cv2

#load the image
img = cv2.imread("img_10th_frame.jpg")

#show the image
cv2.imshow('image',img)

#image stays on the screen till any key is pressed
cv2.waitKey(0)