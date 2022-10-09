waga=int(input("podaj wagę w kg: "))
#wzrost=float(input("podaj wzrost w metrach: "))
wzrost=int(input("podaj wzrost w cm: "))
#bmi = waga / wzrost**2
bmi = waga / (wzrost*0.01)**2
print(f'Twoje bmi wynosi: {bmi:.2f}')

