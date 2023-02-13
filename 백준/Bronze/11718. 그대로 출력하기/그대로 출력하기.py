import re

i=0
chars = ""
while(i < 100):
    try:
        char = ""
        char+=input()
        m = re.search('[^a-zA-Z0-9\\s]+',char)
        if(char[0] == " " or char[len(char)-1] == " " or len(char)>100 or m!=None):
            break
        chars+=char+"\n"
    except(EOFError):
        break
print(chars[:-1])

