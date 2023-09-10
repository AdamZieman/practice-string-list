# practice_string_list.py
# This program demonstrates the programmers understanding of manipulating strings and lists.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 8

# Author: Adam Zieman
# Date: April 22, 2021

def main():
    # User inputs a word with at minimum length of 8 characters
    userWord = input("Please type a word with at least 8 letters: ")

    # Indexing: print the third letter of the word
    print("Third letter:",userWord[2])

    # Store the length of the word
    wordLength = len(userWord)

    # Indexing: print the second-to-last letter of the word
    print("Second-to-Last letter:",userWord[-2])

    # Slicing: print the first 3 letters of the word
    print("First 3 letters:",userWord[:3])

    # Slicing: print the 3rd through 5th letters of the word (4 total)
    print("Letters 2,3,4 and 5:",userWord[2:6])

    # Slicing: print the last 3 letters of the word
    print("Last 3 letters:",userWord[wordLength - 3:])

    # Instantiate a list with the values [8,6,4,2,0]
    list1 = [8,6,4,2,0]

    # Instantiate a list with the values [8,6,4,2,0,1,3,5,7] by concatenating the first list with [1,3,5,7]
    list2 = list1 + [1,3,5,7]

    # Print the second list
    print(list2)

    # User inputs a string with spaces and duplicate letters
    userString = input("Enter a string with spaces and multiples of the letter e: ")

    # Split the string at the spaces and save a list of separate words in a new variable and then print it
    splitString = (userString.split())
    print("Seperate Words:",splitString)

    # Iterate through each word and print the first character of each word, seperating each word with an underscore
    for firstLetter in splitString:
        print(firstLetter[0]+"_",end='')

    print()

    # Split the string at every letter e
    print("Missing letter 'e':",
          userString.split('e'))

    # Print the sentence as a title
    print("Sentence as a title:",
          userString.title())

    # Count the number of letter e and print the count
    eCount = userString.count('e')
    print("Letter 'e' occurs in sentence:",eCount,"times.")

    # Replace every letter 'e' with its uppercase version 'E' and print
    print("version with uppercase letter:",
          userString.replace('e','E'))

    # Find the index of the first 'e' and print that number
    print("Letter 'e' first occurs at index",
          userString.find('e'))

    # Find the index of the last 'e' and print that number
    print("Letter 'e' last occurs at index",
          userString.rfind('e'))

main() # Calls the main() function
