# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(words)
temp = ''
for x in answer:
    temp += temp.join('-')
print('H A N G M A N')
print()
while True:
    option = input('Type "play" to play the game, "exit" to quit:')
    print()
    if option == "play":
        print(temp)
        break
    elif option == "exit":
        exit()
    else:
        pass
count = 0
answer = list(answer)
temp = list(temp)
answerSet = set(answer)
guessed = list()
while count < 8:
    ch = input("Input a letter:")
    guessed.append(ch)

    if len(ch) > 1:
        print("You should input a single letter")
        print()
        print(''.join(temp))
        continue
    if not ch.islower():
        print("Please enter a lowercase English letter")
        print()
        print(''.join(temp))
        continue
    if guessed.count(ch) > 1:
        print("You've already guessed this letter")
        if count >= 8:
            print("You lost!")
            print()
            go = True
            while go:
                k = input('Type "play" to play the game, "exit" to quit:')
                if k == "play":
                    count = 0;
                    for i in range(0, len(temp)):
                        temp[i] = '-'
                        i += 1
                        guessed = list()
                        go = False
                elif k == "exit":
                    exit()
                else:
                    pass
        else:
            print()
            print(''.join(temp))
        continue
    if ch not in answerSet:
        print("That letter doesn't appear in the word")
        count += 1
        if count >= 8:
            print("You lost!")
            print()
            go = True
            while go:
                k = input('Type "play" to play the game, "exit" to quit:')
                if k == "play":
                    count = 0
                    for i in range(0, len(temp)):
                        temp[i] = '-'
                        guessed = list()
                        i += 1
                    go = False
                elif k == "exit":
                    exit()
                else:
                    pass
        else:
            print()
            print(''.join(temp))
        continue
    if ch in answer:
        for i in range(0, len(answer)):
            if ch == answer[i]:
                temp[i] = ch
                i += 1
        if answer == temp:
            temp = ''.join(temp)
            print("You guessed the word {0}!".format(temp))
            print("You survived!")
            print()
            go = True
            while go:
                k = input('Type "play" to play the game, "exit" to quit:')
                if k == "play":
                    count = 0
                    for i in range(0, len(temp)):
                        temp[i] = '-'
                        guessed = list()
                        i += 1
                    go = False
                elif k == "exit":
                    exit()
                else:
                    pass
        else:
            print()
            print(''.join(temp))
        answerSet.remove(ch)

