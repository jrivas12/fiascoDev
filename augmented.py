# Augmented assignment evaluation of a phrase using map
phrase = "Hello, world! I hope you are doing good!"
word_lengths = []

# Using map and augmented assignment to compute word lengths
word_lengths += map(len, phrase.split())

# Print the word lengths
print(word_lengths)