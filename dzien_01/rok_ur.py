today=2022
yob=int(input("podaj rok urodzenia:"))

if today - yob < 18:
    print('jesteś niepełnoletni')
elif today- yob > 101:
    print ('prawdopodobnie już nie żyjesz')
else:
    print('jesteś pełnoletni')

