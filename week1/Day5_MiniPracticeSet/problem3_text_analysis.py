"""Write a Python program that asks the user to enter a sentence. Your program should:

Count the number of words
Count the number of vowels
Reverse the sentence
Use a function for counting vowels."""


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for character in text:
        if character in vowels:
            count += 1

    return count


text = input("Enter a sentence: ")

words = text.split()

print("Sentence:", text)
print("Number of words:", len(words))
print("Number of vowels:", count_vowels(text))
print("Reversed text:", text[::-1])