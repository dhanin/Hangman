sentence = input()
sentence = sentence.replace("!", "").replace(".", "").replace(",", "").replace("?", "")
print(sentence.lower())