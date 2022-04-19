# Klavyeden girilen iki sayıdan büyük olanını bulan program

try:
    number1 = int(input("Enter an integer please : "))
    number2 = int(input("Enter an integer please :"))
    if number1 > number2:
        print(f'{number1} > {number2}')
    else:
        print(f'{number2} > {number1}')
except:
    print("Enter an integer please!!")



