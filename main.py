import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def main() -> None:
    # Initialize the Chrome driver and navigate to the initial page
    driver = webdriver.Chrome()
    driver.get("https://dining.unc.edu/locations/chase/")

    # Define a function to scrape the data and print it out
    def scrape(meal: str, tab_id: int) -> None:
        # Extract the data using Beautiful Soup
        button = driver.find_element(By.CSS_SELECTOR, f"a[data-tabid='{tab_id}']")
        button.click()
        
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.find(class_="c-tab is-active")
        menu_stations = results.find_all("div", class_="menu-station")
        print(f"\n{meal:_^60}\n")
        for station in menu_stations:
            station_name = station.find("h4", class_="toggle-menu-station-data")
            print(f"\n\n{station_name.text.strip()}:\n")
            menu_items = station.find("ul")
            for item in menu_items.find_all("li"):
                print(item.text.strip())

    # Scrape the breakfast data
    scrape("Breakfast", "0")

    # Scrape the lunch data
    scrape("Lunch", "1")

    # Scrape the dinner data
    scrape("Dinner", "2")

    # Quit the driver when finished
    driver.quit()

if __name__ == "__main__":
    main()
