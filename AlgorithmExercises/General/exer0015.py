"""
    Klavyeden girilen N elemanlı bir A dizisinin elemanlarının karelerini alarak B dizisini;
    Kareköklerini alarak  C dizisini oluşturup bu yeni iki dizinin skaler çarpımını bulan
    program.
"""
A = []
B = []
C = []
try:
    while True:
        value = input('Enter an integer please :')
        if(value == ''):
            break
        value = int(value)
        A.append(value)
        B.append(value * value)
        C.append(pow(value, 0.5))

except:
    print("Enter a valid value please!")

scaler_sum = 0
for i in range(len(B)):
    scaler_sum += B[i] * C[i]
print(A)
print(B)
print(C)
print(scaler_sum)
