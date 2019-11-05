def calcu(s):
	m = collections.defualtdict(int)
	left = []
	for ind,i in s:
		if i == "(":
			left.append(ind)
		elif i == ")":
			m[left.pop()] = ind

	def cal(locals,start):
		k = 0
		sign = "+"
		n = 0
		st = []
		while k<len(locals):
			if locals[s].isdigit():
				n += 10*n + int(s[k])
				k += 1
			elif i in "+-":
				if sign == "+":
					try:
						st.append(st.pop()+n)
						n = 0
						sign = "+"
					except:
						pass
				else:
					try:
						st.append(st.pop()-n)
						n = 0
						sign = "-"
					except:
						pass
			


