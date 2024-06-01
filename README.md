<!DOCTYPE html>
<html lang="en">

<body>
    <h1>pcmemes.net leaderboard</h1>
    <img src="https://github.com/Riotcoke123/pcmemes_leaderboard/assets/63672863/1bf6daf3-afbe-456d-b607-b2ae5bb6dce9" alt="pcmemes.net leaderboard image">
   
    
    
# pcmemes.net Leaderboard

This project is designed to scrape upvote data and usernames from pcmemes.net, rank the users based on their upvotes, and save the data to a JSON file every 3 minutes. The project is currently in beta testing.

## Features

- Scrapes multiple pages from pcmemes.net
- Extracts usernames and upvote data
- Ranks users based on upvote scores
- Saves the ranked data to a JSON file every 3 minutes

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Riotcoke123/pcmemes_leaderboard.git
    cd pcmemes_leaderboard
    ```

2. **Install the required libraries**:
    ```sh
    pip install requests beautifulsoup4
    ```

3. **Update Access Token and Client ID**:
    Open the `scrape.py` file and update the `access_token` and `client_id` variables with your own credentials.

4. **Run the scraper**:
    ```sh
    python scrape.py
    ```

</body>
</html>
