import unittest
import random
from roman_calculator import *


class RomanCalcultor(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(RomanCalcultor, self).__init__(*args, **kwargs)
        self.possibles = [{},[],(), "", unittest, 0]

    def test_to_int_to_roman_general(self):
        for i in range(1,1000):
            self.assertEqual(i, to_int(to_roman(i)))
                
    def test_to_rom(self):
        for i in self.possibles:
            self.assertRaises((TypeError,ValueError), to_roman, i)   
    
    def test_to_int(self):
        for i in self.possibles:
            self.assertRaises((TypeError,ValueError), to_int, i) 

    def test_roman_calculations_sum(self):
        sample = []
        for i in range(20):
            sample.append(random.sample(range(100),2))            
        for t in sample:
            if t[0] and t[1]:
                self.assertEqual(to_roman(sum(t)), roman_calculator(to_roman(t[0]),to_roman(t[1]),"+"))
         
            
    def test_roman_calculations_subtract(self):
        sample = []
        for i in range(20):
            sample.append(random.sample(range(100),2))
        for t in sample:
            if  (t[0] and t[1]) and (t[0] > t[1]):    
                self.assertEqual(to_roman(int(t[0]-t[1])), roman_calculator(to_roman(t[0]),to_roman(t[1]),"-"))
           
    def test_roman_calculations_mul(self):
        sample = []
        for i in range(20):
            sample.append(random.sample(range(100),2))
        for t in sample:
            if t[0] and t[1]:
                self.assertEqual(to_roman(t[0]*t[1]), roman_calculator(to_roman(t[0]),to_roman(t[1]),"*"))
            
    def test_roman_calculations_division(self):
        sample = []
        for i in range(20):
            sample.append(random.sample(range(100),2))
        for t in sample:
            if  (t[0] and t[1]) and (t[0] > t[1]):
                self.assertEqual(to_roman(t[0]/t[1]), roman_calculator(to_roman(t[0]),to_roman(t[1]),"/"))                
            
