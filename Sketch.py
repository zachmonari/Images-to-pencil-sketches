import cv2
image=cv2.imread("z1.jpg")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted=255-gray_image
blur=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blur=255-blur
sketch=cv2.divide(gray_image,inverted_blur,scale=256.0)
cv2.imwrite("zz1.png", sketch)
cv2.imshow("image", sketch)
