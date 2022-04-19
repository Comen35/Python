"""
    Klavyeden girilen bir A dizisinin elemanlarını ters sıra ve işaretle B dizisine aktaran
    program
"""
A = []

try:
    while True:
        value = input('Enter an integer please: ')
        if value == '':
            break
        A.append(int(value))

except:
    print('Enter a valid value please!')

B = []

for i in range(len(A) - 1, -1, -1):
    B.append(-1 * A[i])

print(B)
