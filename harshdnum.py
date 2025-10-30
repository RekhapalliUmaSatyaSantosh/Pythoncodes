# def is_harshad_number(n):
#     if n == 0:
#         return False
#     digit_sum = sum(int(d) for d in str(n))
#     return n % digit_sum == 0
# for i in range(1, 101):
#     if is_harshad_number(i):
#         print(i, end=' ')

def is_harshad_number(n):
    if n == 0:
        return False
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0
num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")