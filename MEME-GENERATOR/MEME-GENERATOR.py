from PIL import Image, ImageDraw, ImageFont
import textwrap

# Abrir la imagen base.
imagen_base = Image.open("lisa-blackpink-1.jpg")

# Crear un objeto ImageDraw para dibujar en la imagen.
draw = ImageDraw.Draw(imagen_base) 

ancho_lienzo = 1280  # Ajustar el ancho del lienzo según tus preferencias.
alto_lienzo = 720  # Ajustar el alto del lienzo según tus preferencias.

# Definir la fuente y el tamaño del texto.
fuente = ImageFont.truetype("arial.ttf", size = 82)  # Cambia la fuente y el tamaño según tus preferencias.
color_texto = "white"  # Puedes cambiar el color del texto si lo deseas.
color_sombra = "black"  # Cambia el color de la sombra si lo deseas.

# Agregar texto superior.
texto_superior = "ESE WEY PIENSA QUE"
posicion_superior = (26, 10)  # Cambia la posición según tus preferencias. 

# Dibujar la sombra del texto superior.
draw.text((posicion_superior[0] + 1, posicion_superior[1] + 1), texto_superior, fill = color_sombra, font = fuente)

# Dibujar el texto superior.
draw.text(posicion_superior, texto_superior, fill = color_texto, font = fuente)

# Agrega nuevo texto inferior
texto_inferior = "ES UN PROGRAMADOR."
posicion_inferior = (16, imagen_base.height - 100)  # Cambia la posición según tus preferencias. 
tamaño_fuente_inferior = 45  # Cambia el tamaño de la fuente según tus preferencias. 

# Dibuja la sombra del nuevo texto inferior
draw.text((posicion_inferior[0] + 1, posicion_inferior[1] + 1), texto_inferior, fill = color_sombra, font = fuente)

# Dibuja el nuevo texto inferior
draw.text(posicion_inferior, texto_inferior, fill = color_texto, font = fuente)

# Guardar el meme resultante.
imagen_base.save("meme_generated.jpg")
