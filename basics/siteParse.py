import bs4
import requests

response = requests.get("https://yandex.ru/pogoda/")

tree = bs4.BeautifulSoup(response.text, "html.parser")

weather = tree.select('.forecast-briefly__day')[1:9]
for item in weather:
    day = item.select_one('.forecast-briefly__name').text
    date = item.select_one(".forecast-briefly__date").text
    temperature = item.select_one(".temp__value").text
    condition = item.select_one(".forecast-briefly__condition").text
    print(f"Погода на {day} {date}: {temperature}° {condition}")