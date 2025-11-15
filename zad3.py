ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

blok = [1,2,3,4,5]

lokal = [1,2,3,4,5,6,7,8,9,10]

i = 1

for nr_ulicy in ulice:
    for nr_bloku in blok:
        for nr_lokalu in lokal:
            print(nr_ulicy, nr_bloku,"/",nr_lokalu)


