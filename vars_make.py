
"""
# Author: Ayla Laone
# Date: 02-27-2026
# Description: Variables Make
"""

#Input

circle_radius = 'int(input("The radius of the circle:"))'
rect_length = 'int(input("The length of the rectangle:"))'
rect_width = 'int(input("The width of the rectangle:"))'
octa_side = 'int(input("A side length of the octagon:"))'


#Processing

import math

circle_area = math.pi * circle_radius ** 2
circle_perimeter = 2 * math.pi * circle_radius


rect_area = rect_length * rect_width
rect_perimeter = (rect_length + rect_width) * 2


octa_area = 2 * (1 + math.sqrt(2)) * octa_side ** 2
octa_perimeter = octa_side * 8


#Output

print(f"The circle has an area of {circle_area} and a perimeter of {circle_perimeter}")
print(f"The rectangle has an area of {rect_area} and a perimeter of {rect_perimeter}")
print(f"The octagon has an area of {octa_area} and a perimeter of {octa_perimeter}")