from PIL import Image

"""création d'une nouvelle image de largeur 200 pixels et de hauteur 200 pixels"""
im=Image.new("RGB",(100,100))

"""on colorie tous les pixels en vert pour le fond"""
for x in range (100):
    for y in range(100):
        im.putpixel((x,y),(173,255,47))

"""A cet endroit, chacun copiera son programme"""

"""enregistrement de l'image"""
im.save("tableau.png")
