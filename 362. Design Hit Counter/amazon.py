def count(s):
	res = ""
	remain = ""
	cur = ""
	for l in s:
		if l!=cur:
			if remain:
				numb = remain[1:]
				if numb!="1":
					res += remain
				else:
					res += remain[0]
			remain = l + "1"
			cur = l
		else:
			numb = str(int(remain[1:])+1)
			remain = remain[0] + numb
	if remain:
		numb = remain[1:]
		if numb!="1":
			res += remain
		else:
			res += remain[0]
	print(res)
	return len(res)

a = count("aaabbbbbccccc")

print(a)