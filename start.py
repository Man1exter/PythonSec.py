from random import randint
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