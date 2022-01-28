class Meteor:
    """Cette classe permet la creations des meteorites"""
    width = 50
    height = 50

    fall_value = 5
    max_pv = 100

    def __init__(self,x,y) -> None:
        self.y = y
        self.x = x
        self.pv = Meteor.max_pv

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"
        
    def getX(self) -> int :
        return self.x

    def getY(self) -> int :
        return self.y

    def getPV(self) -> int :
        return self.pv

    def setPV(self,pv) -> None :
        self.pv = pv

    def isAlive(self) -> bool :
        return self.pv > 0

    def fall(self) -> None :
        self.y += Meteor.fall_value

    def move_right(self,step) -> None :
        self.x += step
        
    def move_left(self,step) -> None :
        self.x += step

    def get_relative_Y(self,max_height) -> float:
        """
        Retourne la valeur y relative du vaisseau par rapport à la hauteur du modèle
        """
        return self.y / max_height

    def get_relative_X(self,max_width) -> float:
        """
        Retourne la valeur x relative du vaisseau par rapport à la hauteur du modèle
        """
        return self.x / max_width

    def get_relative_height(self,max_height) -> float:
        """
        Retourne la hauteur relative du vaisseau par rapport à la hauteur du modèle
        """
        return Meteor.height / max_height

    def get_relative_width(self,max_width) -> float:
        """
        Retourne la largeur relative du vaisseau par rapport à la hauteur du modèle
        """
        return Meteor.width / max_width