import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if matches:=re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        n1=int(matches.group(1))
        n2=int(matches.group(2))
        n3=int(matches.group(3))
        n4=int(matches.group(4))
        if n1<256 and n2<256 and n3<256 and n4<256:
            return True
    return False


if __name__ == "__main__":
    main()