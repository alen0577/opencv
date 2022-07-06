import cv2
import numpy as np

image = cv2.imread('nature.jpg', 1)
blur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('org', image)
cv2.imshow('blur', blur)
cv2.imshow('gaussian', gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
