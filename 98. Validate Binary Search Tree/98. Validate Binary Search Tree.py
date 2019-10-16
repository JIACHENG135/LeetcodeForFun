class Solution:
    def isValidBST(self,root) -> bool:
        if not root:
            return True
        else:
            st = [[root,float("inf"),-float("inf")]]
            while st:
                node,up,low = st.pop()
                if node.val>=up or node.val<=low:
                    return False

                if node.right:
                    mml = max(node.val,low)
                    st.append([node.right,up,mml])
                if node.left:
                    mmu = min(node.val,up)
                    st.append([node.left,mmu,low])
            return True