snum = ['первого', 'второго']
sp= list()
for i in range(len(snum)):
	ss = input('Введите элементы {} списка через один из разделителей (, ; /): '.format(snum[i]))
	if ss.find(',') != -1:
		simb = ','
	elif ss.find(';') != -1:
		simb = ';'
	else:
		simb = '/'
	si = ss.split(simb)
	sp.append(list(set(si)))
su = [item for item in sp[0] if item not in sp[1]]
print('Результат: ', end='')
for s in su:
	if s!=su[len(su)-1]:
		print(s, end=', ')
	else:
		print(s)