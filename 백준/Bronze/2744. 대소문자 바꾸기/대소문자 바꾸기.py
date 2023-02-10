text = input()
char = ""
for i in range(len(text)):
    if(text[i].isupper()):
        char += text[i].lower()
    else:
        char += text[i].upper()
print(char)