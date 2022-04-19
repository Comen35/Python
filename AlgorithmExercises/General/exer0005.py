# Klavyeden girilen suyun sıcaklığına göre halini(katı, sıvı, gaz) gösteren program 
temperature = float(input('Enter temperature : '))

if temperature < 0 : 
    print("Solid")
elif temperature >= 0 and temperature < 100:
    print("liquide")
else :
    print("Gase")

