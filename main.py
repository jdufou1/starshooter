import pygame
import numpy as np
from pygame.locals import *
from model.Model import Model
from view.View import View
from Controls import Controls

"""
Initialisation des composants du moteur du jeu
"""
model = Model()
view = View(model)
view.start()
model.start()
controls = Controls(model,view)
controls.start()