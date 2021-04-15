# Librería scikit image

*(realice al menos dos ejercicios que requieran cargar archivos externos y guardar las respuestas a los ejercicios  en archvos independientes para cada ejercicio)*

#### **Explicación <%matlplotlib inline>:**

* %matplotlib inline establece el backend de matplotlib       al backend 'inline': Con este backend, la salida de los     comandos de trazado se muestra en línea dentro de           frontends como el cuaderno Jupyter, directamente debajo     de la celda de código que lo produjo. Los gráficos          resultantes también se almacenarán en el documento del      cuaderno.

### -> Filtros => sobel, roberts, prewitt:
*Prewitt es un filtro de uso común para detectar el borde de una imagen.*
*Se divide en operadores horizontales y verticales,
que se utilizan para detectar los bordes verticales y
horizontales respectivamente
(Nota: la forma horizontal del filtro detecta el borde vertical de la imagen,
la forma vertical del filtro Detecta el borde horizontal de la imagen).*

*El operador de Sobel tiene un filtro practicamente identico al Prewitt con la unica
diferencia que en este filtro se le da un mayor peso al renglon o columna central del filtro*

*La particularidad de este operador es que,
diferenciándose de los operadores de Sobel y Prewitt,
posee la capacidad de evidenciar puntos de borde pero no así la orientación de éstos.*

## Nota:
Pido disculpas fue un tema muy complicado de entender para mi, hice algunos ejercicos muy sencillos (a mi parecer), pero al ver cuan vasto es *~Scikit-Image~* y especificamente *~Scikit-Learn~*, me quedo corto al ver todas estas funcinalidades.....

pude haber  hecho más pero no los realice por falta de compresión, **solamente entender los filtros fue complicado.**