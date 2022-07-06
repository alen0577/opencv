import cv2

img = cv2.imread('download.jpg', 1)
cv2.line(img, (0, 0), (400, 400), (255, 0, 0), 5)
cv2.rectangle(img, (0, 0), (400, 400), (0, 255, 0), 3)
cv2.circle(img, (200, 200), 200, (0, 0, 255), -1)
font = cv2.FONT_ITALIC
cv2.putText(img, 'hai', (200, 200), font, 4, (255, 255, 255), cv2.LINE_AA)
cv2.imshow('bg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
