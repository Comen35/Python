try:
    upperBound = int(input('Enter an integer please :'))
    T1 = 0 
    T2 = 0
    T3 = 0
    T4 = 0
    T5 = 0
    T6 = 0

    for i in range(1, upperBound + 1):
        if(i >= 1):
            T3 += i / (i * i) + 1
            T5 += i / (i + 1)
            T6 += i / (i * 2)
        if i >= 2:
            if i % 2 == 0:
                T2 += i / (((i - 1) * 2) + 1 )
                T4 += i / ( i * (i - 1)  + (i - 1))
            else:
                T2 -= i / (((i - 1) * 2) + 1 )
                T4 -= i / ( i * (i - 1)  + (i - 1))
        if i >= 5:
            T1 += i / (i - 2)

    print(f'T1 = {T1}') 
    print(f'T2 = {T2}') 
    print(f'T3 = {T3}') 
    print(f'T4 = {T4}') 
    print(f'T5 = {T5}') 
    print(f'T6 = {T6}') 


except:
    print('Enter a valid value!!')




