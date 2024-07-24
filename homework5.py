# Задайте переменные разных типов данных:
immutable_var = 1, 'a', 3, 'g'
print('Immutable tuple:', immutable_var)

# Изменение значений переменных:
# immutable_var[0] = 200 # в данном случае невозможно изменить, т.к. кортеж относится к неизменяемым типам данных

# Создание изменяемых структур данных:
mutable_list = [1, 'table', 4, 'pen']
mutable_list[0]=3
print('Mutable_list:', mutable_list)