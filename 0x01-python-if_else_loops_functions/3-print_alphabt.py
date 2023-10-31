#!/usr/bin/python3
alphabet = ""
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) != 'q' and chr(letter) != 'e':
        alphabet += chr(letter)
print(alphabet, end="")
