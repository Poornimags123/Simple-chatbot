import re
import random
import json
def fetch_celebrity_data(celebrity_name):
    with open('Desktop/work/celebrities.json', 'r') as file:
        celebrities_data = json.load(file)

    celebrity_info = celebrities_data.get(celebrity_name)
    
    if celebrity_info:
        # Extract information using regular expressions
        date_of_birth = re.search(r'(\w+\s\d+,\s\d+)', celebrity_info["DateOfBirth"])
        age = celebrity_info["Age"]
        occupation = celebrity_info["Occupation"]
        nationality = celebrity_info["Nationality"]

        # Print the extracted information
        print(f'{celebrity_name} Information:')
        print(f'Date of Birth: {date_of_birth.group() if date_of_birth else "N/A"}')
        print(f'Age: {age}')
        print(f'Occupation: {occupation}')
        print(f'Nationality: {nationality}')
    else:
        print(f'Celebrity not found in the database.')
def main():
     print("Hello! I'm your celebrity information chatbot.\n")
     while True:
         user_input = input("Ask me about a celebrity, or type 'exit' to quit: ")
         if user_input.lower() == 'exit':
             print("Bye!Take care!Visit again!")
             break
             
         else:
             celebrity_name = user_input
             print("Here's what I found:")
             info = fetch_celebrity_data(celebrity_name)
             
if __name__ == "__main__":
    main()
