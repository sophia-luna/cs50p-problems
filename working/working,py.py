import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if matches:=re.search(r"^([0-9]{1,2})(?::(\d\d))? ([AP]M) to ([0-9]{1,2})(?::(\d\d))? ([AP]M)$", s):
            if matches.group(2) and matches.group(5):
                min1=int(matches.group(2))
                min2=int(matches.group(5))
                if min1>59 or min2>59:
                    raise ValueError

            start=int(matches.group(1))
            finish=int(matches.group(4))
            if start>12 or finish>12:
                raise ValueError
            if start==12 and matches.group(3)=="AM":
                start=0
            elif matches.group(3)=="PM" and start!=12:
                start+=12
            if finish==12 and matches.group(6)=="AM":
                finish=0
            elif matches.group(6)=="PM" and finish!=12:
                finish+=12

        else:
            raise ValueError
    except ValueError:
        raise ValueError
    else:
        if start<=9:
            start=f"0{start}"
        if finish<=9:
            finish=f"0{finish}"

        if matches.group(2) and matches.group(5):
            if min1<=9:
                min1=f"0{min1}"
            if min2<=9:
                min2=f"0{min2}"
            return f"{start}:{min1} to {finish}:{min2}"
        else:
            return f"{start}:00 to {finish}:00"




...


if __name__ == "__main__":
    main()