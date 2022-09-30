# Importar o opencv
import cv2

# Carregar a imagem original com o comando imread
imagem = cv2.imread("lampada.png")

# Converter a imagem para escala de cinza
imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#salva a nova imagem criada
cv2.imwrite("imagempb.png", imagem_pb)

# Criar duas telas para apresentar as imagens
cv2.imshow("Original", imagem)
cv2.imshow("PB", imagem_pb)

# Coletando as propriedades da imagem
print ("Altura: %d pixels" % (imagem.shape[0]))
print ("Largura: %d pixels" % (imagem.shape[1]))
print ("Canais: %d"      % (imagem.shape[2]))

# Buscando pixels específicos na imagem para coletar o RGB
(b, g, r) = imagem[0, 0]
print ("Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

(b, g, r) = imagem[305, 250]
print ("Cor do pixel em (250, 305) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

(b, g, r) = imagem[30, 250]
print ("Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

# Salva a nova imagem no diretorio
cv2.imwrite("imagempb.png", imagem_pb)

# Comando para aguardar interrupcao do usuario para fechar a tela
cv2.waitKey()
