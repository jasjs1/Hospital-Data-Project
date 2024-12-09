import time
import os
import json

import os

def clear_Terminal_Upon_Start():
    if os.name == "nt":
        os.system('cls')  
    else:
        os.system('clear') 
        
clear_Terminal_Upon_Start()


DATA_FILE = "hospital_data.json"

# Function to save data to a file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Function to load data from a file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return None


# Requesting ID information
def request_ID_info():
    # Check if hospital ID exists in the data file
    data = load_data()

    if data:
        print("Hospital ID already exists.")
        return True
    else:
        # No existing data, create new ID
        print("No existing ID found. Creating new ID...")
        new_data = create_hospital_id()
        save_data(new_data)
        print("New hospital ID saved successfully!")
        return True

# Handle input for help or other operations
user_input = input("Enter command: ")

if user_input == "!help":
    if request_ID_info():
        # If ID exists or is created, load and display the data
        data = load_data()
        print("Hospital Data:", data)
else:
    print("Printing...")
