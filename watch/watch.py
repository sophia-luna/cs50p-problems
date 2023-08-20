import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches:=re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w{11})\"", s):
        s="https://youtu.be/"+matches.group(1)
        return s
    return "None"


if __name__ == "__main__":
    main()