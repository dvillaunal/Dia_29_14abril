# Que es "Scikit-Image":

'''
Scikit-image, o skimage,
es un paquete Python de código abierto
diseñado para el preprocesamiento de imágenes
'''

# Cargando imagenes desde la maquina:

'''
¿Y si quieres cargar una imagen desde tu máquina en lugar de las que se proporcionan en el paquete?
Seguro que eso es lo que querrás hacer en algún momento. Para ello, podemos utilizar la función imread de skimage.

Podemos leer imágenes en dos formatos: en color y en escala de grises.
Veremos ambos en acción y entenderemos en qué se diferencian.

----------------------------------------------------
                   Nota:
La función imread tiene un parámetro "as_gray"
que se utiliza para especificar si la imagen debe
convertirse en una imagen en escala de grises o no.
----------------------------------------------------

'''

from skimage.io import imread, imshow, imsave
import matplotlib.pyplot as plt
# Expliación en .md
# %matplotlib inline <- no entedi porque no ejecuto en el replit

# Exportamos la imagen contenida en eldirectorio:

'Especificamos al importar la imagen que sea en escala de Grises con el as_gray = True'
image_gray = imread('images.jpg', as_gray=True)

'Guardamos nuestra primera imagen  nuestra imagen'
'le especificamos el formato despues de la coma la variable (imagen) a guardar'
imsave('image_gray.jpg', image_gray)


'''
Podemos ver fácilmente la imagen utilizando la función imshow.
Pero
¿es realmente así como se almacena la imagen?
Comprobemos lo que tenemos en la variable image_gray:
'''
# Print(image_gray):
'''
La variable almacena la imagen en forma de matriz de números.
Como puede ver,
la forma de la matriz es de 259 x 195.
Estos números se denominan valores de píxel y
denotan la intensidad de los píxeles en las imágenes.

Ahora,
cargaremos la imagen en el formato de color original.
Para ello, tendremos que establecer el parámetro 'as_gray' en False:
'''
print('Soy una matriz => ',image_gray.shape)
print(image_gray)
####################################################################

# En formato original
'Especificamos que  NO sea en escala de grises, en caso contrario TRUE'
image_color = imread('images.jpg', as_gray=False)
'Imprimimos las dimensiones de nuestra imagen'
print(image_color.shape)

'Imprimimos nuestra imagen'
# imsave(image_color) <- imprime la imgen dentro del ()

# Cambiar el formato de la imagen
'''
formatos populares son HSV (tono, saturación, valor) y
HSL (tono, saturación, luminosidad) que son
representaciones alternativas del formato RGB.
Voy a explicar brevemente lo que significa cada uno de estos términos.

El matiz es un grado en la rueda de color donde 0 es para el rojo,
120 es el verde, 240 es el azul y de nuevo 360 sería el rojo.

La saturación representa el porcentaje de ese color,
donde 0 es el blanco y 100 es el color completo.

El valor denota la mezcla de los colores con cantidades variables de pintura negra o blanca.
La luminosidad es otra forma de mostrar el tono de la imagen, donde 0 es negro y 1 es blanco
'''

from skimage.color import rgb2hsv
'importamos rgb2hsv para convertir de formato RGB a HSV'

' leemos los datos'
img = imread('images.jpg')

'Conversion a formato HSV'
img_hsv = rgb2hsv(img)

'Creamos un plot donde contenga la foto RGB'
plt.subplot(121), imshow(img)
'Titulo del plot anterior'
plt.title('Formato RGB') 

'Un subplot para mostrar el vs de RGB y HSV'
plt.subplot(122), imshow(img_hsv)
'Titulo del subplot'
plt.title('Formato HSV') 

'Imprimimos y exportamos el plot'
plt.savefig('Formato_RGB_HSV.png')
plt.show()

########################################

# Redimencionamiento de Imagen:
'''
 vamos a utilizar la función de redimensionamiento de skimage.
 La entrada de esta función será la imagen que queremos actualizar y
 las dimensiones requeridas para la nueva imagen:
'''
from skimage.transform import resize
'Importamos la Foto'
model = imread('modelo.jpg')

#Resize image:
'Redimencionamos con los parametros despues de llamar a la variable model'
model_redi = resize(model, (200, 200))

#plot Imagenes:

'Subplot de la foto original'
plt.subplot(121), imshow(model)
'titulo:'
plt.title('Foto Original')

'Foto redimencionada'
plt.subplot(122), imshow(model_redi)
'Titulo'
plt.title('Resized Image')

'Imprimimos y exportamos la imagen'
plt.savefig('Redimencionamiento.png')
plt.show()

######################################

# Detección de bordes:
'Importamos las librerias necesarias'
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Importamos la imagen:
colibri = io.imread('colibri.jpg')

'Convertimos a formato gray'
colibri_g = rgb2gray(colibri)

# Filtros: sobel, roberts, prewitt
'''
Prewitt es un filtro de uso común para detectar el borde de una imagen.
Se divide en operadores horizontales y verticales,
que se utilizan para detectar los bordes verticales y
horizontales respectivamente
(Nota: la forma horizontal del filtro detecta el borde vertical de la imagen,
la forma vertical del filtro Detecta el borde horizontal de la imagen).

El operador de Sobel tiene un filtro practicamente identico al Prewitt con la unica
diferencia que en este filtro se le da un mayor peso al renglon o columna central del filtro

La particularidad de este operador es que,
diferenciándose de los operadores de Sobel y Prewitt,
posee la capacidad de evidenciar puntos de borde pero no así la orientación de éstos.
'''
filtros = [filters.sobel, filters.roberts, filters.prewitt]
filtros_names = ['SOBEL', 'ROBERTS', 'PREWITT']
savefig = ['Filter_sobel.jpg', 'Filter_roberts.jpg', 'Filter_prewitt.jpg']

for filtro,n in zip(filtros, filtros_names):
    # Aplicamos cada uno de los filtros
    col_fil = filtro(colibri_g)
    
    # Mostramos los resultados 
    plt.imshow(col_fil)
    plt.title(n)
    plt.show()

