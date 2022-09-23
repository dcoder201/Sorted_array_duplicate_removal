
class Solution:    
    def remove_duplicate(self, A, N):
        # code here
        k=list(set(A))
        k.sort()
        A[:]=k[:]
        return(len(A))
                
