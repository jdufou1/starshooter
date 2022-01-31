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
    width = 800
    height = 800

    def __init__(self,model) -> None:
        self.model = model
        pygame.display.init()
        self.main_frame = pygame.display.set_mode((View.width,View.height)) # Création de la fenêtre principale
        x_ship = View.width * self.model.getShip().get_relative_X(self.model.getWidth())
        y_ship = View.height * self.model.getShip().get_relative_Y(self.model.getHeight())
        image = pygame.image.load("./img/ship.png").convert() # Chargement de l'image du vaisseau du joueur
        width_ship = View.width * model.getShip().get_relative_width(self.model.getWidth())
        height_ship = View.height * model.getShip().get_relative_height(self.model.getHeight())
        self.current_ship_frame = pygame.transform.scale(image, (width_ship,height_ship)),(x_ship,y_ship) # Redimensionnement de l'image du vaisseau
        self.thread = ViewThread(self)
        self.current_meteor_frames = []
        self.current_bullets_frames = []
        """
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = "Vous avez detruit "+str(self.model.getNbDestroy()) + " meteores"
        self.text_field = font.render(text, True, (255, 255, 255))
        textRect = self.text_field.get_rect()
        self.main_frame.blit(self.text_field, textRect)
        """

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
        image,(x,y) = self.current_ship_frame
        transparent = (0,0,0,0)
        image.fill(transparent)
        self.main_frame.blit(image, (x , y))

        frame = pygame.image.load("./img/ship.png").convert()
        width_ship = View.width * self.model.getShip().get_relative_width(self.model.getWidth())
        height_ship = View.height * self.model.getShip().get_relative_height(self.model.getHeight())
        x_ship = View.width * self.model.getShip().get_relative_X(self.model.getWidth())
        y_ship = View.height * self.model.getShip().get_relative_Y(self.model.getHeight())
        self.current_ship_frame = pygame.transform.scale(frame, (width_ship,height_ship)),(x_ship,y_ship) # Redimensionnement de l'image du vaisseau
        self.main_frame.blit(self.current_ship_frame[0],self.current_ship_frame[1])
    
    def update_meteors(self) -> None:
        """
        Met à jour la position des meteors dans la fenetre en fonction des valeurs du modele
        """
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


    def update_bullets(self) -> None :
        """
        Met à jour la position des balles dans la fenetre en fonction des valeurs du modele
        """
        # On supprime les anciennes sprites de meteors
        while len(self.current_bullets_frames) > 0 :
            image,(x,y) = self.current_bullets_frames.pop()
            transparent = (0,0,0,0)
            image.fill(transparent)
            self.main_frame.blit(image, (x , y))
        # On ajoute les nouvelles images de meteors
        for bullet in self.model.getBullets():
            height_bullet = View.height * bullet.get_relative_height(self.model.getHeight())
            width_bullet = View.width * bullet.get_relative_width(self.model.getWidth())
            bullet_frame = pygame.image.load("./img/meteor.png").convert()
            bullet_frame = pygame.transform.scale(bullet_frame, (width_bullet,height_bullet))
            x_bullet = View.width * bullet.get_relative_X(self.model.getWidth())
            y_bullet = View.height * bullet.get_relative_Y(self.model.getHeight())
            self.main_frame.blit(bullet_frame, (x_bullet , y_bullet))
            self.current_bullets_frames.append((bullet_frame, (x_bullet , y_bullet)))

    def updateHUD(self) -> None :
        transparent = (0,0,0,0)
        self.text_field.fill(transparent)
        self.main_frame.blit(self.text_field, (0 , 0))

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = "Vous avez detruit "+str(self.model.getNbDestroy()) + " meteores"
        self.text_field = font.render(text, True, (255, 255, 255))
        textRect = self.text_field.get_rect()
        self.main_frame.blit(self.text_field, textRect)


    def update_component(self) -> None :
        """
        Met à jour tout les composants de l'affichage du jeu
        """
        self.update_ship()
        self.update_meteors()
        self.update_bullets()
        #self.updateHUD()

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
    speed_view = 0.01 # Mise à jour de l'écran toutes les 0.01 secondes
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

    def getCondition(self) -> bool: 
        return self.condition