prod_1="ananas"
waga_1=2.5 
cena_1=25.5

prod_2="banan"
waga_2=5
cena_2=15

prod_3="cytryna"
waga_3=1
cena_3=10

suma = cena_1 + cena_2 + cena_3
swaga = waga_1 + waga_2 + waga_3

raport = f'''
{prod_1:30} {waga_1:5.2f} kg {cena_1:15.2f} PLN
{prod_2:30} {waga_2:5.2f} kg {cena_2:15.2f} PLN
{prod_3:30} {waga_3:5.2f} kg {cena_3:15.2f} PLN

-----------------------------------------------------------------
waga: {swaga} KG
suma: {suma} PLN

'''
print(raport)
