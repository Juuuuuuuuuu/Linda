
list = 'процент'
number = int(input('vedi'))
if number == 1:
    print(number, list)
elif 2 <= number <=4:
    print(number, list + 'а')
elif 5 <= number <= 100:
    print(number, list + 'ов')