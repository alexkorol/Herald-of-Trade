import pandas as pd
import re

# Load the decoded character data
decoded_data_path = 'decoded_character_data.csv'
decoded_data = pd.read_csv(decoded_data_path)

def extract_jewel_info(xml_data):
    jewel_pattern = re.compile(r'<Item id=.*?Rarity: (MAGIC|UNIQUE)\n(.*?)\nUnique ID: (.*?)\n(.*?)</Item>', re.DOTALL)
    matches = jewel_pattern.findall(xml_data)
    
    jewels = []
    for match in matches:
        rarity, name, unique_id, details = match
        if 'Jewel' in name:
            jewel_info = {
                "Rarity": rarity,
                "Name": name.strip(),
                "Unique ID": unique_id.strip(),
                "Details": details.strip()
            }
            jewels.append(jewel_info)
    
    return jewels

# Process each character's decoded data
all_jewels = []
for index, xml_data in decoded_data['Decoded_Data'].items():
    try:
        print(f"Processing character {index}")
        jewels = extract_jewel_info(xml_data)
        print(f"Extracted jewels: {jewels}")
        if jewels:
            all_jewels.extend(jewels)
        else:
            print(f"No jewels found in character {index}")
    except Exception as e:
        print(f"Error processing character {index}: {e}")

# Convert the list of jewels to a DataFrame
jewel_df = pd.DataFrame(all_jewels)

# Save the DataFrame to a CSV file
output_path = 'extracted_jewels.csv'
jewel_df.to_csv(output_path, index=False)
print(f"Extracted jewel information saved to {output_path}")

# Additional debug: print first few lines of the DataFrame
print(jewel_df.head())