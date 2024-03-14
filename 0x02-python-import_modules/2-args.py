#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cnt = len(sys.argv) - 1
    if cnt > 1:
        rs = 'arguments:'
    elif cnt == 1:
        rs = 'argument:'
    else:
        rs = 'arguments.'

print(f"{cnt} {rs}")
for index, value in enumerate(sys.argv):
    if index != 0:
        print("{}: {}".format(index, value))
