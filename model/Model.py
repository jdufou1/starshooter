from argparse import Namespace
from xml.dom.expatbuilder import Namespaces


from model.Ship import Ship
from model.Meteor import Meteor
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

    def __str__(self) -> str:
        pass

    def getMeteors(self) : 
        return self.meteors

    def createMeteor(self) -> None :
        self.meteors.append(Meteor(np.random.randint(0,self.width - Meteor.width),0))

    def checkMeteor(self) -> None :
        self.meteors = [meteor for meteor in self.meteors if meteor.getY() < Model.height and meteor.isAlive()]
    
    def update(self) -> None :
        self.updateMeteors()
        self.checkMeteor()
        if len(self.meteors) < 1 :
            self.createMeteor()

    def updateMeteors(self) -> None :
        for meteor in self.meteors :
            meteor.fall()

    def start(self) -> None :
        """
        Lance le thread du modele qui fait evoluer le modele
        """
        self.thread.start()

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

class ModelThread(threading.Thread) :

    speed_model = 0.01
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