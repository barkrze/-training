class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        r_str = x_str[::-1]
        print(r_str[-1])
        if(r_str[-1] == '-'):
            r_str = f"-{r_str[:-1]}"
        
        r = int(r_str)
        return r
