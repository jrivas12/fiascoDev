fruits = ('apple', 'apple', 'apple', 'mango', 'orange')
print(fruits.count('apple'))
d = len(fruits)
apple_count = fruits.count('apple') 
if apple_count / len(fruits) > 0.5: 
    print("There are too many apples here.")
else:
    print("Everything is good.")
