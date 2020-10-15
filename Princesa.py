import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image, ImageDraw

#1. dibujar canvas
blank_image = Image.new('RGB', (40, 40), 'white')
img_draw = ImageDraw.Draw(blank_image)

#2. guardar la imagen
blank_image.save('blank_image.jpg')

#3. abrir la imagen utilizando el nombre que ya esta en la ruta por defecto del Colab
img = Image.open('blank_image.jpg')

#4. Como plt sabe cómo manejar la instancia de la clase Image, simplemente ingrese su imagen cargada al método imshow
plt.imshow(img, origin="lower")


from matplotlib.pyplot import imshow
from PIL import Image, ImageDraw

def ROUND(a):
	return int(a + 0.5)
 
def drawDDA(x1,y1,x2,y2,img_draw):
  #1. identificar los diferenciales (los pixeles que van a recorrer en cada eje)
  dx = (x2-x1)
  dy = (y2-y1)

  #2. determinar el largo de la linea
  length = dx if dx > dy else dy

  #3. calcular incrementos en x & y
  ix = dx/length
  iy = dy/length

  #4. asignar los puntos de inicio
  x,y = x1,y1

  #5. pintar los puntos de inicio
  img_draw.point((ROUND(x),ROUND(y)),fill='black')
  
  #6. aqui inicia el dibujo de los demás puntos de la linea hasta el final
  for i in range(length):
    x += ix
    y += iy
    img_draw.point((ROUND(x),ROUND(y)),fill='black')

#aqui termina el algoritmo de DDA

#abrir el canvas creado anteriormente
img = Image.open('blank_image.jpg')

#llamar al ImageDraw de Pillow para manipular la imagen abierta 
img_draw = ImageDraw.Draw(img)

#dibujar las lineas
%timeit drawDDA(1,1,17,1,img_draw)
%timeit drawDDA(1,1,1,4,img_draw)
%timeit drawDDA(1,1,17,1,img_draw)
%timeit drawDDA(17,2,17,3,img_draw)
%timeit drawDDA(2,5,2,7,img_draw)
%timeit drawDDA(16,4,16,6,img_draw)
%timeit drawDDA(15,7,15,8,img_draw)
%timeit drawDDA(14,9,14,10,img_draw)
%timeit drawDDA(8,7,13,11,img_draw)
%timeit drawDDA(10,8,10,9,img_draw)
%timeit drawDDA(6,7,7,7,img_draw)
%timeit drawDDA(6,8,6,9,img_draw)
%timeit drawDDA(5,7,4,8,img_draw)
%timeit drawDDA(3,8,3,10,img_draw)
%timeit drawDDA(2,10,2,16,img_draw)
%timeit drawDDA(5,10,5,12,img_draw)
%timeit drawDDA(4,13,4,14,img_draw)
#%timeit drawDDA(2,12,3,12,img_draw)
%timeit drawDDA(8,10,10,12,img_draw)
%timeit drawDDA(7,10,8,10,img_draw)
%timeit drawDDA(2,11,4,13,img_draw)
%timeit drawDDA(10,12,12,10,img_draw)

%timeit drawDDA(3,17,5,17,img_draw)
%timeit drawDDA(8,17,14,17,img_draw)
%timeit drawDDA(15,15,15,16,img_draw)
%timeit drawDDA(18,15,18,17,img_draw)
%timeit drawDDA(16,13,17,15,img_draw)
%timeit drawDDA(16,11,17,12,img_draw)

%timeit drawDDA(2,18,2,19,img_draw)
%timeit drawDDA(4,18,4,19,img_draw)
%timeit drawDDA(3,19,3,22,img_draw)
%timeit drawDDA(4,19,5,18,img_draw)

%timeit drawDDA(5,22,5,23,img_draw)
%timeit drawDDA(8,22,8,23,img_draw)
%timeit drawDDA(11,18,11,19,img_draw)
%timeit drawDDA(11,21,11,23,img_draw)
%timeit drawDDA(12,23,13,23,img_draw)
%timeit drawDDA(13,21,13,22,img_draw)

%timeit drawDDA(3,23,4,24,img_draw)
%timeit drawDDA(4,25,5,25,img_draw)
%timeit drawDDA(6,24,7,24,img_draw)
%timeit drawDDA(8,25,9,25,img_draw)
%timeit drawDDA(9,24,10,24,img_draw)

%timeit drawDDA(1,24,2,23,img_draw)
%timeit drawDDA(1,25,2,26,img_draw)
%timeit drawDDA(2,27,3,28,img_draw)
%timeit drawDDA(3,29,4,30,img_draw)
%timeit drawDDA(4,31,5,32,img_draw)
%timeit drawDDA(6,31,7,32,img_draw)
%timeit drawDDA(8,31,9,32,img_draw)
%timeit drawDDA(5,29,8,29,img_draw)
%timeit drawDDA(9,29,10,30,img_draw)
%timeit drawDDA(10,31,12,29,img_draw)
%timeit drawDDA(13,29,15,27,img_draw)
%timeit drawDDA(16,27,17,27,img_draw)

%timeit drawDDA(17,18,18,19,img_draw)
%timeit drawDDA(16,22,18,20,img_draw)
%timeit drawDDA(16,23,17,24,img_draw)
%timeit drawDDA(16,25,17,26,img_draw)

%timeit drawDDA(2,14,4,14,img_draw)
%timeit drawDDA(6,19,7,19,img_draw)

%timeit drawDDA(10,13,10,14,img_draw)
%timeit drawDDA(11,14,14,14,img_draw)
%timeit drawDDA(13,12,13,13,img_draw)
%timeit drawDDA(14,11,16,11,img_draw)
