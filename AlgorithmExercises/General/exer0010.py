""" 
    1-99 arasında haneleri toplamı tek olan sayıların listesini veren program
"""

for  i in range(1, 100):
    toplam = 0

    for j in str(i):
        
        toplam += int(j)

    if toplam % 2 != 0:        
        print(i)