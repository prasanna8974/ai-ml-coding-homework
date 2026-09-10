def string_length(text):
    return len(text)

def uppercase_text(text):
    return text.upper()

def lowercase_text(text):
    return text.lower()

def reverse_text(text):
    return text[::-1]

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"

    for character in text:
        if character in vowels:
            count += 1

    return count


text = input("Enter a string: ")

print("Length:", string_length(text))
print("Uppercase:", uppercase_text(text))
print("Lowercase:", lowercase_text(text))
print("Reverse:", reverse_text(text))
print("Vowel Count:", count_vowels(text))