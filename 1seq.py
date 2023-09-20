result = list()
for i in range(1,int(input('Введите количество элементов: '))+1):
    result.append(int(input('Введите {} элемент: '.format(i))))
result.sort()
print('Вывод:', result)