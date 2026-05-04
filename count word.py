def count_words(sentence):
    words = sentence.split()
    return len(words)

# Example
text = input("Enter a sentence: ")
print("Word count:", count_words(text))
