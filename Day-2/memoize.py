def memoize(func):
    memo = {}
    def wrappeer(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return wrappeer
        
        

@memoize
def fib(n):
     if n == 0:
         return 0
     elif n == 1:
         return 1
     else:
         return fib(n-1)+fib(n-2)
     
print(fib(100))