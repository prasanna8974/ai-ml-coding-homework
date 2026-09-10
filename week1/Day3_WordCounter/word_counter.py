sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))

print("Word lengths:")

for word in words:
    print(word, ":", len(word))