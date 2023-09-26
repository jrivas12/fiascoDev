import sys

def main():
 
  with open("search.txt") as file:
    words = file.read().split()

  # Loop until the user says they are done.
  done = False
  while not done:

    # Prompt the user for a word to find.
    search_word = input("Enter a word to find: ")

    # Count the number of occurrences of the search word.
    count = words.count(search_word)

    # Calculate the percentage of the search word in the file.
    percentage = count / len(words) * 100

    # Print the statistics.
    print(search_word, "appears", count, "times in the file. This is", percentage, "% of the total words.")

    # Prompt the user for the next word.
    next_word = input("Enter the next word: ")

    # Check if the two words are next to each other.
    found = False
    for i in range(len(words) - 1):
      if words[i] == search_word and words[i + 1] == next_word:
        found = True
        break

    # If the two words are next to each other, print the statistics.
    if found:
      print("The words '", search_word, "' and '", next_word, "' appear together", count, "times in the file. This is", percentage, "% of the total words.")

    # Prompt the user if they are done.
    done = input("Are you done? (y/n) ") == "y"

if __name__ == "__main__":
  main()
