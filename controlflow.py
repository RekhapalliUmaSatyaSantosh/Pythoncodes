# # num1=int(input("Enter first number:"))
# # num2=int(input("Enter second number:"))
# # num3=int(input("Enter third number:"))
# # if num1>num2 and num1>num3:
# #     print("Biggest number:",num1)
# # elif num2>num3:
# #     print("Biggest number:",num2)
# # else:
# #     print("Biggest number is:",num3)

# # a='hello'
# # print(a.replace('h','H'),)

# # a=int(input("Enter a number:"))
# # if a>=1 and a<=100:
# #     print(f"The number {a} is in between 1 and 100")
# # else:
# #     print(f"The number {a} is not in between 1 an 100")

# num = int(input("Enter a number between 0 to 9:"))
# if num == 0:
#     print('ZERO')
# elif num == 1:
#     print('ONE')
# elif num == 2:
#     print('TWO')
# elif num == 3:
#     print('THREE')
# elif num == 4:
#     print('FOUR')
# elif num == 5:
#     print('FIVE')
# elif num == 6:
#     print('SIX')
# elif num == 7:
#     print('SEVEN')
# elif num == 8:
#     print('EIGHT')
# elif num == 9:
#     print('NINE')
# else:
#     print('OUT OF RANGE')
    
# list=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
# list2=['','','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
# list3=['HUNDRED']
# num = int(input("Enter a number between 0 to 999:"))
# if num <0 and num >99 :
#     print("Out of range")
# elif num <= 19:
#     print(list[num]) 
# elif num <= 99:
#     a=num //10
#     b=num%10
#     if b==0:
#         print(list2[10])
#     else:
#         print(list2[a],list[b])

# output = " "
# if num == 0:
#     output = "ZERO"
# elif num <= 19:
#     output = list[num]
# elif num <= 99:
#     output = list2[num // 10] + ' ' + list[num % 10]
# elif num <= 999:
#     output = list[num // 100] + 'HUNDRED'
#     output += ' ' + list2[(num % 100) // 10]
#     output += ' ' + list[num % 10]
# else:
#     output = "Out of range"
# print(output)

for i in range(1,5):
    for j in range(i,5):
        print(i,end=" ")
    print("\n")