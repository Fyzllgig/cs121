def fibonacci(n,depth):
    if n<=2:
        print ' '*depth,'base case reached!'        
        return 1
    else:
        print ' '*depth,'now computing the component fibonacci values of',n
        return fibonacci(n-1,depth+1)+fibonacci(n-2,depth+1)
    
def test():
    assert fibonacci(1,0)==1
    assert fibonacci(3,0)==2
    assert fibonacci(10,0)==55