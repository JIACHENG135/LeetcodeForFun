class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        m = {}
        if not head:
            return
        q = collections.deque([head])
        while q:
            cur = q.popleft()
            m[cur] = Node(cur.val,None,None)
            if cur.next:
                q.append(cur.next)
        
        for node in m:
            new = m[node]
            if node.next:
                new.next = m[node.next]
            if node.random:
                new.random = m[node.random]
        return m[head]