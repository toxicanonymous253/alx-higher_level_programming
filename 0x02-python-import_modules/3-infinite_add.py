#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            result = int(sys.argv[i])
            sum += result
        print("{:d}".format(sum))
    else:
        print("{}".format(sum))
