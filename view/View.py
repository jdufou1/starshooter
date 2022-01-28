# from turtle import width
import pygame
from pygame.locals import *
import threading
import time

"""
TODO : repartir les affichages des composants dans differentes classes : MeteorView,ShipView
"""

class View :
    """
    Classe qui s'occupe de l'affichage du jeu
    """
    width = 1000
    height = 1000

    def __init__(self,model) -> None:
        self.model = model
        pygame.display.init()
        self.main_frame = pygame.display.set_mode((View.width,View.height)) # Création de la fenêtre principale
        self.ship_frame = pygame.image.load("./img/ship.png").convert() # Chargement de l'image du vaisseau du joueur
        width_ship = View.width * model.getShip().get_relative_width(self.model.getWidth())
        height_ship = View.height * model.getShip().get_relative_height(self.model.getHeight())
        self.ship_frame = pygame.transform.scale(self.ship_frame, (width_ship,height_ship)) # Redimensionnement de l'image du vaisseau
        self.thread = ViewThread(self)
        self.current_meteor_frames = []

    def update(self) -> None :
        """
        Mise à jour de la vue
        """
        self.update_component()
        pygame.display.flip() # met à jour l'affichage

    def update_ship(self) -> None :
        """
        Met à jour la position du vaisseau dans la fenetre en fonction des valeurs du modele
        """
        x_ship = View.width * self.model.getShip().get_relative_X(self.model.getWidth())
        y_ship = View.height * self.model.getShip().get_relative_Y(self.model.getHeight())
        rect = self.ship_frame.get_rect()
        rect = rect.move(x_ship , y_ship)
        self.main_frame.blit(self.ship_frame, rect)
    
    def update_meteors(self) -> None:
        # On supprime les anciennes sprites de meteors
        while len(self.current_meteor_frames) > 0 :
            image,(x,y) = self.current_meteor_frames.pop()
            transparent = (0,0,0,0)
            image.fill(transparent)
            self.main_frame.blit(image, (x , y))
        # On ajoute les nouvelles images de meteors
        for meteor in self.model.getMeteors():
            height_meteor = View.height * meteor.get_relative_height(self.model.getHeight())
            width_meteor = View.width * meteor.get_relative_width(self.model.getWidth())
            meteor_frame = pygame.image.load("./img/meteor.png").convert()
            meteor_frame = pygame.transform.scale(meteor_frame, (width_meteor,height_meteor))
            x_meteor = View.width * meteor.get_relative_X(self.model.getWidth())
            y_meteor = View.height * meteor.get_relative_Y(self.model.getHeight())
            self.main_frame.blit(meteor_frame, (x_meteor , y_meteor))
            self.current_meteor_frames.append((meteor_frame, (x_meteor , y_meteor)))


    def update_component(self) -> None :
        """
        Met à jour tout les composants de l'affichage du jeu
        """
        self.update_ship()
        self.update_meteors()

    def start(self) -> None :
        """
        Démarre le thread de mise à jour de la fenetre de jeu
        """
        self.thread.start()

    def stop(self) -> None :
        """
        Stop le thread de mise à jour de la fenetre de jeu
        """
        self.thread.setCondition(False)

class ViewThread(threading.Thread) :
    """
    Classe qui s'occupe de mettre à jour l'affichage du jeu
    """
    speed_view = 0.005 # Mise à jour de l'écran toutes les 0.01 secondes
    condition = True

    def __init__(self,view) -> None:
        threading.Thread.__init__(self)
        self.view = view

    def run(self) -> None :
        while(ViewThread.condition) :
            self.view.update()
            time.sleep(ViewThread.speed_view)

    def setCondition(self,condition) -> None:
        """
        Met à jour la condition d'actualisation de l'affichage
        """
        self.condition = condition