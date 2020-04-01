    def climbStairs(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 2
        
        last = 1
        before_last = 2
        
        for index in reversed(range(0, n-2)):
            curr = before_last + last
            last = before_last
            before_last = curr
            
        return curr