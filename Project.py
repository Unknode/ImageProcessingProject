# importando lib opencv
from cv2 import cv2
import numpy as np

#Carregando uma imagem
img = cv2.imread('images/realFingerPrint.jpg')

#crop = img[:,30:180]
#mostrando a imagem na tela
cv2.imshow("Imagem original", img)

#Parametro define quantos milissegundos a imagem ira ficar na tela.
cv2.waitKey(0) 

#Convertendo a imagem para escala de cinza
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Método para remover ruido (Ajustando)
#new_gray_image = cv2.fastNlMeansDenoising(gray_image,None,10,10,7,21)
#cv2.imshow("Nova Imagem Alterada", new_gray_image)
#cv2.waitKey(0) 

cv2.imshow("Imagem Alterada", gray_image)
cv2.waitKey(0) 

#Aplicando threshold na imagem
ret, threshold_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_BINARY)
#ret, threshold_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_BINARY_INV)
#ret, threshold_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_TRUNC)
#ret, threshold_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_TOZERO)
#ret, threshold_image = cv2.threshold(gray_image, 127,255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Imagem Threshold", threshold_image)
cv2.waitKey(0) 

cv2.destroyAllWindows()

#Salvando a nova imagem
cv2.imwrite('imgGrayImage.jpg', gray_image)

