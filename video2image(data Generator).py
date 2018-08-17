import cv2

cap = cv2.VideoCapture('C:/Users/satinder/Desktop/center5.mp4')
ret = True
i = 0
j = 3772
while ret:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow('s', frame)
    if i%5 == 0:
        cv2.imwrite('C:/Users/satinder/Desktop/center/'+str(j)+'.jpg', frame)
        j = j+1
    i = i+1
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cv2.destroyAllWindows()
