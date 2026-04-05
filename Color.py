class Color:
    '''
    Color Class - Represents the light ray:
    
    Attributes
    ----------
    r : float in [0, 255] 
        the color's red amount
    g : float in [0, 255] 
        the color's green amount
    b : float in [0, 255] 
        the color's blue amount
        
    '''

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def ColorArray(self):
        return [min(255,max(0,self.r))/255, min(255,max(0,self.g))/255, min(255,max(0,self.b))/255]
    
    # Addition d'un autre vecteur
    def __add__(self, other):
        a = self.r + other.r
        b = self.g + other.g
        c = self.b + other.b
        return Color(a, b, c)
    
    def gammaCorrection(self):
        e = 1.0/2.2
        self.r = self.r ** e
        self.g = self.g ** e
        self.b = self.b ** e