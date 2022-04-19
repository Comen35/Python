
A = []
B = []
C = []

while True:
    value = input('Enter a number please: ')
    if(value == ''):
        break

    A.append(float(value))

sum = 0

for i in A:
    sum += i

arithmetic_mean = sum / (len(A))

for i in A:
    if i < arithmetic_mean:
        B.append(i)
    if i > arithmetic_mean:
        C.append(i)

print(f'Arithmetic mean: {arithmetic_mean}')
print(A)
print(B)
print(C)


