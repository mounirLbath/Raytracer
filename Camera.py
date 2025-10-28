import matplotlib.image as mpimg
import numpy as np
import pygame
from Vect3 import *
from Material import *
from math import *
from Scene import *
from Color import *

def ImageName():
    fin = open("ImageID.txt", "r")
    a = fin.read()
    fin.close()
    fout = open("ImageID.txt", "w")
    fout.write(str(int(a)+1))
    fout.close()
    zeros = '0' * (3 - len(a))
    return 'Image' + zeros + a + '.png'

class Camera:
    '''
    Camera Class - Camera with rendering algorithm:

    Attributes
    ----------
    width : int
        screen width
    height : int
        screen height
    fov : float
        camera's field of view (in degrees)
    coord : Vect3
        the camera's position in the scene
    scene : Scene
        the scene that the camera is rendering
    
    '''

    def __init__(self, width, height, fov, coord, scene):
        self.width = width
        self.height = height
        self.fov = pi * fov / 180
        self.coord = coord
        self.scene = scene
        self.rgbArray = np.zeros((self.height, self.width,3))
    
    # returns the color when origin is at coord and surface gets hit by ray with nbBounce bounces left
    def GetColor(self, ray, coord, nbBounce):
        color = Color(0,0,0)
        
        if nbBounce < 0:
            return color
        
        # Returns array [ray intersection point, sphere it hit, normal] if ray hits something else empty array
        result = self.scene.Intersect(ray, coord)

        # if ray hit something
        if len(result) != 0:
            
            # Calculates interPoint
            interPoint = coord + ray * result[0]

            if(result[1].material.materialType == "specular"):
                color = self.GetColor(ray - result[2] * 2* ray.dot(result[2]), interPoint, nbBounce-1)
            
            
            # Calculates pixel intensity
            intensity = self.PixelIntensity( interPoint, result[1])

            # add the diffuse part to the color
            color += Color(intensity * result[1].material.color.r, intensity * result[1].material.color.g, intensity * result[1].material.color.b)

            
        return color

    # Returns pixel intensity for a certain intersection point and the sphere it hits  
    def PixelIntensity(self, interPoint, sphere):
        
        # Sphere normal
        normal = (interPoint - sphere.coord).normalize()

        # Unit vector, direction = from interPoint to lamp
        lightVect = (self.scene.lightSource.coord - interPoint).normalize()

        # Distance from interPoint to light
        distToLight = (self.scene.lightSource.coord - interPoint).norm()

        # Checks if this point is in shadow
        
        result = self.scene.Intersect( lightVect, interPoint)
        if len(result) != 0:
            t = result[0]
            if distToLight >= t:
                return 0

        # Returns the correct intensity
        return min(max(0, lightVect.dot(normal)) * self.scene.lightSource.intensity / (distToLight ** 2), 1)

    # Renders the image and saves it as a png
    def Render(self):
        for x in range(self.width):
            for y in range(self.height):

                # Calculates the direction Vect3 for the ray
                ray = Vect3(x - self.width/2 + 0.5, y - self.height/2 + 0.5, -self.height/(2*tan(self.fov/2))).normalize()

                # Calculates pixel intensity and plot
                self.Plot(Vect3(x,y,0), self.GetColor(ray, self.coord, 5))


        # Creates image
        mpimg.imsave(ImageName(), self.rgbArray)
        
        # Display the image
        surface = pygame.surfarray.make_surface(np.transpose(self.rgbArray*255, (1, 0, 2)))  
        pygame.init()

        window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Image Viewer")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            window.blit(surface, (0, 0))
            pygame.display.flip()

        pygame.quit()



    # Colors one single pixel with a given color
    def Plot(self, coord, color):
        self.rgbArray[self.height - coord.y - 1][coord.x] = color.ColorArray()