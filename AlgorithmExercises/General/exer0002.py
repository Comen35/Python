# Klavyeden üç kenarı girilen bir üçgenin türünü (eşkenar, ikizkenar, çeşitkenar) belirleyen program

first_edge = input("Enter length of first edge :")

if type(first_edge) == int:
    first_edge = int(first_edge)
else:
    first_edge = float(first_edge)

second_edge =input("Enter length of second edge :")

if type(second_edge) == float:
    second_edge = float(second_edge)
else:
    second_edge = float(second_edge)

third_edge = input("Enter length of third edge :")
if type(third_edge) == int:
    third_edge = int(third_edge)
else:
    third_edge = float(third_edge)

if first_edge == second_edge == third_edge:
    print('equilateral triangle')
elif first_edge == second_edge or first_edge == third_edge or second_edge == third_edge:
    print("isosceles triangle")

else:
    print("scalene triangle")


