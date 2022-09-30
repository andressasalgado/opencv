import cv2

# abrimos a webcam - setamos 0 para indicar qual camera o algoritmo deve buscar, voce pode ter mais de uma, sete a que preferir
video = cv2.VideoCapture(0)

# classificador é o algoritmo haarcascade
classificador = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Já nesse comando while nós criamos a variavel frame, que coleta a leitura da imagem do vídeo
while True:
	conectado, frame = video.read()

	# nós também passamos o frame pra escala de cinza, pois é o recomendado pelo opencv
	frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# variavel que guarda o resultado do metodo detectMultiScale
	facesDetectadas = classificador.detectMultiScale(frameCinza)

	# x, y, l, a sao os resultados encontrados nas facesDetectadas, como podemos ver no print acima
	# x é o ponto na largura
	# y é o ponto na altura
	# l é largura dessa face
	# a é a altura dessa face

	# nesse for ele vai percorrer esses pontos pra poder desenhar o retangulo na face encontrada, primeiro passamos a imagem (e aqui ja podemos usar a imagem colorida), segundo parametro sao os pontos iniciais,
	# o terceiro parametro é a soma dos pontos iniciais com sua respectiva largura e altura, o tamanho que ele tem que criar esse desenho. O quarto parametro é a cor e por ultimo a espessura da borda
	for (x, y, l, a) in facesDetectadas:
		cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 0, 255), 2)

	# criamos a janela pra imagem
	cv2.imshow('Video', frame)
	
	if cv2.waitKey(1) == ord('q'):
		break
		
video.release()
cv2.destroyAllWindows()