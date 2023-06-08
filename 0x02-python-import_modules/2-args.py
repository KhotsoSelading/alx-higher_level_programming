#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    iCounter = len(sys.argv) - 1
    if iCounter == 0:
        print("0 arguments.")
    elif iCounter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(iCounter))
    for i in range(iCounter):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
