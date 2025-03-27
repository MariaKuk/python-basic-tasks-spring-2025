"""
Изменяемые и неизменяемые типы данных.
Методы.
"""

list_ = []
print(list_)

print(list_.append(1000))

print(list_)

list_.append(1)
print(list_)

list_.sort()
print(list_)

list_.sort(reverse=True)
print(list_)

print("ABC".lower().capitalize())
