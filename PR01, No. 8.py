lowflush = (input('Lowflush model: '))      #2
people =int(input('people: '))              #up to you
avg_liter = (input('liters per flush: '))   #15 liters/flush
times_per_day = (input('average times: '))  #14 times/day
cost = (input('cost: '))                    #$150

toilet =  people//3     #amount of toilets

old = toilet*15*14      #old toilet magnitude
new = toilet*2*14       #new toilet magnitude

economical_cost = toilet*150

print('Estimated magnitude', new,'liters/day','and the most economical cost' , economical_cost,'dollars' )