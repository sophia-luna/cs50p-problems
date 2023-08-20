from datetime import date
from datetime import timedelta
import sys
import re
import inflect

def main():
    s=input("Date of Birth: ")
    min=int(minutes(s))
    p=inflect.engine()
    number=p.number_to_words(min)
    number=number.strip().capitalize().replace("and ", "")
    print(f"{number} minutes")

def minutes(s):
    try:
        if re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s):
            bday=date.fromisoformat(s)
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")
    else:
        today=date.today()
        dif=today-bday
        sec=dif.total_seconds()
        min=sec/60
        return min



if __name__ == "__main__":
    main()