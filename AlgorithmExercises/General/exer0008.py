"""
    Klavyeden girilen bir ondalıklı sayıyı, tam ve ondalık kısımnlarını ayırıp ayrı ayrı yazdıran program
"""

number = input("Enter an float number plase: ")
number = number.split('.')
print(number[0])
print(number[1])