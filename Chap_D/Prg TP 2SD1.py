"""Ne pas modifier leslignes de commentaires, qui apparaissent envert"""

"""import de la bibliothèque Pillow, qui permet de traiter les images"""
from PIL import Image

"""Chargement de votre image (changer le nom) - l'image doit dans le même dossier que le fichier Python"""
"""Dans la suite, l'image sera nommée img"""
img=Image.open("Coucher-soleil3.jpg")


"""on récupère la largeur et la hauteur de l'image en pixels"""
largeur,hauteur=img.size
print(largeur,hauteur)

"""on redimensionne l'image en divisant chaque longueur par 1 (// désigne le quation dans la division euclidienne)"""
im2=img.resize((largeur//2,hauteur//2))

"""puis on enregistre l'image au format png"""
im2.save("image2.png")

"""même chose en divisant les côtés par 5"""
im3=img.resize((largeur//5,hauteur//5))
im3.save("image3.png")

"""continuez le programme pour obtenir une image de côtés 10 puis 20 fois plus petits"""