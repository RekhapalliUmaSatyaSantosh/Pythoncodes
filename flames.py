name1 = input()
name2 = input()
list1 = list(name1)
list2 = list(name2)
count = 0
for char1 in list1:
    if char1 in list2:
        count += 1 
        list2.remove(char1)
result = len(name1) + len(name2) - (2 * count)
flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]
while len(flames) > 1:
    index_to_remove = (result % len(flames)) - 1  
    if index_to_remove >= 0:
        flames = flames[index_to_remove + 1:] + flames[:index_to_remove]
    else:
        flames = flames[:len(flames) - 1]
print(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {flames[0]}")