import cv2
from PIL import Image
import numpy as np
import keyboard

# Fonction pour convertir une image en ASCII art
def convert_to_ascii(image, width=100):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aspect_ratio = image.shape[1] / image.shape[0]
    new_height = int(width / aspect_ratio)
    resized_image = cv2.resize(image, (width, new_height))
    ascii_chars = "@%#*+=-:. "
    ascii_image = ""
    
    for row in resized_image:
        for pixel_value in row:
            index = int(pixel_value / 255 * (len(ascii_chars) - 1))
            ascii_image += ascii_chars[index]
        ascii_image += "\n"
    
    return ascii_image

# Capture de la vidéo en direct depuis la caméra avec une résolution personnalisée
cap = cv2.VideoCapture(0)

# Spécifiez la résolution souhaitée (par exemple, 1920x1080)
cap.set(3, 1920)  # 3 correspond à la largeur
cap.set(4, 1080)  # 4 correspond à la hauteur

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convertir la frame en ASCII art
    ascii_art = convert_to_ascii(frame)
    
    # Afficher l'ASCII art
    print(ascii_art)
    
    # Arrêtez la boucle en appuyant sur la touche 'q'
    if keyboard.is_pressed('q'):
        break

# Libérer la capture de la caméra
cap.release()
cv2.destroyAllWindows()
