import cv2

img = cv2.imread("images/lena.jpg", 1)

img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
img = cv2.arrowedLine(img, (0,0), (100,255), (255,0,0), 5)

img = cv2.rectangle(img, (10,10), (300,300), (0,255,0), 5)

cv2.imshow('image', img)
cv2.waitKey(5000)
