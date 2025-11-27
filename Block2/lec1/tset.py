import cv2

print(cv2.__version__)
image = cv2.imread('photo/Artemko_copy.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()