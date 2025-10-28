# Raytracer

A **raytracer built from scratch** in Python.  
It renders simple 3D scenes with **diffuse** and **specular** materials.

## Overview

The project implements a minimal raytracing engine that supports:
- Ray–sphere intersection  
- Diffuse and specular reflections  
- Adjustable camera (resolution and field of view)

Learned and inspired by [this course](https://perso.liris.cnrs.fr/nicolas.bonneel/ENS.html).

## Example Renders

| Specular Example | Animation Example |
|------------------|-------------------|
| <img src="/assets/SpecularDemo.png" width="300"> | <img src="/assets/BallAnimation.gif" width="300"> |

## Usage

1. Define your scene in [`main.py`](https://github.com/devmlGit/Raytracer/blob/6575699a04a688d8eb9c28f1f75fd2b8310e60ec/main.py).  
2. Change resolution or field of view in [this line](https://github.com/mounirLbath/Raytracer/blob/4b6c15a6a2ba42777b7e7b7bd8469a022fc8e68d/main.py#L20C4-L20C56).  
3. To perform multiple renders, create a `/renders/` directory and add an `ImageID.txt` file inside.  
4. Run the renderer:

```bash
python main.py

```bash
python main.py
