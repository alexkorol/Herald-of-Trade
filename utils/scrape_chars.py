import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_pob_codes(character_urls):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    codes = []

    for url in character_urls:
        try:
            driver.get(url)
            time.sleep(5)  # Allow time for the page to load

            # Find and click the 'copy code' button
            copy_code_button = driver.find_element(By.XPATH, '//div[@role="button" and contains(@class, "gap-1")]')
            copy_code_button.click()
            time.sleep(1)  # Allow time for the click event

            # Get the copied code from clipboard
            code = driver.execute_script("return navigator.clipboard.readText()")
            if code not in codes:  # Ensure we are not duplicating codes
                codes.append(code)
        except Exception as e:
            print(f"Error: {e}")

    driver.quit()

    # Save the codes to a CSV file
    df = pd.DataFrame(codes, columns=['POB_Code'])
    df.to_csv('character_codes.csv', index=False)

if __name__ == "__main__":
    # Read character URLs from CSV file
    character_urls_df = pd.read_csv('character_urls.csv')
    character_urls = character_urls_df['Character_URL'].tolist()
    
    scrape_pob_codes(character_urls)
