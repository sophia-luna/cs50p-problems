import emoji

s=input("Input: ")
if s.find('_')!=-1:
    output=emoji.emojize(s)
else:
    output=emoji.emojize(s,language='alias')
print(f"Output: {output}")