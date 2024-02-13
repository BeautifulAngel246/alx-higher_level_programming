#!/usr/bin/python3
""" 6-main """
import sys
sys.path.append("/alx-higher_level_programming/0x0C-python-almost_a_circle")
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
