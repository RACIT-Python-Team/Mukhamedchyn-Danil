import cv2

img = cv2.imread('plan.png')

img = cv2.resize(img, (640, 480))

def CoordPicker(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


video = cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    cv2.namedWindow('CoordPicker')
    cv2.setMouseCallback('CoordPicker', CoordPicker)
    cv2.imshow('CoordPicker', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()