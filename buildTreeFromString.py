import collections
class TreeNode:
	def __init__(self,val):
		self.val = val
		self.child = []
	def __repr__(self):
		res = []
		q = collections.deque([self])
		ct = 0
		while q:
			level = collections.deque()
			tmp = []
			ct += 1
			while q:
				cur = q.popleft()
				tmp.append(str(cur.val[0])+","+str(cur.val[1]))
				for c in cur.child:
					level.append(c)
			res.append("level " + str(ct)+":" + "|".join(tmp))
			q = level

		return " ".join(res)
		

def buildTreeFromString(s):
	st = []
	for ind,i in enumerate(s):

		if not st:
			st.append(TreeNode([ind]))
		else:
			prev = st[0]
			if i=="(":
				cur = TreeNode([ind])
				st[-1].child.append(cur)
				st.append(cur)
			else:
				st[-1].val.append(ind)
				st.pop()

	return prev

def buildTreeFromStringRecursive(s):
	m = {}
	left = []
	for i in range(len(s)):
		if s[i]=="(":
			left.append(i)
		else:
			m[left.pop()] = i 

	def helper(start,end):
		
		node = TreeNode([start,end])
		k = start+1
		print(start,end)
		while k<end:
			node.child.append(helper(k,m[k]))
			k = m[k] + 1
		return node
	return helper(0,m[0])

def countAndSay(s):
	mem = collections.defaultdict(lambda :1)

	def helper(s,prev):
		# print(s,prev,mem)
		wait = s+","+prev
		if wait in mem: 
			return mem[wait]
		if not s:
			mem[""] = 1
			return 1
		if len(s) == 1:
			return 0
		ans = 0
		for i in range(len(s)):
			for j in range(i+1,len(s)):
				cur = s[i:j]
				if cur!=prev:
					ans += helper(s[j:],cur)

		mem[wait] = ans
		return ans
	helper(s,"")
	ans = 0
	print(mem)

print(countAndSay("123"))




# print(buildTreeFromStringRecursive("(()()())"))



