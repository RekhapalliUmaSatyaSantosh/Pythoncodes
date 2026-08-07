a=input("Enter a brace:")
if a == "[""]":
    print("It is a list")
elif a=="("")":
    print("It is a tuple")
elif a=="{""}":
    print("It is a set")
else:
    print("It is neither a list nor a tuple")