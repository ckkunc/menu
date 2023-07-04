from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from twilio.rest import Client

def main() -> None:
    # Initialize the Chrome driver and navigate to the initial page
    driver = webdriver.Chrome()
    driver.get("https://dining.unc.edu/locations/chase/")

    # Creating a Twilio client with my account sid and auth token
    account_sid = "AC13510655afad85f11f7ac79578dc23c5"
    auth_token = "2cc46305cad37cc6ff00220e537424e3"
    client = Client(account_sid, auth_token)

    # Define a function to scrape the data and save it to a .txt file
    def scrape(dining_hall: str, meal: str, tab_id: int, write_mode: str) -> None:
    # Open a file in write mode
        with open(f"{dining_hall}.txt", f"{write_mode}") as f:
            # Extract the data using Beautiful Soup
            button = driver.find_element(By.CSS_SELECTOR, f"a[data-tabid='{tab_id}']")
            button.click()
            
            time.sleep(1)

            # Write the active page's menu to the file, except for redundant stations such as Beverages
            soup = BeautifulSoup(driver.page_source, "html.parser")
            results = soup.find(class_="c-tab is-active")
            menu_stations = results.find_all("div", class_="menu-station")
            meal = f"{dining_hall} {meal}"
            f.write(f"\n{meal:_^60}\n")
            for station in menu_stations:
                station_name = station.find("h4", class_="toggle-menu-station-data")
                station_name = station_name.text.strip()
                if station_name != "Condiments and Spreads" and station_name != "Beverages" and station_name != "Salad Bar" and station_name != "Cereal" and station_name != "Soup and Salads":
                    f.write(f"\n\n-{station_name}-\n")
                    menu_items = station.find("ul")
                    for item in menu_items.find_all("li"):
                        f.write(item.text.strip() + "\n")


    # Scrape Chase's breakfast data and write to a .txt file
    scrape("Chase", "Breakfast", "0", "w")

    # Scrape Chase's lunch data and append to a .txt file
    scrape("Chase", "Lunch", "1", "a")

    # Scrape Chase's dinner data and append to a .txt file
    scrape("Chase", "Dinner", "2", "a")

    # Quit the driver when finished
    driver.quit()

    # Open the .txt file and read the contents



if __name__ == "__main__":
    main()
