import re

while True:
    url = input()
    result = re.fullmatch(r"(https?://)?((www\.)?youtube\.com|youtu\.be)/.+", url)
    if result:
        print("Correct")
    else:
        print("Incorrect")
