"""
Functions for computing areas of various shapes
"""
import math

def triangle_area(height, base):
    if base < 0 or height < 0:
        raise ValueError('Base and height must be 0 or positive')
    return height * base * 0.5

def square_area(height, base):
    return height * base

def circle_area(radius):
    if radius < 0:
        raise ValueError
    return radius ** 2 * math.pi