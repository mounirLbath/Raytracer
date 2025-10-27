from Sphere import *
from Camera import *
from Vect3 import *
from Scene import *
from Light import *
from Color import *

def main():
    scene = Scene(np.array([Sphere(Vect3(0,0,10), 10, Material(Color(0,0,0), "specular")),
                            Sphere(Vect3(3,0,35), 1, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(0,0,1080), 940, Material(Color(0,0,255), "diffuse")),
                                Sphere(Vect3(0,0,-1000), 940, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(0,1000,0), 940, Material(Color(0,255,0), "diffuse")),
                                Sphere(Vect3(0,-1400,0), 1393, Material(Color(255,0,0), "diffuse")),
                                Sphere(Vect3(-1000,0,0), 940, Material(Color(255,255,255), "diffuse")),
                                Sphere(Vect3(1000,0,0), 940, Material(Color(255,255,255), "diffuse"))]), Light(Vect3(-10,20,33), 1250))

    camera = Camera(150, 150, 60, Vect3(0,3,55), scene)
    camera.Render()

main()
