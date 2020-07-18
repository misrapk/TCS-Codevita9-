n = int(input())

f = input()
m = input()

countR = m.count('r')
countM = m.count('m')

lst1 = [i for i in f]

for i in f:
	if i == 'r':
		if countR == 0:
			print(len(lst1), end= '')
			break

		countR -=1
		lst1.pop(0)

	elif  i == 'm':
		if countM == 0:
			print(len(lst1), end = '')
			break
		countM -= 1
		lst1.pop(0)

else:
	print(0, end = '')

