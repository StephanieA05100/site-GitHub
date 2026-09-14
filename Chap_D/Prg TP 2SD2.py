"""
Le programme cidessous permet de :
    - charger l'image jpeg
    - déterminer sa largeur et sa hauteur
    - balayer tous les pixels (balayage en largeur et en hauteur)
    - remplacer les pixels dont la composante bleue est supérieure à 200 par un pixel entièreent bleu (0,0,255)
    - enregistrer l'image modifiée sous un nouveau nom
"""
from PIL import Image
img=Image.open("Coucher-soleil.jpg")
largeur, hauteur = img.size
"""pixels = img.load()"""
for x in range (largeur):
    for y in range (hauteur):
        r,v,b=img.getpixel((x,y))
        if b>200:
            img.putpixel ((x, y), ( 0 , 0 , 255 ))
img.save("soleil modifié.png")
img.show()
