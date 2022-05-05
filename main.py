'''
Написать программу которая :
1. Высчитывает возраст из заданных данных (current_year - нынешний год, year_of_birth - год рождения)
#current_year = 2022
#year_of_birth = 1988
'''
current_year = 2022
year_of_birth = 1988

a = int(input("Введите Ваш год рождения: "))
b = int(input("Введите нынешний год: "))
age = (b - a)
print(age)

# '''



'''Найти недостающую часть кода (code_2)
a. Найдите остаток от х деленого на у
b. Полученный результат умножьте на 13
c. Извлеките квадратный корень из полученного результата
d. Возьмите целую часть от результата
code_2 data
x = 152
y = 132
'''

x = 152
y = 132

result_a = x % y
result_b = result_a * 13
result_c = result_b ** 0.5
result_d = int(result_c)
print(result_a, result_b, result_c, result_d)

'''
 Соединить код в отдельную переменную пример:
        475-12-967

'''
code_1 = '354' #str
code_2 = result_d #int
code_3 = 132 #int

total_code = code_1 + "-" + str(code_2) + "-" + str(code_3)
print(total_code)

print("Hello Mary Gold. You are " + str(age) + " years old. Your secret code is " + total_code + ".")


'''

'''



