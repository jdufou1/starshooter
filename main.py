import pygame
import numpy as np
from pygame.locals import *
from model.Model import Model
from view.View import View
from Controls import Controls

"""
TODO : remplacer tout le code en architecture MVC
"""

"""
Initialisation des composants du moteur du jeu
"""
model = Model()
view = View(model)
view.start()
model.start()

controls = Controls(model,view)
controls.start()



"""
Démarrage du jeu
"""

"""
print(model.width,model.height)

ecran = pygame.display.set_mode((model.width,model.height)) #Crée la fenêtre de tracé

image = pygame.image.load("./img/ship.png").convert() # charge une image à partir d'un fichier
image = pygame.transform.scale(image, (model.getShip().width,model.getShip().height))
ecran.blit(image, ((model.width / 2) - model.getShip().width / 2,model.height - model.getShip().height)) #Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)

pygame.display.flip() #L'affichage devient effectif : l'image est rendue visible.



loop = True
while loop: # Boucle d'événements
	for event in pygame.event.get(): #parcours de la liste des événements
		if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
			loop = False

while 1 :
	pass
"""
# pygame.quit()