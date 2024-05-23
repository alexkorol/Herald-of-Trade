from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape_character_urls(list_urls):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    character_urls = []

    for url in list_urls:
        driver.get(url)
        time.sleep(5)  # Allow time for the page to load

        while True:
            try:
                # Scrape all character links on the current page
                char_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/character/")]')
                for link in char_links:
                    char_url = link.get_attribute('href')
                    if char_url not in character_urls:
                        character_urls.append(char_url)

                # Find and click the 'next page' button if it exists
                next_page_button = driver.find_elements(By.XPATH, '//button[contains(text(), "Next")]')
                if next_page_button:
                    next_page_button[0].click()
                    time.sleep(5)  # Allow time for the page to load
                else:
                    break
            except Exception as e:
                print(f"Error: {e}")
                break  # Break the loop if any error occurs

    driver.quit()

    # Save the character URLs to a CSV file
    df = pd.DataFrame(character_urls, columns=['Character_URL'])
    df.to_csv('character_urls.csv', index=False)

if __name__ == "__main__":
    list_urls = [
        'https://poe.ninja/builds/necropolis?items=The+Adorned&min-ehp=50000&min-depth=1000&sort=ehp',
        'https://poe.ninja/builds/necropolis?items=The+Adorned&type=depthsolo&class=Necromancer&min-ehp=50000&min-depth=1000&sort=dps',
        'https://poe.ninja/builds/necropolis?items=The+Adorned&type=depthsolo&class=Trickster&min-ehp=50000&min-depth=1000&sort=dps',
        'https://poe.ninja/builds/necropolis?items=The+Adorned&type=depthsolo&class=Pathfinder&min-ehp=50000&min-depth=1000&sort=dps',
        'https://poe.ninja/builds/necropolis?items=The+Adorned&type=depthsolo&class=Chieftain&min-ehp=50000&min-depth=1000&sort=dps',
        'https://poe.ninja/builds/necropolis?items=The+Adorned&type=depthsolo&class=Inquisitor&min-ehp=50000&min-depth=1000&sort=dps',
        'https://poe.ninja/builds/necropolis?items=The+Adorned&type=depthsolo&class=Hierophant&min-ehp=50000&min-depth=1000&sort=dps'
    ]
    scrape_character_urls(list_urls)
