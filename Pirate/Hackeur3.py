# -*- coding: utf-8 -*-
#Importation du module random
from random import *

#####################################################################

cle=["-","-","-","-","-","-","-","-","-","-","-"]

############################## NIVEAU 1 ##############################

def cracker1(reponse):
  
  a=reponse+1      
  b=2*reponse-5   
  
  if a==b:                #Si a est égal à b alors c'est gagné
    cle[1]=randint(0,9)   #Calcul du premier chiffre de la clé
    print(True,"\nCle :",cle[1],"- - - - - - - - -")
  else:
    print(False)          #Ce n'est pas la bonne réponse. Essaie encore !

############################## NIVEAU 2 ##############################

def cracker2(reponse):
  
  if cle[1]>=7:
    a=2*cle[1]-7
  else:
    if cle[1]>=5:
      a=3*cle[1]-5
    else :
      a=5*cle[1]                 

  if reponse==a:
    cle[2]=(cle[1]+3)%10  #Le deuxième chiffre de la clé est calculé
    print(True,"\nCle :",cle[1],cle[2],"- - - - - - - -")
  else:
    print(False)          #Ce n'est pas la bonne réponse. Essaie encore !

############################## NIVEAU 3 ##############################

def cracker3(reponse):

  a=reponse
  for i in range(10):    
    a=a-2 
  
  if a==cle[2]:          
    cle[3]=(cle[2]+5)%10  #Le troisième chiffre de la clé est calculé
    print(True,"\nCle :",cle[1],cle[2],cle[3],"- - - - - - -")
  else:
    print(False)

############################## NIVEAU 4 ##############################

def cracker4(reponse):

  a=cle[3]
  for i in range(5):    
    a=a+i
  
  if reponse==a:
    cle[4]=(cle[3]+7)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],"- - - - - -")        
  else:
    print(False)

############################## NIVEAU 5 ##############################

def cracker5(reponse):

  a=reponse
  for i in range(10):    
    a=a-1       
                 
  if a==cle[4]:      
    cle[5]=(3*cle[4]+3)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],"- - - - -")           
  else:
    print(False)

############################## NIVEAU 6 ##############################             

def f(x):
  return -x**2+12*x-6     #f(x)=-x²+12x-6

def cracker6(reponse):
  M=f(0)
  for x in range(10):    
    if f(x)>M:
      M=f(x)
    
  if reponse==M:
    cle[6]=(3*cle[5]+5)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],"- - - -")           
  else:
    print(False)

############################## NIVEAU 7 ##############################

def cracker7(reponse):

  a=cle[6]
  while a<20:     #Tant que a est strictement inférieur à 20 faire ...
    a=a+1      
  
  if reponse==a:
    cle[7]=(3*cle[6]+7)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],"- - -")
  else:
    print(False)

############################## NIVEAU 8 ##############################

def g(x):
  return -0.1*x**2+1.5*x+2     #g(x)=-0.1x²+1.5x+2

def cracker8(reponse):

  x=cle[7]
  while g(x)>0:
    x=x+1      
  
  if reponse==x:
    cle[8]=(7*cle[7]+3)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],cle[8],"- -")
  else:
    print(False)

############################## NIVEAU 9 ##############################

def cracker9(reponse):

  a=cle[8]
  while a<100:
    a=a+10      
  
  if reponse==a:
    cle[9]=(7*cle[8]+5)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],cle[8],cle[9],"-")
  else:
    print(False)

############################## NIVEAU 10 ##############################

def cracker10(reponse):

  S=0
  n=0
  while S<30:
    n=n+1
    S=S+cle[n]        #cle[n] désigne le n-ième chiffre de la clé
    
  if reponse==S:
    cle[10]=(7*cle[9]+7)%10
    print(True,"\nCle :",cle[1],cle[2],cle[3],cle[4],cle[5],cle[6],cle[7],cle[8],cle[9],cle[10])
    print("Demande au professeur la validation !")
  else:
    print(False)
