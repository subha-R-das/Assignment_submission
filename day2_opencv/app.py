import cv2
import numpy as np

image= cv2.imread('goku.jpg')

gray_image = cv2.imread('goku.jpg',0)


zeros = np.zeros((image.shape[0],image.shape[1],), np.uint8)
b,g,r = cv2.split(image)
print('blue channel',b)
print('green channel',g)
print('red channel',r)
# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow('frame Goku', gray_image)
# cv2.imshow('frame Goku gray', image)



blue = cv2.merge([b,zeros,zeros])
green = cv2.merge([zeros,g,zeros])
red = cv2.merge([zeros,zeros,r])

custom_image = cv2.merge([b,g+100,r])

# cv2.imwrite('blue.png',blue)
# cv2.imshow('Blue',blue) 
# cv2.imshow('green',green) 
# cv2.imshow('red',red) 
cv2.imshow('custom_image',custom_image)
cv2.waitKey(0)