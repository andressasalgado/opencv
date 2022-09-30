import cv2
classificador = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
imagem = cv2.imread('beatles.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza)

print(len(facesDetectadas))

print(facesDetectadas)

for (x, y, l, a) in facesDetectadas:
	cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

cv2.imshow("Original", imagem)
#cv2.imshow("PB", imagemCinza)

#print(imagem.shape)

cv2.waitKey()