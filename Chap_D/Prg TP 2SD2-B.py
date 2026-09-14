"""
Le programme cidessous permet de :
    - charger l'image jpeg
    - déterminer sa largeur et sa hauteur
    - balayer tous les pixels (balayage en largeur et en hauteur)
    - remplacer les pixels colorés par des pixels gris
    - remplacer les pixels par des pixels noirs ou blacs
"""
from PIL import Image
img=Image.open("Coucher-soleil.jpg")
largeur, hauteur = img.size

for x in range (largeur):
    for y in range (hauteur):
        r,v,b=img.getpixel((x,y))
        """on crée un pixel gris, dont toutes composantes sont égales et sont égales à la moyenne des trois couleurs"""
        gris=(r+v+b)//3
        img.putpixel ((x, y), ( gris , gris , gris ))
img.save("soleil gris.png")

for x in range (largeur):
    for y in range (hauteur):
        r,v,b=img.getpixel((x,y))
        """on crée un pixel noir ou blanc, à partir du pixel gris déjà modifié précédemment"""
        if r<250:
            img.putpixel ((x, y), ( 0 , 0 , 0 ))
        else:
            img.putpixel ((x, y), ( 255 , 255 , 255 ))
img.save("soleil nb.png")
