import cv2
import numpy as np
url="https://192.168.43.1:8080/video"
cap=cv2.VideoCapture(url)
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
out=cv2.VideoWriter('output.mp4v',fourcc,20.0,(480,360))
while(cap.isOpened()):
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lined=cv2.line(gray,(0,0),(240,360),(255,0,0),5)
    cv2.imshow("Faces Found",lined)
    out.write(lined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
