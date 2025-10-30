# def add(n1,n2):
#     return n1 + n2
# def subtract(n1,n2):
#     return n1 - n2
# def multiply(n1,n2):
#     return n1 * n2
# def divide(n1,n2):
#     if n2 == 0:
#         return "Error! Division by zero."
#     return n1 / n2
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))    
# choice=input("Enter operation (1, 2, 3, 4): ")
# if choice == '1':
#     print(f"{num1} + {num2} = {add(num1, num2)}")
# elif choice == '2':
#     print(f"{num1} - {num2} = {subtract(num1, num2)}")
# elif choice == '3':
#     print(f"{num1} * {num2} = {multiply(num1, num2)}")
# elif choice == '4':
#     print(f"{num1} / {num2} = {divide(num1, num2)}")
# else:
#     print("Invalid operation selected.")
# ch=input("Do you want to continune (yes/no):")
# while choice<'5':
#     if ch=='yes' or ch=='y':
#         num1=int(input("Enter first number: "))
#         num2=int(input("Enter second number: "))    
#         choice=input("Enter operation (1, 2, 3, 4): ")
#         if choice == '1':
#             print(f"{num1} + {num2} = {add(num1, num2)}")
#         elif choice == '2':
#             print(f"{num1} - {num2} = {subtract(num1, num2)}")
#         elif choice == '3':
#             print(f"{num1} * {num2} = {multiply(num1, num2)}")
#         elif choice == '4':
#             print(f"{num1} / {num2} = {divide(num1, num2)}")
#         else:
#             print("Invalid operation selected.")
#     else:
#         print("Thank you!")

print(eval(input("enter")))
# print(int(eval(input("Enter"))))