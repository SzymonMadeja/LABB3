paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0


while paliwo > 0:
    paliwo = paliwo - paliwo_zuzyte_na_s
    czas += 1
    print(f"Aktualny stan paliwa to {paliwo}\n Przebyty czas: {czas}s")

   
print("Brak paliwa, koniec lotu")