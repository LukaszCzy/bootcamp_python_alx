city_1 = input('Podaj miasto startowe: ')
city_2 = input('Podaj cel podroży:')
distance = int(input('Podaj dystans:'))
fuel_usage = float(input('podaj spalanie paliwa:'))
fuel_price = float(input('podaj cenę paliwa za litr:'))


cost = (distance*fuel_usage / 100) * fuel_price

print(f'Koszt przejazdu na trasie z {city_1} do {city_2} wynosi {cost} PLN')
