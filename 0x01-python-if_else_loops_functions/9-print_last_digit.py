def print_last_digit(number):
    lastNumber = abs(number) % 10
    print("{}".format(lastNumber), end="")
    return lastNumber
