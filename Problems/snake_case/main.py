string = list(input())
cap = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z'}
counter = 0
for char in string:
    if char in cap:
        string[counter] = chr(ord(string[counter]) + 32)
        if counter != 0:
            string.insert(counter, '_')
    counter += 1
print("".join(string))
