
def test(*args):
    print(args)
def test1(**kwargs):
    print(kwargs)
    print(len(kwargs))
    for i,v in kwargs.items():
        print(i,v)
test(1,2,3,4,5,6)
# dict = {1:1}
test1(a = '123',b ='456', c='789')