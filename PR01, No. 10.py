x1 = float(input('X1: '))   #2
y1 = float(input('Y1: '))   #-4
x2 = float(input('X2: '))   #7
y2 = float(input('Y2: '))   #-2
 
gradient = (y2-y1) / (x2-x1) 
xmid = (x1+x2) / 2
ymid = (y1+y2) / 2
gradient_perpendicular = -1 / gradient

b = ymid - gradient_perpendicular * xmid

print('point 1:(', x1,',', y1,')')
print('point 1:(', x2,',', y2,')')
print(f'y =, {gradient_perpendicular}x + {b}')

