import requests
from bs4 import BeautifulSoup

URL = "https://dining.unc.edu/locations/chase/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="c-tab__content")
menu_stations = results.find_all("div", class_="menu-station")

for station in menu_stations:
    station_name = station.find("h4", class_="toggle-menu-station-data")
    print(f"\n\n{station_name.text.strip()}:\n")
    menu_items = station.find("ul")
    for item in menu_items.find_all("li"):
        print(item.text.strip())