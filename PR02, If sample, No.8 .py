
freeservices = float(input('enter the free service number: ')) #1 or 2
miles = float(input('enter the number of miles: '))

if freeservices == 1:
    if 1500 < miles <= 3000:
        print ('vehicle must be serviced')
    else :
        print ('vehicle does not need to be serviced')
elif freeservices == 2:
    if 3001 < miles <= 4500:
         print ('vehicle must be serviced')
    else : 
        print ('vehicle does not need to be serviced')