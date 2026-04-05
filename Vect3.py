from math import sqrt

class Vect3:
    '''
    Vect3 Class - 3D Vector with basic operations:
    
    Attributes
    ----------
    x : float
        the x coordinate
    y : float
        the y coordinate
    z : float
        the z coordinate
        
    '''
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Affichage du vecteur
    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)
    
    # Addition d'un autre vecteur
    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        c = self.z + other.z
        return Vect3(a, b, c)

    # Soustraction d'un autre vecteur
    def __sub__(self, other):
        a = self.x - other.x
        b = self.y - other.y
        c = self.z - other.z
        return Vect3(a, b, c)

    # Multiplication par un scalaire
    def __mul__(self, other):
        if isinstance(other, Vect3):
            return Vect3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )
        return Vect3(
            self.x * other,
            self.y * other,
            self.z * other
        )

    def __rmul__(self, other):
        return self * other

    # Division par un scalaire
    def __truediv__(self, other):
        a = self.x / other
        b = self.y / other
        c = self.z / other
        return Vect3(a, b, c)
    
    # Vecteur opposé
    def __neg__(self):
        a = -self.x
        b = -self.y
        c = -self.z
        return Vect3(a, b, c)

    # Produit scalaire
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    # Produit vectoriel
    def cross(self, other):
        a = self.y * other.z - self.z * other.y
        b = self.z * other.x - self.x * other.z
        c = self.x * other.y - self.y * other.x
        return Vect3(a, b, c)

    # Norme du vecteur
    def norm(self):
        return sqrt(self.x ** 2 + self.y **2 + self.z **2)

    # Normalisation
    def normalize(self):
        return self / self.norm()

    # Norme au carré
    def normSquare(self):
        return self.norm() ** 2
    
    def ColorArray(self):
        return [min(1,max(0,self.x)), min(1,max(0,self.y)), min(1,max(0,self.z))]
    
    def gammaCorrection(self):
        e = 1.0/2.2
        self.x = self.x ** e
        self.y = self.y ** e
        self.z = self.z ** e
