import cv2

fps = 80
camera = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (int(camera.get(3)), int(camera.get(4))))

# Check if camera opened successfully
if (camera.isOpened()== False): 
  print("Error opening web camera")

while(camera.isOpened()):

    ret, frame = camera.read()

    if ret == True:

        #write the frames in the file
        out.write(frame)

        #display the results
        cv2.imshow('frame', frame)

        #press a to stop recording
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    else:
        break
#destroy the session when a is pressed
out.release()
camera.release()
cv2.destroyAllWindows()