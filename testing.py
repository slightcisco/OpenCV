import cv2

print("Open CV Version")
print(cv2.__version__)

img = cv2.imread("images/lena.jpg", 0)
print(img)

cv2.imshow('image', img)
