import requests
from bs4 import BeautifulSoup
import json

# Access token and Client ID
access_token = 'uVQuT5zBpHnSaJpmJkKolramkwIUCTX4pAuYTUK4SnrCngk5Lp-w1QjMfLSskQrv-ljbRwUN6af40g8mH0XA8j0BYxmdxxTQgCF3GfKh6ucXd-v9LBYdvd4_D45sABHN'
client_id = 'HD4kXXPjIlJ_VycPFS_4yI8q5CGq2uXSxEwUb4JuyTlK8qkCoWnLjnOc_0zL9Ffg'

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
    'Content-Type': 'application/json'
}

# CSS selectors
username_selector = 'a.user-name.text-decoration-none > span'
# Placeholder for correct upvote selector
upvote_selector = 'div.voting > div.post--up'  # Update this with the correct selector

# List to hold the scraped data
data = []

# Loop through each URL and scrape the data
for url in urls:
    response = requests.get(url, headers=headers)
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
        
        try:
            upvote_value = int(upvote_text) * 0.002222222
        except ValueError:
            upvote_value = 0

        # Debugging: Print each extracted username and upvote
        print(f"Username: {username_text}, Upvote: {upvote_value}")

        data.append({
            'username': username_text,
            'upvote': upvote_value
        })

# Sort the data by upvote in descending order
data.sort(key=lambda x: x['upvote'], reverse=True)

# Add ranking to the data
for index, item in enumerate(data):
    item['rank'] = index + 1

# Specify the path where the JSON file will be saved
file_path = 'C:\\Users\\srrm4\\OneDrive\\Desktop\\vote.json'

# Save the data to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)