"""
    Klavyeden girilen bir N değerine göre tek indisli elemanları '0', çift indisli elamanları
    '1' olan N elemanlı bir A dizisini oluşturan program
"""
A = []
try:
    lengthOfList = input('Enter length of the List: ')
    for i in range(int(lengthOfList)):
        if i % 2 == 0 :
            A.append(0)
        else:
            A.append(1)
except:
    print('Enter a valid value please!')

print(A)