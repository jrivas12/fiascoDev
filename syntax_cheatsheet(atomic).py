class MainMenu:
    def __init__(self):
        self.topics = {
            '1': ("\033[94mFormats", FormatMenu()),
            '2': ("\033[93mClasses", ClassMenu()),
            '3': ("\033[92mControl Flow", ControlFlowMenu()),
            '4': ("\033[95mIterators", IteratorMenu()),
            '5': ("\033[96mDecorators", DecoratorMenu()),
            '6': ("\033[93mFunctions", FunctionMenu()),
            '7': ("\033[94mList and Tuples", ListandTuplesMenu()),
            '8': ("\033[95mDictionaries\033[0m", DictionaryMenu()),
        }

    def display(self):
        print("\033[96m=== Main Menu ===\033[0m")
        for key, topic in self.topics.items():
            print(f"{key}. {topic[0]}")
        print("0. Exit")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '0':
                print("Goodbye!")
                break

            if choice in self.topics:
                sub_menu = self.topics[choice][1]
                sub_menu.run()


class SubMenu:
    def __init__(self, examples):
        self.examples = examples

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. {example}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                print("Running example:", self.examples[int(choice) - 1])
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")


class FormatMenu(SubMenu):
    def __init__(self):
        examples = [
            '''name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: "My name is Alice and I am 25 years old."''',

            '''pi = 3.14159
message = "The value of pi is approximately {:.2f}".format(pi)
print(message)  # Output: "The value of pi is approximately 3.14"''',

            '''from string import Template

name = "Bob"
age = 30
template = Template("$name is $age years old.")
message = template.substitute(name=name, age=age)
print(message)  # Output: "Bob is 30 years old."'''
        ]
        super().__init__(examples)

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")


class ClassMenu(SubMenu):
    def __init__(self):
        examples = [
            '''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"''',

            '''class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: name={self.name}, age={self.age}, major={self.major}"''',

            '''class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account: number={self.account_number}, balance={self.balance}"'''
        ]
        super().__init__(examples)

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")



class ControlFlowMenu(SubMenu):
    def __init__(self):
        examples = [
            '''# Dynamic Formatting and If-Else Example
favorite_color = input("What is your favorite color? ")

if favorite_color.lower() == "blue":
    print(f"Oh, {favorite_color} is a calming and serene color!")
elif favorite_color.lower() == "red":
    print(f"{favorite_color} is a bold and energetic color!")
elif favorite_color.lower() == "green":
    print(f"{favorite_color} represents nature and growth!")
else:
    print(f"{favorite_color} is a great choice!")
''',

            '''# While Loop with User Input Example
total = 0

while True:
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break  # Exit the loop if the user enters 0
    total += number

print(f"The sum of all numbers entered is: {total}")
''',

            '''# For Loop with Range and If-Else Example
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
'''
        ]
        super().__init__(examples)

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")



class IteratorMenu(SubMenu):
    def __init__(self):
        examples = [
            '''# Using an Iterator with a List
fruits = ["apple", "banana", "orange"]

# Create an iterator from the list
fruit_iterator = iter(fruits)

# Iterate through the elements using a loop
for fruit in fruit_iterator:
    print(fruit)
''',

            '''# Creating a Custom Iterator
class SquaresIterator:
    def __init__(self, max_value):
        self.current = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        square = self.current ** 2
        self.current += 1
        return square

# Create a custom iterator that generates squares up to 9
squares_iterator = SquaresIterator(3)

# Iterate through the squares
for square in squares_iterator:
    print(square)
''',

            '''# Using the built-in enumerate() function
fruits = ["apple", "banana", "orange"]

# Iterate through the list and get both index and value
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
'''
        ]
        super().__init__(examples)

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")

