import sys
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
        self.right = False # Permet de rester appuyer sur droit
        self.left = False # Permet de rester appuyer sur gauche

    def run(self) -> None :
        while(ThreadControls.condition) :

            if self.right : 
                self.controls.getModel().move_right_ship()
            if self.left :
                self.controls.getModel().move_left_ship()
                

            # verification de l'activation des controles : 
            for event in pygame.event.get() :
                # Action à activer lorsque le joueur presse une touche
                if event.type == pygame.QUIT:
                        # On arrete les threads du model et de la view
                        self.controls.getModel().stop()
                        self.controls.getView().stop()
                        self.condition = False
                        # On arrete la librairie graphique et on arete le programme
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.right = True
                    if event.key == pygame.K_LEFT:
                        self.left = True
                    if event.key == pygame.K_SPACE:
                        x_bullet = self.controls.getModel().getShip().getX() + int((self.controls.getModel().getShip().getWidth() / 2))
                        y_bullet = self.controls.getModel().getShip().getY() - self.controls.getModel().getShip().getHeight()
                        self.controls.getModel().createBullet(x_bullet,y_bullet)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.right = False
                    if event.key == pygame.K_LEFT:
                        self.left = False
            time.sleep(ThreadControls.speed_controls)




    def setCondition(self,condition) -> None:
        """
        Met à jour la condition d'actualisation de l'affichage
        """
        self.condition = condition