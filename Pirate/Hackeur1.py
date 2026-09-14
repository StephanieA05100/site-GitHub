# -*- coding: utf-8 -*-
#Importation du module random
from random import *

#####################################################################

cle=["-","-","-","-","-","-","-","-","-","-","-"]

############################## NIVEAU 1 ##############################

def cracker1(reponse):
  
  a=15         
  b=2*a-5   
  
  if reponse==b:          #Si ta réponse est égale à b alors c'est gagné
    cle[1]=randint(0,9)   #Calcul du premier chiffre de la clé
    print(True,"\nCle :",cle[1],"- - - - - - - - -")
  else:
    print(False)          #Ce n'est pas la bonne réponse. Essaie encore !

############################## NIVEAU 2 ##############################

def cracker2(reponse):
  
  a=cle[1]             #a est égal au premier chiffre de la clé trouvé précédemment         
  b=a**2+1             #b est égal à a^2+1 (a au carré plus 1)         

  if reponse==b:
    cle[2]=(cle[1]+3)%10  #Le deuxième chiffre de la clé est calculé
    print(True,"\nCle :",cle[1],cle[2],"- - - - - - - -")
  else:
    print(False)          #Ce n'est pas la bonne réponse. Essaie encore !

############################## NIVEAU 3 ##############################

def cracker3(reponse):

  a=cle[2]     #a est égal 2ieme chiffre de la clé         
  a=2*a
  a=a+1

  if reponse==a:          
    cle[3]=(cle[2]+5)%10  #Le troisième chiffre de la clé est calculé
    print(True,"\nCle :",cle[1],cle[2],cle[3],"- - - - - - -")
  else:
    print(False)

############################## NIVEAU 4 ##############################

def cracker4(reponse):
                       
  a=cle[1]               #a est égal au premier chiffre de la clé                 
  a=a+cle[2]
  a=a+cle[3]
  
  if reponse==a:
    cle[4]=(cle[3]+7)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],"- - - - - -")        
  else:
    print(False)

############################## NIVEAU 5 ##############################

def cracker5(reponse):

  a=0
  if cle[1]<cle[2]:
    a=a+1
  if cle[3]<cle[4]:
    a=a+1
  if cle[1]<=5 and cle[2]<=5:
    a=a+1
  if cle[3]<=5 or cle[4]<=5:
    a=a+1
        
  if reponse==a:      
    cle[5]=(3*cle[4]+3)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],"- - - - -")           
  else:
    print(False)

############################## NIVEAU 6 ##############################

def cracker6(reponse):

  if cle[5]>5:    
    a=reponse-5
  else:
    a=2*reponse+3
                 
  if a==17:
    cle[6]=(3*cle[5]+5)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],"- - - -")           
  else:
    print(False)

############################## NIVEAU 7 ##############################

def cracker7(reponse):

  a=cle[6]
  for i in range(10):    
    a=a+1              
    
  if reponse==a:
    cle[7]=(3*cle[6]+7)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],"- - -")
  else:
    print(False)

############################## NIVEAU 8 ##############################

def cracker8(reponse):

  a=cle[7]
  for i in range(5):
    a=2*a           
    
  if reponse==a:
    cle[8]=(7*cle[7]+3)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],cle[8],"- -")
  else:
    print(False)

############################## NIVEAU 9 ##############################

def cracker9(reponse):

  a=reponse
  for i in range(5):  
    a=a-1            
  
  if a==cle[8]:
    cle[9]=(7*cle[8]+5)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],cle[8],cle[9],"-")
  else:
    print(False)

############################## NIVEAU 10 ##############################

def cracker10(reponse):

  S=0  
  for i in range(1,10):     #Pour i allant de 1 à 9
    S=S+cle[i]              #cle[i] désigne le ième chiffre de la clé
    
  if reponse==S:
    cle[10]=(7*cle[9]+7)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],cle[8],cle[9],cle[10])
    print("Demande au professeur la validation !")
  else:
    print(False)
    
  
