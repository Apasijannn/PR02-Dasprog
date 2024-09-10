Data_usage = float(input('Data usage: '))

if 0.0 < Data_usage <= 1.0:
    print ('charges: 250')
elif 1.0 < Data_usage <= 2.0:
    print('charges: 500')
elif 2.0 < Data_usage <= 5.0:
    print('charges: 1000')
elif 5.0 < Data_usage <= 10.0:
    print('charges: 1500')
elif Data_usage > 10.0:
    print('charges: 2000')
elif Data_usage < 0.0:
    print('bad data')