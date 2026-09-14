from PIL import Image

"""création d'une nouvelle image de largeur 300 pixels et de hauteur 200 pixels"""
drapeauF=Image.new("RGB",(300,200))

"""balayage des pixels d'abscisse inférieure à 100, sur toute la hauteur, pour les colorier en bleu"""
for x in range (100):
    for y in range(200):
        drapeauF.putpixel((x,y),(0,0,255))

"""balayage des pixels d'abscisse entre 100 et 200, sur toute la hauteur, pour les colorier en blanc"""
for x in range (100,200):
    for y in range(200):
        drapeauF.putpixel((x,y),(255,255,255))

"de la même manière, colorier les pixels d'abscisse comprise entre 200 et 300 en rouge"""
        



"""affichage de l'image"""
drapeauF.show()
        
"""enregistrement de l'image - dans le même dossier que le fichier Python"""
drapeauF.save("drapeau français.png")
