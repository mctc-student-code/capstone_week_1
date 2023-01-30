"""
To run the test without the unittest main method, on terminal run  python3 -m unittest test_area.py

all test function should start their name with word test, any function that doesn't start their name with test are not considered test function
and we can use these as helper functions if required.

if the assertion method is not written in the test function, the test is considered to be passed which could be a source of error
"""
from unittest import TestCase
import area

class TestShapeAreas(TestCase): # required to extend TestCase class
    
    def test_triangle_area(self):
        # A triangle with height 4 and base 5 shold have area 10
        self.assertEqual(10, area.triangle_area(4,5))
    
    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91)) # to avoid the small fractional error - rounding
        
    # Tests if either height or base is zero or both is zero
    def test_triangle_zero_height_base(self):
        self.assertEqual(0, area.triangle_area(0,5))
        self.assertEqual(0, area.triangle_area(5,0))
        self.assertEqual(0, area.triangle_area(0,0))
    
    # Tests for negative height or base or both are negative
    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            area.triangle_area(-9,10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(10,-9)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9,-10)
        
    def test_square_area(self):
        self.assertEqual(20, area.square_area(4,5))

class TestCircleArea(TestCase):
    
    def test_circle_area(self):
        self.assertAlmostEqual(78.5398163, area.circle_area(5))
        
        with self.assertRaises(ValueError):
            area.circle_area(-5)