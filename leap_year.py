n=int(input('enter a year:'))
if  n%4 != 0 :
    print('given year not a leap year')
elif  n%100 != 0 :
    print('given year is leap year')
elif  n%400 != 0 :
    print('given year is not a leap year')
else :
    print('given year is a leap year')
