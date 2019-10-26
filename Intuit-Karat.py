import collections
def parent(edges):
	indegree = collections.defaultdict(int)
	nodes = set()
	for u,v in edges:
		nodes |= set([u,v])
		indegree[v] += 1
	one,zero = set(),set()
	for n in nodes:
		if indegree[n] == 0:
			zero.add(n)
		if indegree[n] == 1:
			one.add(n)

	return one,zero

def parent2(edges,s,e):
	g = collections.defaultdict(set)
	for u,v in edges:
		g[v].add(u)

	s1,s2 = set(),set()
	q = collections.deque([s])
	while q:
		cur = q.popleft()
		s1.add(cur)
		for nei in g[cur]:
			if nei not in s1:
				q.append(nei)
	q = collections.deque([e])
	while q:
		cur = q.popleft()
		s2.add(cur)
		for nei in g[cur]:
			if nei not in s2:
				q.append(nei)
	return len(s1.intersection(s2)) != 0

def parent3(edges,e):
	g = collections.defaultdict(set)
	for u,v in edges:
		g[v].add(u)

	q = collections.deque([e])
	visited = set()
	wait = []
	while q:
		level = collections.deque()
		tmp = []
		while q:
			cur = q.popleft()
			visited.add(cur)
			for nei in g[cur]:
				if nei not in visited:
					level.append(nei)
					tmp.append(nei)
		if tmp:
			q = level
			wait = tmp
	print(wait)
	return wait
edges = [[1,4], [1,5], [2,5], [3,6], [6,7]]
print(parent(edges))
print(parent2(edges,2,3))
print(parent3(edges,5))


		

