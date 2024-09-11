grade = input('desired grade: ')                    #B
current = float(input('current score: '))           #74.6
minimum = float(input( 'minimum score: '))          #79.5
percentage = float(input('percent of the score: ')) #25%

Needed_score = (minimum - current* (100 - percentage) /100) *100/percentage
Needed_score = round(Needed_score, 2)

print('you need a score', Needed_score, 'to get the grade', grade)
