string = input()
for ch in string:
    if not ch.isalpha():
        break
    else:
        print("vowel") if ch in "aeiou" else print("consonant")
