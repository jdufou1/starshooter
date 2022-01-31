class Bullet :

    width = 10
    height = 10
    speed = 20

    def __init__(self,x,y) -> None:
        self.y = y
        self.x = x
    
    def getX(self) -> int :
        return self.x

    def getY(self) -> int :
        return self.y

    def update(self) -> None :
        self.y -= Bullet.speed

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
        return Bullet.height / max_height

    def get_relative_width(self,max_width) -> float:
        """
        Retourne la largeur relative du vaisseau par rapport à la hauteur du modèle
        """
        return Bullet.width / max_width

