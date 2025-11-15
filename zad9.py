#Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
imie = input("Podaj imie: ") 

print(f"Witaj {imie}")

wiek = int(input("Podaj wiek: "))

print(f"Twój wiek to: {wiek}")

nazwisko = input("Podaj nazwisko:")

print(imie[0], nazwisko[0])

x = input("Podaj tekst: ")

for i in range(5):
    print(x)

z = input("Podaj 2 tekst: ")

trzeci = x,z

print(trzeci)

czwarty = imie,nazwisko

dlugosc = len(czwarty)

polowa = round((dlugosc / 2),0)

print(czwarty[0,polowa])

