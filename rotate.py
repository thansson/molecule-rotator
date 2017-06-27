#!/usr/bin/python3
#-*-encoding:utf8-*-
import numpy as np
from numpy import cos, sin
from random import random
import sys

"""
Molecule rotator
This program rotates given molecule to random direction.
The molecule must be given in correct xyz-format: https://en.wikipedia.org/wiki/XYZ_file_format

Usage: ./rotate.py input.xyz output.xyz
"""

def random_axis():
    """
    Returns random unit vector in R^3.
    """
    theta = np.random.uniform(0,np.pi)
    phi = np.random.uniform(0,2*np.pi)

    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return [x,y,z]

def rotate_vector(vec,axis,theta):
    """
    Rotates given 3D-vector to random direction.
    Takes array of three number as an input vector.
    Returns rotated vector as an array.
    """
    rotmat = [[cos(theta)+ axis[0]**2*(1-cos(theta)), axis[0]*axis[1]*(1-cos(theta))-axis[2]*sin(theta), axis[0]*axis[2]*(1-cos(theta)) + axis[1]*sin(theta)],
    [axis[1]*axis[0]*(1-cos(theta))+axis[2]*sin(theta), cos(theta)+axis[1]**2*(1-cos(theta)), axis[1]*axis[2]*(1-cos(theta))-axis[0]*sin(theta)],
    [axis[2]*axis[0]*(1-cos(theta))-axis[1]*sin(theta), axis[2]*axis[1]*(1-cos(theta))+axis[0]*sin(theta), cos(theta)+axis[2]**2*(1-cos(theta))]]
    return(np.matmul(rotmat,vec))


def rotate_molecule(filename):
    """
    Rotates molecule specified in xyz-file given as argument, to random direction given in format from read_molecule()-function. Needs rotate_vector-function to work.
    Returns rotated molecule in xyz-format.
    """
    with open(filename) as inp:
        xyz = [line.rstrip('\n') for line in open(filename)]
    i = 2
    while(i < len(xyz)):
        xyz[i] = xyz[i].split()
        vec = [float(xyz[i][1]),float(xyz[i][2]),float(xyz[i][3])]
        vec = rotate_vector(vec,axis,theta)
        xyz[i][1] = str(vec[0])
        xyz[i][2] = str(vec[1])
        xyz[i][3] = str(vec[2])
        xyz[i] = '  '.join(xyz[i])
        i=i+1
    return(xyz)

def write_output(out, xyz):
    output = open(out,'w')
    for line in xyz:
        output.write("%s\n" % line)
    return

axis = random_axis() #random axis of rotation
theta = np.random.uniform(0,np.pi*2); #random angle
inp = sys.argv[1]
out = sys.argv[2]
xyz = rotate_molecule(inp)
write_output(out, xyz)
