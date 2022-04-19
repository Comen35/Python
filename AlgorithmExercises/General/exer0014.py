"""
    Klavyeden girilen N elemanlı A, B, C dizilerini kullanarak D=A+B-C işlemiyle
    D dizisini oluşturup, bu yeni diziyi büyükten küçüğe doğru sıralayan program.
"""

A = []
B = []
C = []
D = []

for i in range(3):
    if i == 0:
        print("A Dizisi")
    if i == 1:
        print("B Dizisi")
    if i == 2:
        print("C Dizisi")

    while True:
        try:           
            if(i == 0):
                value = input('Enter an integer please : ')
                if(value == ''):
                    break
                A.append(value)
            if(i == 1):
            
                value = input('Enter an integer please : ')
                if(value == ''):
                    break
                B.append(value)
            if(i == 2):
                
                value =input('Enter an integer please : ')
                if(value == ''):
                    break
                C.append(value)          
        except:
            print("Enter a valid value please!")
    print("******************************")

for i in range(0, len(A)):
    D.append(int(A[i]) + int(B[i]) - int(C[i]))

print("**************************")

print(A)
print(B)
print(C)
print(sorted(D))