class DecoratorMenu(SubMenu):
    def __init__(self):
        examples = [
            '''# Simple Function Decorator
def greet():
    return "Hello!"

# Define a decorator function
def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

# Apply the decorator to the greet() function
greet = uppercase_decorator(greet)

# Call the decorated function
print(greet())  # Output: "HELLO!"
''',

            '''# Decorator with Arguments
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Apply the decorator with argument to the greet() function
@repeat(num_times=3)
def greet(name):
    return f"Hello, {name}!"

# Call the decorated function
print(greet("Alice"))
''',

            '''# Chaining Multiple Decorators
def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result + "!"
        return modified_result
    return wrapper

# Apply multiple decorators to the greet() function
@exclamation_decorator
@uppercase_decorator
def greet():
    return "hello"

# Call the decorated function
print(greet())  # Output: "HELLO!"
'''
        ]
        super().__init__(examples)

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")

class FunctionMenu(SubMenu):
    def __init__(self):
        examples = [
            '''# Function with Default Parameters
def greet(name="Guest"):
    return f"Hello, {name}!"

# Call the function without arguments
print(greet())  # Output: "Hello, Guest!"

# Call the function with an argument
print(greet("Alice"))  # Output: "Hello, Alice!"
''',

            '''# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 5
result = factorial(5)
print("Factorial of 5:", result)  # Output: 120
''',

            '''# Lambda Functions
# Define a lambda function to square a number
square = lambda x: x**2

# Use the lambda function
print(square(5))  # Output: 25

# Lambda function as an argument in a higher-order function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
''',

            '''# Example 4: Closure
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create closures with different values of x
closure1 = outer_function(10)
closure2 = outer_function(20)

print(closure1(5))  # Output: 15
print(closure2(5))  # Output: 25
'''
        ]
        super().__init__(examples)
    
    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")


class ListandTuplesMenu(SubMenu):
    def __init__(self):
        examples = [
            '''#  List Comprehension
# Generate a list of even numbers from 1 to 10
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]''',

            '''# Tuple Unpacking
# Define a tuple
person = ('John', 30, 'Engineer')

# Unpack the tuple into variables
name, age, profession = person

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
''',

            '''#  List Concatenation and Slicing
# Create two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate the two lists
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Get a sublist using slicing
sublist = concatenated_list[2:5]
print(sublist)  # Output: [3, 4, 5]
'''
        ]
        super().__init__(examples)
        
    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")



class DictionaryMenu(SubMenu):
    def __init__(self):
        examples = [
            '''# Example 1: Creating a Dictionary
# Using curly braces and key-value pairs
person = {
    'name': 'John',
    'age': 30,
    'occupation': 'Engineer'
}

# Using dict() constructor with keyword arguments
person = dict(name='John', age=30, occupation='Engineer')

print(person)  # Output: {'name': 'John', 'age': 30, 'occupation': 'Engineer'}
''',

            '''# Example 2: Dictionary Comprehension
# Create a dictionary of squares from 1 to 5
squares = {num: num**2 for num in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
''',

            '''# Example 3: Merging Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Using the update() method
merged_dict = dict1.copy()
merged_dict.update(dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using dictionary unpacking in Python 3.9+
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
''',

            '''# Example 4: Iterating Over a Dictionary
person = {
    'name': 'John',
    'age': 30,
    'occupation': 'Engineer'
}

# Iterate over keys
print("Keys:")
for key in person:
    print(key)

# Iterate over values
print("\nValues:")
for value in person.values():
    print(value)

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in person.items():
    print(key, ":", value)
'''
        ]
        super().__init__(examples)

    def display(self):
        print("=== Sub Menu ===")
        for i, example in enumerate(self.examples, 1):
            print(f"{i}. Example {i}")
        print("-1. Back")

    def run(self):
        while True:
            self.display()
            choice = input("Enter your choice: ")

            if choice == '-1':
                break

            if choice.isdigit() and int(choice) <= len(self.examples):
                example_code = self.examples[int(choice) - 1]
                print(f"Running Example {int(choice)}:")
                print(example_code)
                exec(example_code)
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")

if __name__ == '__main__':
    main_menu = MainMenu()
    main_menu.run()
