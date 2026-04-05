from Sphere import *
from Camera import *
from Vect3 import *
from Scene import *
from Light import *

def main():
    scene = Scene(np.array([Sphere(Vect3(0,3,20), 10, Material(Vect3(1,1,1), "diffuse")),
                            # Sphere(Vect3(0,-4,30), 3, Material(Vect3(1,1,1), "diffuse")),
                            # Sphere(Vect3(10,5,25), 3, Material(Vect3(0,0,0), "diffuse")),
                                Sphere(Vect3(0,0,1080), 940, Material(Vect3(1,1,1), "diffuse")), # wall behind camera
                                Sphere(Vect3(0,0,-1000), 940, Material(Vect3(0,0,1), "diffuse")), # back wall
                                Sphere(Vect3(0,1000,0), 940, Material(Vect3(0,1,0), "diffuse")), # ceiling
                                Sphere(Vect3(0,-1400,0), 1393, Material(Vect3(1,0,0), "diffuse")), #ground
                                Sphere(Vect3(-1000,0,0), 940, Material(Vect3(0,0,0) , "diffuse")), #left
                                Sphere(Vect3(1000,0,0), 940, Material(Vect3(0,0,0) , "diffuse")) # right wall
                                ]), Light(Vect3(-10,20,33), 600))

    camera = Camera(500, 500, 60, Vect3(0,3,55), scene)
    camera.Render()

if __name__ == "__main__":
    main()
