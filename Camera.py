import matplotlib.image as mpimg
import numpy as np
import pygame
from multiprocessing import Pool, cpu_count
from Vect3 import *
from Material import *
from math import *
from Scene import *

workerScene = None


def initWorkerScene(scene):
    global workerScene
    workerScene = scene


def traceColor(scene, ray, coord, nbBounce):
    eps = 1e-4
    if nbBounce <= 0:
        return Vect3(0, 0, 0)

    result = scene.Intersect(ray, coord)

    if len(result) != 0:
        interPoint = coord + ray * result[0]
        normal = result[2]
        newOrigin = interPoint + normal * eps
        sphere = result[1]

        if sphere.material.materialType == "specular":
            return traceColor(scene, ray - normal * 2 * ray.dot(normal), newOrigin, nbBounce - 1)
        elif sphere.material.materialType == "diffuse":
            lightVect = (scene.lightSource.coord - newOrigin).normalize()
            distToLight = (scene.lightSource.coord - newOrigin).norm()
            inShadow = scene.Intersect(lightVect, newOrigin)
            intensity = 0
            if len(inShadow) == 0 or distToLight < inShadow[0]:
                intensity = max(0, lightVect.dot(normal)) * scene.lightSource.intensity / (distToLight ** 2)

            color = intensity * sphere.material.albedo

            a = np.random.random()
            b = np.random.random()
            dirLocal = Vect3(np.cos(2 * np.pi * a) * np.sqrt(1 - b), np.sin(2 * np.pi * a) * np.sqrt(1 - b), np.sqrt(b))

            randomVect = Vect3(np.random.random() - 0.5, np.random.random() - 0.5, np.random.random() - 0.5)
            tangent = normal.cross(randomVect).normalize()
            tangent2 = normal.cross(tangent)
            dir = dirLocal.x * tangent + dirLocal.y * tangent2 + dirLocal.z * normal

            color += traceColor(scene, dir, newOrigin, nbBounce - 1) * sphere.material.albedo
            return color

    return Vect3(0, 0, 0)


def sampleRay(args):
    ray, coord, nb = args
    return traceColor(workerScene, ray, coord, nb)


def ImageName():
    try:
        fin = open("./renders/ImageID.txt", "r")
        a = fin.read()
        if a== "":
            a = "0"
        fin.close()
        fout = open("./renders/ImageID.txt", "w")
        fout.write(str(int(a)+1))
        fout.close()
        zeros = '0' * (3 - len(a))
        return './renders/Image' + zeros + a + '.png'
    except:
        return 'Image.png'

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
        return traceColor(self.scene, ray, coord, nbBounce)


        
    # Renders the image and saves it as a png
    def Render(self):
        N = 10
        with Pool(processes=min(N, cpu_count() or 1), initializer=initWorkerScene, initargs=(self.scene,)) as pool:
            for x in range(self.width):
                print(((x)) / (self.width))
                for y in range(self.height):
                    ray = Vect3(x - self.width / 2 + 0.5, y - self.height / 2 + 0.5, -self.height / (2 * tan(self.fov / 2))).normalize()
                    samples = pool.map(sampleRay, [(ray, self.coord, 5)] * N)
                    result = Vect3(0, 0, 0)
                    for s in samples:
                        result += s
                    result = result * (1.0 / N)
                    result.gammaCorrection()
                    self.Plot(Vect3(x, y, 0), result)


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