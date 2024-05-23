# Utils for PoE Helper App

This folder contains utility scripts for tasks related to scraping, decoding, and extracting specific item information from Path of Exile character data.

## Folder Structure

These example scripts follow the workflow of researching most used corrupted magic jewel mods for crafting purposes, but can be adapted and modified to suit other goals. 

- scrape_lists.py - Scrapes lists of character URLs using Selenium.
- scrape_chars.py - Scrapes Path of Building (PoB) codes from character pages.
- decode_pobs.py - Decodes PoB codes into readable data.
- extract_items.py - Extracts information about jewels from decoded character data.

## Scripts

### scrape_lists.py

This script uses Selenium to scrape lists of character URLs from specified URLs.

#### Usage

1. Ensure Python and Selenium are installed.
2. Update the list_urls with URLs to scrape.
3. Run the script: python scrape_lists.py
   - Saves the URLs to character_urls.csv.

### scrape_chars.py

Scrapes Path of Building (PoB) codes from character pages obtained via scrape_lists.py.

#### Usage

1. Read character_urls.csv for URLs.
2. Run the script: python scrape_chars.py
   - Saves the PoB codes to character_codes.csv.

### decode_pobs.py

Decodes the PoB codes into readable data.

#### Usage

1. Read character_codes.csv for PoB codes.
2. Run the script: python decode_pobs.py
   - Outputs the decoded data to decoded_character_data.csv.

### extract_items.py

Extracts information about jewels from the decoded data provided by decode_pobs.py.

#### Usage

1. Read decoded_character_data.csv for decoded data.
2. Run the script: python extract_items.py
   - Saves the extracted jewel information to extracted_jewels.csv.
