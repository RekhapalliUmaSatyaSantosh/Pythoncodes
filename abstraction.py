# # from abc import abstractmethod
# class vehicle:
#     # @abstractmethod
#     def getwheels(self):
#         pass

# from abc import abstractmethod,ABC
# class vehicle(ABC):
#     # @abstractmethod
#     def getnoofwheels(self):
#         pass
# class bus(vehicle):
#     def getnoofwheels(self):
#         return 6
# class car(vehicle):
#     def getnofwheels(self):
#         return 4
# b=bus()
# print(b.getnoofwheels())
# c=car()
# print(c.getnofwheels())

# from abc import*
# class test(ABC):
#     @abstractmethod
#     def m1(self):
#         print('This is m1 method')
#     @abstractmethod
#     def m2(self):
#         print('This is m2 mthod')
# class subtest(test):
#     def m1(self):
#         pass
#     def m2(self):
#         pass
# t=subtest()
# t.m1()
# t.m2()

# from abc import*
# class interface(ABC):
#     @abstractmethod
#     def m1(self):
#         print('This is m1 method')
#     @abstractmethod
#     def m2(self):
#         print('This is m2 method')
#     @abstractmethod
#     def m3(self):
#         print('This is m3 method')
# class abstract(interface):
#     def m1(self):
#         print('This is m1 method')
#     def m2(self):
#         print('This is m2 method')
# class concrete(abstract):
#     def m3(self):
#         print('This is m2 method')
# c=concrete()
# c.m1()
# c.m2()
# c.m3()

# class test:
#     def __init__(self):
#         self.x=10
#     def m1(self):
#         print('public method')
#     def m2(self):
#         print(self.x)
#         self.m1()
# t=test()
# t.m2()
# print(t.x)
# t.m1()

# class test:
#     def __init__(self):
#         self.__x=10
#     def __m1(self):
#         print('It is private method')
#     def m2(self):
#         print(self.__x)
#         self.__m1()
# t=test()
# t.m2()
# print(t._test__x)
# t._test__m1()

# class test:
#     def __init__(self):
#         self._x=10
#     def _m1(self):
#         print('This is protected class')
# class subtest(test):
#     def m2(self):
#         print(self._x)
#         self._m1()
# t=subtest()
# t.m2()
# print(t._x)
# t._m1()

import calendar
help(calendar)
