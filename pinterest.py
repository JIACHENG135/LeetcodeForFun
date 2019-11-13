import collections
def longestPrefix(words):
	ans = list(range(len(words)))
	ct = 0
	longestLength = max([len(word) for word in words])
	while ct<longestLength and len(ans)>0:
		prev = ans
		wait = []
		biggerThenTwo = collections.defaultdict(set)
		for i in ans:
			if ct<len(words[i]):
				biggerThenTwo[words[i][ct]].add(i)
		for key in biggerThenTwo:
			if len(biggerThenTwo[key])>1:
				wait.extend(biggerThenTwo[key])
		ans = wait
		ct += 1
	return words[prev[0]][:ct-1]


a = longestPrefix(["bandage","banana","anchor","anchovy","bass"])
print(a)
