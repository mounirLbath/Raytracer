class Material:
    '''
    Material Class - Represents the light ray:
    
    Attributes
    ----------
    albedo : albedo
        the material's albedo
        
    '''

    def __init__(self, albedo, materialType):
        self.albedo = albedo
        self.materialType = materialType