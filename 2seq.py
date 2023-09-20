ss = input('Введите любые цифры через один из разделителей (, ; /): ')
if ss.find(',') != -1:
    simb = ','
elif ss.find(';') != -1:
    simb = ';'
else:
    simb = '/'
si = ss.split(simb)
su = list(set(si))
print('Результат: ', end='')
for s in su:
    if s!=su[len(su)-1]:
        print(s, end=', ')
    else:
        print(s)