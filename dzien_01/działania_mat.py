digit_1 = float(input("podaj pierwszą liczbę:"))
digit_2 = float(input("podaj drugą liczbę:"))
math_symbol = input('podaj rodzaj operacji')

addition = '+'
subtraction = '-'
multiplication = '*'
division = '/'
exponentiation = '**'


digit_1 - digit_2
digit_1 *  digit_2
digit_1 / digit_2
digit_1**digit_2
 
if math_symbol == '+':
    print(digit_1 + digit_2)
elif math_symbol == '-':
    print(digit_1 - digit_2)
elif math_symbol == '*':
    print(digit_1 * digit_2) 
elif math_symbol == '/':
        if digit_2 == 0:
            print('nie dziel przez zero')
        else:
            print(digit_1 / digit_2)
elif math_symbol == '**':
    print(digit_1 ** digit_2)
