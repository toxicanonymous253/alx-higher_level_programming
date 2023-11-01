#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            #convert lowercase to upercase by minusing 32 from the ascii value
            uppercaseChar = chr(ord(char) - 32)
            result += uppercaseChar
        else:
            result += char
    print("{}".format(result))
