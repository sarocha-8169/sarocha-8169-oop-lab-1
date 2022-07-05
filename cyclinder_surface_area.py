import math
radius = float(input('Enter radius :'))
if radius < 0 :
    print('Please enter a positive number for radius')

height = float(input('Enter height :'))
if height < 0 :
    print('Please enter a positive number for height')
    
Surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
print(f'The surface area of a cylinder with radius {radius} and height {height} is {Surface_area}')