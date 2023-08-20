import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums=re.findall(r"(?:\W|^)(um)(?:\W|$)", s, re.IGNORECASE)
    i=0
    for um in ums:
        i+=1
    return i



if __name__ == "__main__":
    main()