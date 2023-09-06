from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from twilio.rest import Client


def main() -> None:
    # Initialize the Chrome driver and navigate to the initial page
    driver = webdriver.Chrome()
    driver.get("https://dining.unc.edu/locations/chase/")

    # Creating a Twilio client with my account sid and auth token
    account_sid = "account_sid"
    auth_token = "auth_token"
    client = Client(account_sid, auth_token)

    # Define a function to scrape the data and save it to a .txt file
    def scrape(dining_hall: str, meal: str, tab_id: int, write_mode: str) -> None:            
        element_present = True

        try:
            # Wait for up to 2 seconds for an <a> element with child div element with text "Breakfast (7am-9am)" to be present
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-tabid='0']")))
        except TimeoutException:
                element_present = False

        if element_present:
            with open(f"{dining_hall}.txt", f"{write_mode}") as f:
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
                            f.write(f"{item.text.strip()}\n")
        else:
            with open(f"{dining_hall}.txt", "w") as f:
                f.write(f"{dining_hall} is closed today.")
                print("Success")

    # Scrape Chase's breakfast data and write to a .txt file
    scrape("Chase", "Breakfast", "0", "w")

    # Scrape Chase's lunch data and append to a .txt file
    scrape("Chase", "Lunch", "1", "a")

    # Scrape Chase's dinner data and append to a .txt file
    scrape("Chase", "Dinner", "2", "a")

    # Quit the driver when finished
    driver.quit()

    # Open the .txt file and read the contents
    #with open("Chase.txt", "r") as f:
    #   file_contents = f.read()

    # Send test text message containing the file contents
    #message = client.messages.create(
    #    to="test_number",
    #    from_="twilio_number",
    #    body=file_contents)

    #print(f"Sent message: {message.sid}")


if __name__ == "__main__":
    main()