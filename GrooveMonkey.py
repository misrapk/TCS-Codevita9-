def findLcm(num1, num2):
	if(num1 > num2):
		num = num1
		den = num2
	else:
		num = num2
		den = num1

	rem = num % den
	while(rem != 0):
		num = den
		den = rem
		rem = num % den

	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd))

	return lcm



t = int(input())
while(t!=0):
	n = int(input())
	monkey = list(map(int, input().split()))
	steps = set()
	monkey.insert(0,0)

	for i in range(1,n+1):
		if (monkey[i] ==0):
			continue

		count = 0
		current = i
		block = i
		while(True):
			current = monkey[current]
			monkey[block] = 0
			block = current 
			count += 1
			if(current==i):
				break

		steps.add(count)

	if(len(steps) == 1):
		for x in steps:
			print(x)

	else:
		s = list(steps)
		lcm = findLcm(s[0], s[1])
		for i in range(2, len(s)):
			lcm = findLcm(lcm , s[i])

		print(lcm)

	t = t-1
