from random import randint
import math
# kasa = 10000
# wiek = 43
# imie = input('Jak masz na imie: ')
# imie2 = input('Jak masz na imie: ')

# # print(imie)
# # print(imie2)

# if kasa >= wiek:
#     print("kasa wieksza od wieku " + imie )
# else:
#     print("slabo to wyglada" + imie2 )

print("Moge wejsc do klubu?")
print("----------------------")
imie = input("Jak masz na imie? ")
wiek = int(input("Ile masz lat? "))
kasa = int(input("Ile masz kasy przy sobie? "))


if wiek >= 18 and kasa >= 50:
    print("Zapraszam do srodka",imie)
else:
    print("Sorry nie spelniasz wymagan")


################################################################################################################

################################################################################################################

print("Program pierwszy dzienny Pythonowy")

numbs = randint(1,100)
odp = -1
ele = 0

print("===> Liczby od 1 do 100 <===")

while odp != numbs:
    ele += 1
    odp = int(input("Podaj liczbe: "))
    if odp > numbs:
        print("Mniejsza liczba!")
    elif odp < numbs:
        print("Wieksza liczba!")

print("Brawo!,odgadles za ",ele," razem swoja liczbe")
print("Wygrana liczba to: ", odp)
print("----------------------")

###################################################################################################################

####################################################################################################################

print("Program drugi dzienny Pythonowy")

a = int(input("Podaj liczbe a : "))
b = int(input("Podaj liczbe b : "))
c = int(input("Podaj liczbe c : "))
delta = b * b - 4 * a * c
print("delta wynosi: ",delta)
print('pierwiastek z delty wynosi: ',math.sqrt(delta))
print("----------------------")