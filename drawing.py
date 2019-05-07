import cv2
import numpy as np

#img = cv2.imread("images/lena.jpg", 1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
img = cv2.arrowedLine(img, (0,0), (100,255), (255,0,0), 5)

img = cv2.rectangle(img, (10,10), (300,300), (0,255,0), 5)
img = cv2.circle(img, (230,230), 50, (255,255,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Hello World", (100,500), font, 4, (255,0,0), 4, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
