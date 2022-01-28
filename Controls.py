
import pygame
from pygame.locals import *
import threading
import time

class Controls :

    def __init__(self,model,view) -> None:
        self.model = model
        self.view = view
        self.thread = ThreadControls(self)

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

    def getModel(self) :
        return self.model

    def getView(self) :
        return self.view
    

class ThreadControls(threading.Thread):
    """
    Classe qui s'occupe de mettre à jour l'affichage du jeu
    """
    speed_controls = 0.01 # Verification des controles
    condition = True

    def __init__(self,controls) -> None:
        threading.Thread.__init__(self)
        self.controls = controls

    def run(self) -> None :
        while(ThreadControls.condition) :
            # verification de l'activation des controles : 
            for event in pygame.event.get() :
                print("gkjhg")
                if event.type == K_RIGHT:
                    self.controls.getModel().getShip().move_right(5)
                if event.type == K_LEFT:
                    self.controls.getModel().getShip().move_left(5)
            time.sleep(ThreadControls.speed_controls)
            """
            for event in pygame.event.get() :
                if event.type == K_RIGHT:
			        self.controls.getModel.getShip().move_right(5)
                if event.type == K_LEFT:
			        self.controls.getModel.getShip().move_left(5)
            time.sleep(ThreadControls.speed_controls)
            """

    def setCondition(self,condition) -> None:
        """
        Met à jour la condition d'actualisation de l'affichage
        """
        self.condition = condition