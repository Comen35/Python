""" Klavyeden girilen N değerine göre (N > 20); 
    A-) 10 - N arası tüm sayıların toplamını, 
    B-) 5-N arası tek sayıların çarpımını
    C-) 14-N arası çift sayıların toplamını
    hesaplayan program   
"""
from unittest import result


class NumberNotInRange(Exception):
   
    def __init__(self, number, message="Number is not greater than 20"):
        self.salary = number
        self.message = message
        super().__init__(self.message)

resultA = 0  
resultB = 1 
resultC = 0
try:
    number = int(input('Enter an integer greater than 20 : '))
    if(number <= 20):
        raise NumberNotInRange(number)
    else:
        for i in range(1, number):
            if(i >= 10):
                resultA += i
            if(i >= 5 and i % 2 != 0):
                resultB *= i
            if(i >= 14 and i % 2 == 0):
                resultC += i

    print(f'10 {number} arası sayıların toplamı: {resultA}')
    print(f'5 {number} arası tek sayıların çarpımı: {resultB}')
    print(f'14 {number} arası çift sayıların toplamı: {resultC}') 
except:
    print("Enter an integer  greater than 20 please!!")




       

