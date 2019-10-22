result = [["17-Jan.-2000",5617,5404],["17-Jan.-2000",5617,5404],["17-Jan.-2000",5617,5404]]
toString = lambda x: [str(i) for i in x]
result = [" ".join(toString(i)) for i in result]
for i in result:
	print(i)

class list(list):
	def __lt__(self,other):
		return sum(self)>sum(other)

a = [1,2]
b = [2,3]
c = [3,1.5]
import heapq,itertools
h = []
heapq.heappush(h,a,itertools.cmp_to_key = sum)
heapq.heappush(h,b,itertools.cmp_to_key = sum)
heapq.heappush(h,c,itertools.cmp_to_key = sum)
while h:
	print(heapq.heappop(h))
