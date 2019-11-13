class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        g = collections.defaultdict(set)
        nameMap = {}
        emailSet = set()
        
        for name,*emails in accounts:
            emailSet |= set(emails)
            firstMail = emails[0]
            nameMap[firstMail] = name
            for email in emails[1:]:
                g[email].add(firstMail)
                g[firstMail].add(email)
                nameMap[email] = name
                
        cc = collections.defaultdict(list)
        ccn = 0
        visited = set()
        def dfs(email,ccn):
            cc[ccn].append(email)
            visited.add(email)
            for nei in g[email]:
                if nei not in visited:
                    dfs(nei,ccn)
            
        res = []
        for email in emailSet:
            if email not in visited:
                ccn += 1
                dfs(email,ccn)
        
        for key in cc:
            name = nameMap[cc[key][0]]
            res.append([name]+sorted(cc[key]))
        return res
            