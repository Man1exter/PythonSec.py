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

lista = []
print(lista)

lista = ['Mariusz','Kamil','Anna','Krzysztof','Janusz','Justyna','Wiktoria']
print(lista)
print("index 0: ",lista[0])
print("index 2: ",lista[2])
print("index 3: ",lista[3])
print("index 4: ",lista[4])

lista[1] = "USUNIETO"
print(lista)

print(lista + ["JOSZUA", "SOSZUSZKA"])
print(lista * 2)
print("Ilosc elementow w liscie(bez zaliczenie mnozenia jej o 2): ", len(lista))
lista.append("HIERONINIM")

print("======================================================")

lista2 = []
lista2.append("HIERONINIM")
lista2.append("ROMUALDNODO")
lista2.append("KWOSTELIUSZON")
print(lista2)


print(" --- ")
print(" --- ")
################################################################################################################

################################################################################################################

mezczyzna = input("Podaj imie mezczyzny: ")
kobieta = input("Podaj imie kobiety: ")
dziecko1 = input("Podaj imie dziecka1: ")
dziecko2 = input("Podaj imie dziecka2: ")

wybor1 = 1
wybor2 = 2

print("Witamy rodzinke: ",mezczyzna," ",kobieta," ",dziecko1," ",dziecko2)
print("Jaki problem?")
print("Jedzenie [1]")
print("Szkoła [2]")
decyzja = input("Ktory numerek: ? ")
if decyzja == 1:
    print("Odwiedz nas na fb")
elif decyzja == 2:
    print("zadzwon do nas")
else:
    print("cos zle zostalo napisane")

################################################################################################################

################################################################################################################

it = 0
print("bez petli => ",it)
print("odlicza do 10 ale jest warunek..")

while it < 10:
    print(it)
    it += 1
    if it == 7:
        break

print("Koniec tego dobrego z whilem :D")

print("  ")
print("  ")
print("  ")

################################################################################################################

################################################################################################################

print("Moge wejsc do klubu?")
print("----------------------")
imie = input("Jak masz na imie? ")
wiek = int(input("Ile masz lat? "))
kasa = int(input("Ile masz kasy przy sobie? "))


if wiek >= 18 and kasa >= 50:
    print("Zapraszam do srodka",imie)
else:
    print("Sorry nie spelniasz wymagan")

if wiek >= 18 or kasa >= 50:
    print("Zawsze mozesz wypic sok przy ladzie")

print("  ")
print("  ")

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