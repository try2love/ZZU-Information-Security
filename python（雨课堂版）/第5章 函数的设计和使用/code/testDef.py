def test(x:int, y:int) -> int:
    '''x and y must be integers, return an integer x+y'''
    #assert isinstance(x, int), 'x must be integer'
    #assert isinstance(y, int), 'y must be integer'
    z = x+y
    #assert isinstance(z, int), 'must return an integer'
    return z

x=test(1,2.0)
print(x)
