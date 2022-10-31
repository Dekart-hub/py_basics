import re

while True:
    url = input()
    res = re.fullmatch(r"(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/.+", url)
    if res:
        print("Correct")
    else:
        print("Incorrect")