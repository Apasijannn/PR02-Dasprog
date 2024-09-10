HH,MM,SS =map(int,input().split(':'))
CH,CM,CS =map(int,input().split(':'))

HH -= 2
CH -= 7
HS = HH*3600
MS= MM*60
CHS = CH*3600
CMS = CM*60

while HH-CH <= 24:
    if  HS-CHS or MS-CMS or SS-CS != 0:
        print (f'{HS-CHS:02}:{MS-CMS:02}:{SS-CS:02}')
        print('See you on the next Pear event')
    break