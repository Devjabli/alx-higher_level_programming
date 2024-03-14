#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tl = 0
    for x in range(len(sys.argv) - 1):
        tl += int(sys.argv[x + 1])
    print("{}".format(tl))
