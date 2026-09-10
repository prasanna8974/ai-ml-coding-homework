def reverse_text(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text


word = input("Enter a word: ")

reversed_word = reverse_text(word)

if word.lower() == reversed_word.lower():
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")