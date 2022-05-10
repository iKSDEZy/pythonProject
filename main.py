# 0-100
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz


spisok1 = list(range(0, 101))
print(spisok1)
for num in spisok1:
    ostatok = num % 3
    ostatok2 = num % 5
    if ostatok + ostatok2 == 0:
        print(num , 'FizzBuzz')
    else:
        if ostatok == 0:
            print(num, 'Fizz')
        if ostatok2 == 0:
            print(num, 'Buzz')



