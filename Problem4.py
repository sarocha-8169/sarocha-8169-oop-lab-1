import math
print('radius \theight \tsurface_area')
for x in range(1, 11):
    radius = x
    height = radius*2
    surface_area = 2*math.pi*radius*(radius+height)
    print(f'{radius:6} {height:7} {surface_area:13.2f}')
