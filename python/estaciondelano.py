month = int(input ('provides month of the year (1-12):  '))
stations = None # es esquivalente a null o vacia

if month == 1 or month == 2 or month == 12:
     stations = 'Winter'

elif month == 3 or month == 4 or month == 5:
         stations = 'Spring'
elif month == 6 or month == 7 or month == 8:
         stations = 'Summer'

elif month == 9 or month == 10 or month == 11:
         stations = 'Autumn'
else:
     stations= 'Wrong Month'

print (f'for the month {month} the stations is {stations}')