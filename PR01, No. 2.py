height  = float(input('height of the dam: ')) #170 meters
flow    = float(input('flow: ')) #1300 is from 1.30*10^3

mass    = 1000*flow
gravity = 9.8

w   = mass*gravity*height
w = round(w, 0)
Mw  = w / 10**6     #convert watt to megawatt
e   = Mw*0.9        #electrical energy 
e = round(e, 2)

print('Total watts of the dam: ', w, 'w')
print('Total electrical energy after converted: ', e)