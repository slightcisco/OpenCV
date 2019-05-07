import cv2
import numpy as np
import time

font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while cap.isOpened():

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, threshold = cv2.threshold(blur, 235, 255, cv2.THRESH_BINARY)


    contors, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contors[1:]:
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        cv2.drawContours(frame, [approx], 0, (0), 5)
        cv2.drawContours(blur, [approx], 0, (0), 5)
        x = approx.ravel() [0]
        y = approx.ravel() [1]
        if len(approx) == 3:
            cv2.putText(frame, "Triangle", (x,y), font, 1, (0,0,255))
            cv2.putText(blur, "Triangle", (x,y), font, 1, (0,0,255))
            print("TRIANGLE")
        elif len(approx) == 4:
            cv2.putText(frame, "Rectangle", (x,y), font, 1, (0,0,255))
            cv2.putText(blur, "Rectangle", (x,y), font, 1, (0,0,255))
            print("RECTANGLE")
        elif len(approx) == 5:
            cv2.putText(frame, "Pentagon", (x,y), font, 1, (0,0,255))
            cv2.putText(blur, "Pentagon", (x,y), font, 1, (0,0,255))
            print("PENTAGON")
        elif len(approx) == 6:
            cv2.putText(frame, "Hexagon", (x,y), font, 1, (0,0,255))
            cv2.putText(blur, "Hexagon", (x,y), font, 1, (0,0,255))
            print("HEXAGON")
        elif len(approx) == 8:
            cv2.putText(frame, "Octagon", (x,y), font, 1, (0,0,255))
            cv2.putText(blur, "Octagon", (x,y), font, 1, (0,0,255))
            print("OCTAGON")
    time.sleep(.1)
    cv2.imshow("Original", frame)
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
