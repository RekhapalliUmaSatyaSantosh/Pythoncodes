import random
low=int(input("Enter lower bound: "))
high=int(input("Enter upper bound: "))
num=random.randint(low,high)
guess=0
while guess!=num:
    print(f"Guess a number between {low} and {high}:",end=" ")
    guess=int(input())
    if guess<num:
        print("Too Low!")
    elif guess>num:
        print("Too High!")
    else:
        print(f"Congratulatons you guessed the number {num} correctly!")
    