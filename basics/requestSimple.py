import requests
import json
import re


while True:
    query = input()
    if not re.fullmatch(
            r"(?:\b|^)((?:(?:(?:\d)|(?:\d{2})|(?:1\d{2})|(?:2[0-4]\d)|(?:25[0-5]))\.){3}(?:(?:(?:\d)|(?:\d{2})|(?:1\d{2})|(?:2[0-4]\d)|(?:25[0-5]))))(?:\b|$)",
            query
                    ):
        print("Неверный IP")
        continue
    response = requests.get("http://ip-api.com/json/" + query)
    print("http://ip-api.com/json/" + query)
    if response.status_code == 200:
        response_content = json.loads(response.text)
        print(response_content['country'])
    else:
        print("Таĸого IP не существует")