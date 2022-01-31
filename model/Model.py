from argparse import Namespace
from xml.dom.expatbuilder import Namespaces


from model.Ship import Ship
from model.Meteor import Meteor
from model.Bullet import Bullet
import numpy as np
import threading
import time

class Model:
    """
    Modèle du jeu / point d'entrée des requêtes à faire sur les éléments du modèle
    """
    height = 1000
    width = 1000

    def __init__(self) -> None:
        self.ship = Ship( (self.width  / 2) - (Ship.width / 2), self.height - Ship.height )
        self.meteors = []
        self.createMeteor()
        self.thread = ModelThread(self)
        self.bullets = []
        self.nbDestroy = 0

    def __str__(self) -> str:
        pass

    def getMeteors(self) : 
        return self.meteors

    def getShip(self) : 
        return self.ship

    def createMeteor(self) -> None :
        self.meteors.append(Meteor(np.random.randint(0,self.width - Meteor.width),0))

    def checkMeteor(self) -> None :
        # self.meteors = [meteor for meteor in self.meteors if meteor.getY() < Model.height and meteor.isAlive()]
        meteors = []
        for meteor in self.meteors :
            contact = False
            for bullet in self.bullets :
                if meteor.isInside(bullet.getX(),bullet.getY()):
                    contact = True
            if not contact and meteor.getY() < Model.height and meteor.isAlive() :
                meteors.append(meteor)
            elif contact:
                self.nbDestroy += 1

        self.meteors = meteors

    def update(self) -> None :
        self.updateMeteors()
        self.updateBullets()
        self.checkMeteor()
        self.checkBullets()
        if len(self.meteors) < 1 :
            self.createMeteor()

    def updateMeteors(self) -> None :
        # Génération aléatoire de meteors
        alea = np.random.randint(400)
        if alea < 5 and len(self.meteors) < 4 :
            self.createMeteor()
        # Application de la gravite sur les meteors
        for meteor in self.meteors :
            meteor.fall()

    def createBullet(self,x,y) -> None:
        """
        Creer une balle dans le modele
        """
        self.bullets.append(Bullet(x,y))

    def checkBullets(self) -> None :
        """
        Trie des balles qui sont toujours dans le monde
        """
        self.bullets = [bullet for bullet in self.bullets if bullet.getY() > 0]

    def updateBullets(self) -> None :
        """
        Mise à jour des balles tirés par le joueur
        """
        for bullet in self.bullets :
            bullet.update()

    def start(self) -> None :
        """
        Lance le thread du modele qui fait evoluer le modele
        """
        self.thread.start()

    def stop(self) -> None :
        """
        Stop le thread de mise à jour du modele
        """
        self.thread.setCondition(False)

    def getShip(self) -> None :
        """
        Retourne le vaisseau
        """
        return self.ship

    def getHeight(self) :
        """
        Retourne la hauteur du modele
        """ 
        return Model.height
    
    def getWidth(self) :
        """
        Retourne la largeur du modele
        """ 
        return Model.width

    def getMeteors(self) :
        """
        Retourne les meteors
        """ 
        return self.meteors

    def getBullets(self) :
        """
        Retourne les balles
        """
        return self.bullets

    def getNbDestroy(self) -> int :
        """
        Retourne le nombre de meteore detruit par le joueur
        """ 
        return self.nbDestroy

    def move_right_ship(self) -> None :
        if self.ship.getX() + Ship.width  + Ship.step < Model.width :
            self.ship.move_right()
    
    def move_left_ship(self) -> None :
        if self.ship.getX() - Ship.step > 0 : 
            self.ship.move_left()

class ModelThread(threading.Thread) :

    speed_model = 0.05
    condition = 1

    def __init__(self,model):
        threading.Thread.__init__(self)
        self.model = model

    def run(self) :
        while(ModelThread.condition) :
            self.model.update()
            time.sleep(ModelThread.speed_model)

    def setCondition(self,condition):
        self.condition = condition

"""
Zone de test

model = Model()
model.createMeteor()
model.start()
"""