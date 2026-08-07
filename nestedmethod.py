class test:
    def m1(self):
        def calc(a,b):
            print('sum=',a+b)
            print('minus=',a-b)
            print('product=',a*b)
            print('divide=',a/b)
            print('average=',(a+b)/2)
        calc(100,200)
        calc(200,100
             )
t=test()
t.m1()