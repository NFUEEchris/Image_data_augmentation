import cv2
import os

cap = cv2.VideoCapture('C:\\Users\\bblow\\Downloads\\aa.mp4')
save_file='G:\\save_file'
sec=10



i=0
fps=10*30 #set video are 30fps
while(cap.isOpened()):
  ret, frame = cap.read()
  
  if i%fps==0:
    cv2.imwrite(save_file+"\\frame_"+str(int(i/fps))+".jpg",frame)
  i+=1

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()