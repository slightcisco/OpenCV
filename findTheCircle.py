import cv2
import numpy as np
import time
font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while cap.isOpened():
    circlesx = []
    circlesy = []
    trianglex = []
    triangley = []
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, threshold = cv2.threshold(blur, 180, 240, cv2.THRESH_BINARY)
    contors, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contors[1:]:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(blur, [approx], 0, (0), 5)
        data = approx.ravel()
        x = data[0]
        y = data[1]
        avgx = []
        avgy = []
        for i in range(int(len(data)/2)):
            avgx.append(data[2*i])
            avgy.append(data[2*i+1])
        x = int(np.mean(avgx))
        y = int(np.mean(avgy))
        if len(approx) > 6:
            circlesx.append(x)
            circlesy.append(y)
            cv2.putText(blur, ".", (x,y), font, 10, (0,0,255))
    if len(circlesx) == 1:
        x = circlesx[0]
        y = circlesy[0]
        cv2.putText(frame, "Circle", (x,y), font, 1, (0,0,255))
        print("Circle is at")
        print("x: " + str(x))
        print("y: " + str(y))

    if len(trianglex) == 1:
        x = trianglex[0]
        y = triangley[0]
        cv2.putText(frame, "Triangle", (x,y), font, 1, (0,0,255))
        print("Triangle is at")
        print("x: " + str(x))
        print("y: " + str(y))

    time.sleep(.1)
    cv2.imshow("output", threshold)
    cv2.imshow("blur", blur)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
#cv2.imshow("shapes", img)
#cv2.imshow("original", og)
#cv2.imshow("contours", cntImg)
