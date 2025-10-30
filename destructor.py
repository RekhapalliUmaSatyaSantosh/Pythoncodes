# import time
# class test:
#     def __init__(self):
#         print('obj initialization activities.....')
#     def __del__(self):
#         print('Destructor')
# t=test()
# t=None
# time.sleep(1)
# print('End of obj')

# class test:
#     def __init__(self):
#         print('Constructor')
#     def __del__(self):
#         print('Destructor')
# t=test()
# t1=test()
# t=None
# print('End of obj')

# import time
# class test:
#     def __init__(self):
#         print('Contructor Execution...')
#     def __del__(self):
#         print('Destructor Execution...')
# t1=test()
# t2=t1
# t3=t1
# del t1
# print('Object not destroyed after deleting t1')
# time.sleep(10)
# del t2
# print('Object not destroyed even after deleting t2')
# time.sleep(10)
# print('Deleting last refernce')
# del t3
# print('End of application')
# l=[test(),test(),test()]
# print('hello')
# del l
# time.sleep(10)
# print('end')

# import sys
# class test:
#     pass
# t1=test()
# t2=t1
# t3=t2
# t4=t3
# print(sys.getrefcount(t1))

n=float(input())
# for i in range(n):
if n==float:
    print('True')
else:
    print('False')
        