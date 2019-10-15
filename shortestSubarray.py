import collections
def shortestSubarray(a,b):
	k = len(b)
	m = collections.defaultdict(int)
	l = 0
	ans = [0,len(a)-1]
	for i in range(len(a)):
		if a[i] in b:
			m[a[i]] += 1
		while len(m) == k:
			# print(ans)
			
			if len(m) == k:
				ans = min(ans,[l,i],key=lambda x:abs(x[0]-x[1]))
			if a[l] in b:
				m[a[l]] -= 1
				if m[a[l]] == 0:
					del m[a[l]]
			l += 1
	return a[ans[0]:ans[1]+1]

def shortestSubarray(a,b):
	k = len(b)
	ct = 0
	m = collections.defaultdict(int)
	counter = collections.Counter(b)
	l = 0
	ans = [0,len(a)-1]
	for i in range(len(a)):
		if a[i] in b and a[i]<:
			m[a[i]] += 1
		while len(m) == k:
			# print(ans)
			
			if len(m) == k:
				ans = min(ans,[l,i],key=lambda x:abs(x[0]-x[1]))
			if a[l] in b:
				m[a[l]] -= 1
				if m[a[l]] == 0:
					del m[a[l]]
			l += 1
	return a[ans[0]:ans[1]+1]

# a = "abcaabc"   
# b = "bca"
a = "dancbbkcld" 
b = "ankb"
print(shortestSubarray(a,b))
