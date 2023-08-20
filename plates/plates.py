def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if s[0].isnumeric() or s[1].isnumeric():
        return False
    for i in range(len(s)):
        if not(s[i].isalnum()):
            return False
        if s[i].isdigit() and i+1<len(s):
            if s[i+1].isalpha():
                return False
        if s[i]=='0' and s[i-1].isalpha():
            return False
    return True

main()