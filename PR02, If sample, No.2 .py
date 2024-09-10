weight = float (input('weight : '))
height = float (input('height : '))
pounds_weight = float(weight * 2.20) 
inches_height = float (height * 0.39)
BMI = float ((703 * pounds_weight / inches_height **2))
print (f'BMI: {BMI:.1f}' )
if BMI < 18.5:
    print ('Underweight')
elif 18.5 <= BMI <= 24.9:    
    print ('Normal')
elif 25.0 <= BMI <= 29.9:
    print ('Overweigth')
elif BMI >= 30:
    print ('Obese')
