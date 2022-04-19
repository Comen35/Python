"""
    0-255 arasında girilen bir tamsayının ASCII kod karşılığını ekrana yazdıran program
"""

try : 
    number = int (input("Enter a number in range 0 - 255 : "))

    if number < 0 or number > 255:
        raise "Enter an integer in range 0 - 255 please!!"
    else:
        print(chr(number))

except: 
    print("Enter an integer please ")


