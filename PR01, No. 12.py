velocity = float(input('velocity: '))   #77.2 m/s^2 = 278*1000/3600 (changing from km/hr to m/s^2)
space =float(input('distance: '))       #94 meters

t = 2*space /velocity
t = round(t, 2)
a = velocity/t 
a = round(a, 2)

print('The time for the fighter to be accelerated: ',t,'seconds')
print('The acceleration of a jet launched from an aircraft catapult: ',a,'m/s^2')