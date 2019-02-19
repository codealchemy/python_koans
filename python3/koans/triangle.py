#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
# Helpful snippet to drop into interactive session (like Ruby's binding.pry)
# import code; code.interact(local=dict(globals(), **locals()))
# from https://gist.github.com/obfusk/208597ccc64bf9b436ed
#
def triangle(a, b, c):
    validate_triangle_sides(a, b, c)
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def validate_triangle_sides(*args):
    ordered = sorted(args)
    if ordered[0] + ordered[1] < ordered[2]:
        raise TriangleError("Sum of two sides should be greater than the third")

    if ordered[0] <= 0 or ordered[1] <= 0 or ordered[2] <= 0:
        raise TriangleError("All sides must be greater than 0")

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
