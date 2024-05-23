import pandas as pd
import base64
import zlib
import json

# Decoding functions from decode_pob.py
def decode_base64(import_code):
    try:
        base64_decode = base64.urlsafe_b64decode(import_code)
        return base64_decode
    except (TypeError, ValueError) as e:
        print(f"Base64 decoding error: {e}")
        return None

def decompress_data(compressed_data):
    try:
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data.decode('utf-8')
    except zlib.error as e:
        print(f"Decompression error: {e}")
        return None

def decode_pob_code(encoded_str):
    # Decode base64
    decoded_bytes = decode_base64(encoded_str)
    if decoded_bytes is None:
        print("Failed to decode base64 for:", encoded_str)
        return None
    
    # Decompress data
    decompressed_str = decompress_data(decoded_bytes)
    if decompressed_str is None:
        print("Failed to decompress data for:", encoded_str)
        return None
    
    return decompressed_str

# Function to process POB codes and save decoded data
def process_pob_codes():
    # Read the CSV file with POB codes
    pob_codes = pd.read_csv('character_codes.csv')['POB_Code']
    decoded_data_list = []

    for index, code in enumerate(pob_codes):
        print(f"Processing code {index+1}/{len(pob_codes)}")
        decoded_data = decode_pob_code(code)
        if decoded_data is not None:
            decoded_data_list.append(decoded_data)
        else:
            print(f"Failed to decode POB code: {code}")

    # Save the decoded data to a CSV file
    df = pd.DataFrame(decoded_data_list, columns=['Decoded_Data'])
    df.to_csv('decoded_character_data.csv', index=False)

if __name__ == "__main__":
    process_pob_codes()