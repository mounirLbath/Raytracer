from Sphere import *
from Camera import *
from Vect3 import *
from Scene import *
from Light import *
from Color import *

def main():
    scene = Scene(np.array([Sphere(Vect3(0,0,10), 10, Material(Color(0,0,0), "specular")),
                            Sphere(Vect3(0,-4,30), 3, Material(Color(255,255,255), "diffuse")),
                            Sphere(Vect3(10,5,25), 3, Material(Color(0,0,0), "specular")),
                                Sphere(Vect3(0,0,1080), 940, Material(Color(255,255,255), "diffuse")), # wall behind camera
                                Sphere(Vect3(0,0,-1000), 940, Material(Color(255,255,255), "diffuse")), # back wall
                                Sphere(Vect3(0,1000,0), 940, Material(Color(0,255,0), "diffuse")), # ceiling
                                Sphere(Vect3(0,-1400,0), 1393, Material(Color(255,0,0), "diffuse")), #ground
                                Sphere(Vect3(-1000,0,0), 940, Material(Color(255,255,255), "diffuse")), #left
                                Sphere(Vect3(1000,0,0), 940, Material(Color(255,255,255), "diffuse")) # right wall
                                ]), Light(Vect3(-10,20,33), 1250000))

    camera = Camera(200, 200, 60, Vect3(0,3,55), scene)
    camera.Render()

main()
