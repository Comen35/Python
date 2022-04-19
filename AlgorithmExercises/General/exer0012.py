"""
    Klavyeden girilen satır sayısına göre aşağıdaki üçgeni oluşturan program

1   
2   1
3   2   1
4   3   2   1
"""

try:
    row_number = int(input('Enter row number please: '))

except: 
    print('Enter valid value please!')

for i in range(1, row_number + 1):
        for j in range(i, 0, -1):
            print(f'BACH     ', end='')
        print()