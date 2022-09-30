import cv2
imagem = cv2.imread('lampada.png')
cv2.imshow("Imagem original", imagem)

# Percorre toda a altura a cada 10 pixels
for y in range(0, imagem.shape[0], 10):
	# Percorre toda a largura a cada 10 pixels
	for x in range(0, imagem.shape[1], 10):
		# Na minha imagem, a cada 10 pixels, utiliza do pixel atual + 5 pixels para modificar a cor deles, assim, desenhando um quadrado mas permitindo que a imagem ainda possa ser vista
		imagem[y:y+5, x: x+5] = (0,255,4)
cv2.imshow("Imagem modificada", imagem)

cv2.waitKey()