letters = ['A', 'B', 'C']
numbers = [1, 2, 3]

combined_list = [item for pair in zip(letters, numbers) for item in pair] + letters[len(numbers):] + numbers[len(letters):]

print(combined_list)
