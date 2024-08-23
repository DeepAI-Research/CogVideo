import json
import os
from tqdm import tqdm

def json_to_txt_files(json_file_path, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Check if the JSON is a list or a dictionary
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        items = [data]  # Wrap the dictionary in a list
    else:
        raise ValueError("JSON file must contain either a list or a dictionary.")

    # Process each item in the JSON
    for index, item in tqdm(enumerate(items), total=len(items)):
        # Create a filename based on the index
        filename = f"{index:05d}.txt"
        file_path = os.path.join(output_directory, filename)

        # Write the item content to a text file
        with open(file_path, 'w') as file:
            file.write(f"{item['caption']}\n")


    print(f"Created {len(items)} text files in {output_directory}")

if __name__ == "__main__":
    # Example usage
    json_file_path = "test.json"
    output_directory = "txt_files"

    json_to_txt_files(json_file_path, output_directory)