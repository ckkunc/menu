from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from twilio.rest import Client


def main() -> None:

    # Creating a Twilio client with my account sid and auth token
    account_sid = "account_sid"
    auth_token = "auth_token"
    client = Client(account_sid, auth_token)

    # Calls the function on both Lenoir and Chase. The button_mode dictionary has the button_id
    # and the mode to either write or add to a .txt file. So, the data from the breakfast button (id = 0)
    # should be written since it is the beginning of the data. But data from lunch (id = 1) is simply added 
    # to the existing file. 
    dining_halls = ["Lenoir", "Chase"]
    button_mode= {"0": "w", "1": "a", "2": "a"}
    for hall in dining_halls:
        for key in button_mode:
            scrape(hall, key, button_mode[key])

# Define a function to scrape the data and save it to a .txt file
def scrape(dining_hall: str, tab_id: int, write_mode: str) -> None:  

    # Initialize the Chrome driver and navigate to the initial page
    driver = webdriver.Chrome()
    if dining_hall == "Lenoir":
        driver.get("https://dining.unc.edu/locations/top-of-lenoir")
    else:
        driver.get("https://dining.unc.edu/locations/chase")

    element_present = True

    try:
        # Wait 1 second for the first button element to be located
        WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-tabid='0']")))
    except TimeoutException:
            element_present = False

    #If the first button exists, then the dining hall is open
    if element_present:
        with open(f"menus/{dining_hall}.txt", f"{write_mode}") as f:
            # Set the button as the css element with the equal tab_id
            try:
                button = driver.find_element(By.CSS_SELECTOR, f"a[data-tabid='{tab_id}']")
                button.click()
            # If the button doesn't exist, then return. This is especially useful if there is only a breakfast and dinner
            # menu for example. Then, the only tab_ids are 0 and 1, while there are usually 0, 1, and 2. This code fixes any
            # potential errors that could arise from that.
            except NoSuchElementException:
                print(f"Button with tab id {tab_id} not found")
                return

            # Write the active page's menu to the file, except for redundant stations such as Beverages
            soup = BeautifulSoup(driver.page_source, "html.parser")
            results = soup.find(class_="c-tab is-active")
            menu_stations = results.find_all("div", class_="menu-station")
            meal_element = soup.find("a", attrs={"data-tabid": tab_id})
            meal = meal_element.text.strip()
            meal = f"{dining_hall} {meal}"
            hyphen = "-"
            f.write(f"\n\n{hyphen:-^30}\n{meal}\n{hyphen:-^30}\n\n")
            for station in menu_stations:
                station_name = station.find("h4", class_="toggle-menu-station-data")
                station_name = station_name.text.strip()
                if (station_name != "Condiments and Spreads" and station_name != "Beverages" and station_name != "Salad Bar" and station_name != "Cereal" and station_name != "Soup and Salads"
                    and station_name != "Burritos & Bowls" and station_name != "Homemade Soups" and station_name != "The Grill" and station_name != "Stress Less Cabinet" and station_name != "Stress Less Freezer" and station_name != "Deli"):
                    f.write(f"\n-{station_name}-\n")
                    menu_items = station.find("ul")
                    for item in menu_items.find_all("li"):
                        f.write(f"{item.text.strip()}\n")
    #Else, the dining hall is closed
    else:
        with open(f"menus/{dining_hall}.txt", "w") as f:
            f.write(f"{dining_hall} is closed today.")
    # Quit the driver when finished
    driver.quit()



    # Open the .txt file and read the contents
    #with open("Chase.txt", "r") as f:
    #  file_contents = f.read()

    # Send test text message containing the file contents
    #message = client.messages.create(
    #    to="test_number",
    #    from_="twilio_number",
    #    body=file_contents)

    #print(f"Sent message: {message.sid}")


if __name__ == "__main__":
    main()
