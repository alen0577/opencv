import cv2
import numpy as np

image = cv2.imread('blue.jpg', 1)
cv2.imshow('org', image)
new_img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow('new_img', new_img)

lower_boundary = np.array([70, 50, 50])
upper_boundary = np.array([80, 255, 255])
mask = cv2.inRange(new_img, lower_boundary, upper_boundary)
cv2.imshow('mask', mask)

res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
