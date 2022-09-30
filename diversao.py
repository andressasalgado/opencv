import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('lampada.png')
#Cria um retangulo azul por toda a largura da imagem
image[30:50, :] = (255, 0, 0)
#Cria um quadrado vermelho
image[100:150, 50:100] = (0, 0, 255)
#Cria um retangulo amarelo por toda a altura da imagem
image[:, 200:220] = (0, 255, 255)
#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a
350
image[150:300, 250:350] = (0, 255, 0)
#Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a
350
image[300:400, 50:150] = (255, 255, 0)
#Cria um quadrado branco
image[250:350, 300:400] = (255, 255, 255)
#Cria um quadrado preto
image[70:100, 300: 450] = (0, 0, 0)
cv2.imshow("Imagem alterada", image)
cv2.imwrite("alterada.jpg", image)


#img = cv2.imread('lampada.png')
#(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
#zeros = np.zeros(img.shape[:2], dtype = "uint8")
#cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
#cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
#cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
#cv2.imshow("Original", img)

img = cv2.imread('lampada.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255,cv2.THRESH_BINARY_INV)
resultado = np.vstack([np.hstack([suave, bin]),np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])])
cv2.imshow("Binarização da imagem", resultado)




cv2.waitKey(0)
