def largestNum(num):
	numStr = str(num)
	i = 9
	while i>=0:
		if str(i) in numStr:
			return i
		i -= 1


def smallestNum(num):
	numStr = str(num)
	i =0
	while i<=9:
		if str(i) in numStr:
			return i
		i += 1

def findPair(num):
	if num ==2:
		return 1
	if num >= 3:
		return 2
	return 0


N = int(input())

nums = list(map(int, input().split()))

assert(len(nums) == N)

bitscore = [""]*N

for i in range(len(bitscore)):
	curScore = str(11*largestNum(nums[i]) + 7*smallestNum(nums[i]))
	if len(curScore) > 2:
		curScore = curScore[1:]

	bitscore[i] = curScore

oddFreq = [0] *10
evenFreq = [0] * 10

for i in range(len(bitscore)):
	index = int(bitscore[i][0])
	if (i+1)%2 ==0:
		evenFreq[index]+=1
	else:
		oddFreq[index] += 1

countPairs = [0] * 10
for i in range(10):
	if evenFreq[i] <=1 and oddFreq[i] <=1:
		continue
	countPairs[i] += findPair(evenFreq[i]) + findPair(oddFreq[i])
	countPairs[i] = min(2, countPairs[i])

print(sum(countPairs), end = "")