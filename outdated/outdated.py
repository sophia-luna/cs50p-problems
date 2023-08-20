months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

while True:
    try:
        date=input("Date: ").strip()
        if '/' in date:
            m,d,y=date.split('/')
            m=int(m)
            d=int(d)
            y=int(y)
        elif "," in date:
            m,d,y=date.split(' ')
            d=d.replace(',', '')
            if m in months:
                m=int(months[m])
            d=int(d)
            y=int(y)
        else:
            d=0
            m=0
    except (NameError, ValueError):
        pass
    else:
        if d>0 and d<=31 and m>0 and m<=12:
            break

print(f"{y:04}-{m:02}-{d:02}")