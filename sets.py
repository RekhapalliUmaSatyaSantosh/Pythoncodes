# fruits={"apple","banana","cherry"}
# # fruits.remove("banana")  
# # print(fruits)
# for x in fruits:
#     print(x)

# set_1={1,2,3,4,5}
# set_2={4,5,6,7,8}
# intersection=set_1*set_2
# print(intersection)

n=int(input("enter no.of students"))
d={}
for i in range(n):
    name=input("Enter name of student:")
    marks=int(input("enter marks of student:"))
    d[name]=marks
print('*'*30)
print('NAME','\t\t','MARKs')
print('*'*30)
for name in d:
    print(name,'\t\t',d[name])