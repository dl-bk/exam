# Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

# start = int(input("Enter start of range: "))
# end = int(input("Enter end of range: "))
# summ = 0
# if start <= end:
#     for number in range(start, end +1):
#         summ += number
# else:
#     for number in range(end, start +1):
#         summ += number
# print(summ)

# Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

summ = 0
for number in range(1, 101):
    if number % 2 == 0:
        summ += number
print(summ)

# Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

# string = input("Enter string: ")
# for char in string:
#     print(char)

# Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку
    
import random
lst = [random.randint(0,50) for _ in range(10)]
new_lst = [num for num in lst if num % 2 == 0]
print(new_lst)

# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери
# def capital_strings(lst):
#     capital_str_lst = [word for word in lst if word[0].isupper()]
#     return capital_str_lst

# u_lst = [input("Enter word: ") for _ in range(5)]
# cap_lst = capital_strings(u_lst)
# print(cap_lst)

# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".
def python_filter_str(lst):
    str_with_python = [string for string in lst if 'python' in string.lower()]
    return str_with_python

user_str_lst = [input("Enter string: ") for _ in range(5)]
py_lst = python_filter_str(user_str_lst)
print(py_lst)