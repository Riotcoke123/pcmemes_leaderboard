import requests
from bs4 import BeautifulSoup
import json
import time
import re

# Access token and Client ID
access_token = ''
client_id = ''

# List of URLs to scrape
urls = [
    "https://pcmemes.net/",
    "https://pcmemes.net/?ccmode=&sort=top&t=day",
    "https://pcmemes.net/?ccmode=&sort=bottom&t=day",
    "https://pcmemes.net/?ccmode=&sort=new&t=day",
    "https://pcmemes.net/?ccmode=&sort=hot&t=day"
]

# Headers for the request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Client-ID': client_id,
    'Content-Type': 'application/json',
    'X-Author': 'PCMEMES.NET leaderboard by riotcoke'
}

# CSS selectors
username_selector = 'a.user-name.text-decoration-none > span'
upvote_selector = 'div.d-flex.flex-row-reverse.flex-md-row.flex-nowrap div.voting.my-2.d-none.d-md-flex.pr-2'

# File path to save JSON data
file_path = '\vote.json'

def scrape_and_save():
    # Dictionary to hold the scraped data
    data_dict = {}

    # Loop through each URL and scrape the data
    for url in urls:
        response = requests.get(url, headers=headers)
        
        # Handle rate limiting (status code 429)
        if response.status_code == 429:
            print(f"Rate limit exceeded for {url}. Sleeping for 60 seconds.")
            time.sleep(60)
            response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Debugging: Print the response status and URL
            print(f"Scraping {url} - Status Code: {response.status_code}")

            usernames = soup.select(username_selector)
            upvotes = soup.select(upvote_selector)

            # Debugging: Check if selectors are capturing any data
            print(f"Found {len(usernames)} usernames and {len(upvotes)} upvotes")

            for username, upvote in zip(usernames, upvotes):
                username_text = username.get_text().strip()
                upvote_text = upvote.get_text().strip()

                # Debugging: Print raw upvote text to understand its format
                print(f"Raw upvote text: {upvote_text}")

                # Extract the number of upvotes using regular expressions
                match = re.search(r'(-?\d+)', upvote_text)  # Allow for negative numbers
                if match:
                    upvote_number = int(match.group(1))
                else:
                    upvote_number = 0

                # Sum upvotes for each username
                if username_text in data_dict:
                    data_dict[username_text] += upvote_number
                else:
                    data_dict[username_text] = upvote_number

        else:
            print(f"Failed to scrape {url} - Status Code: {response.status_code}")

    # Apply the 4.258% multiplier to the summed upvotes
    for username in data_dict:
        data_dict[username] *= 0.04258

    # Convert the dictionary to a list of dictionaries and sort the data by score in descending order
    data = [{'username': k, 'score': v} for k, v in data_dict.items()]
    data.sort(key=lambda x: x['score'], reverse=True)

    # Add ranking to the data
    for index, item in enumerate(data):
        item['rank'] = index + 1

    # Save the data to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    # Debugging: Print the final sorted and ranked data
    print(json.dumps(data, indent=4))

# Loop to run the script every 3 minutes
while True:
    scrape_and_save()
    print("Data scraped and saved. Waiting for 3 minutes...")
    time.sleep(180)  # Sleep for 3 minutes
