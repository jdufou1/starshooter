class Ship :
    """Cette classe permet la creation du vaisseau (ship)"""
    height = 100 # taille 
    width = 100 # largeur 
    step = 5

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def getX(self) -> int :
        return self.x

    def getY(self) -> int :
        return self.y

    def getHeight(self) -> int :
        return Ship.height

    def getWidth(self) -> int :
        return Ship.width

    def move_right(self) -> None :
        self.x += Ship.step
        
    def move_left(self) -> None :
        self.x -= Ship.step

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
        return Ship.height / max_height

    def get_relative_width(self,max_width) -> float:
        """
        Retourne la largeur relative du vaisseau par rapport à la hauteur du modèle
        """
        return Ship.width / max_width