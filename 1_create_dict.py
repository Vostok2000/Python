# Словари

# Создаем англо-русский словарь
# Ключ- слово на английском языке
# Значение - слово на русском языке

english_dict={
    'apple':'яблоко',
    'milk':'молоко',
    'cat':'кот'
}
russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely']
)
for key in english_dict:
    print(key)
    print(english_dict[key])


#       название_словаря[ключ]

# Обращение к элементу словаря с помощью метода get()
word = input("Введите слово")
print(english_dict.get(word))
# get() - возвращает значение по ключу, если такой ключ есть в словаре
# в противном случае возвращает None

#вывод элементов словаря с помощью цикла
#for key in название_словаря:print(key)
