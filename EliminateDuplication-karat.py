def eliminate(s):
	res = []
	k = 0
	while k<len(s):
		if not res:
			res.append([s[k],1])
			k += 1
		else:
			top = res.pop()
			if s[k] == top[0]:
				if top[1] == 2:
					cur = top[0]
					while k<len(s) and s[k] == cur:
						k += 1
				else:
					top[1] += 1
					res.append(top)
					k += 1
			else:
				res.append(top)
				res.append([s[k],1])
				k += 1
	ans = ""
	for s,n in res:
		ans += s*n
	return ans
res = eliminate("aabcccbcccba")
print(res)
