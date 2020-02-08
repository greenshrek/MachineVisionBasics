import cv2


video_file = cv2.VideoCapture("output.avi")

# Check if video file is opened successfully
if (video_file.isOpened()== False): 
  print("Error opening web camera")

count = 10

while(True):

    ret, frame = video_file.read()

    #write the 10th frame in the file
    if count == 10:
      cv2.imwrite('img_10th_frame.jpg',frame)
      break
    
    count += 1

#destroy the session when a is pressed
video_file.release()
cv2.destroyAllWindows()