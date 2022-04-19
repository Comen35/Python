"""
    Girilen ay adına göre, bunun yılın kaçıncı ayı olduğunu bulan program
"""

from operator import indexOf


months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'Agust',
    'September',
    'October',
    'Novermber',
    'December'
]

month = input('Enter a month name please: ')

if month.capitalize() in months:
    print(int(indexOf(months, month.capitalize()) + 1))
else:
    print('Enter a valid month name please...')
