import cv2

artem=cv2.imread(r'C:\Users\danam\PycharmProjects\Mukhamedchyn-Danil\photo\Artem.jpg')
GrAY_Artem=cv2.cvtColor(artem, cv2.COLOR_BGR2GRAY)
Blur_Artem=cv2.GaussianBlur(GrAY_Artem, (7,7), 0)
cv2.imshow('Artemko', artem)
cv2.imshow('GrAY Artemko', Blur_Artem)
cv2.imwrite('photo/Gray_Artem.jpg', Blur_Artem)
cv2.imwrite('photo/Artemko_copy.jpg', artem)
cv2.waitKey(0)
cv2.destroyAllWindows()