def convert(x):
    x=x.replace(':)','🙂')
    x=x.replace(':(','🙁')
    return x

def main():
    emoticon=input()
    emoticon=convert(emoticon)
    print(emoticon)

main()