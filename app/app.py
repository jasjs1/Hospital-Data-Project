import time
import os
import json

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

# Function to create a new hospital ID
def create_hospital_id():
    hospital_ID_Input = input("Input a six-digit numerical pin: ")
    hospital_Name_Input = input("Input your name: ")

    # Security question selection
    print("You can choose from one of the two security questions.")
    print("Press 1 for: 'What is the name of your first pet?'")
    print("Press 2 for: 'What is the name of your mother?'")

    question_choice = input("Enter your choice (1 or 2): ")

    if question_choice == "1":
        security_question = "What is the name of your first pet?"
    elif question_choice == "2":
        security_question = "What is the name of your mother?"
    else:
        print("Invalid choice. Defaulting to the first question.")
        security_question = "What is the name of your first pet?"

    security_answer = input(security_question + " ")

    return {
        "hospital_ID": hospital_ID_Input,
        "hospital_name": hospital_Name_Input,
        "security_question": security_question,
        "security_answer": security_answer,
    }

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
