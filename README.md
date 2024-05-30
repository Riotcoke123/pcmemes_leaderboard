<!DOCTYPE html>
<html lang="en">

<body>
    <h1>pcmemes.net leaderboard</h1>
    <img src="https://github.com/Riotcoke123/pcmemes_leaderboard/assets/63672863/1bf6daf3-afbe-456d-b607-b2ae5bb6dce9" alt="pcmemes.net leaderboard image">
    <p><strong>NOTE:</strong> This project is currently in beta testing.</p>
    <h2>Installation and Usage</h2>
    <h3>Introduction</h3>
    <p>This script is designed to scrape post data from a website and save it to a JSON file. It utilizes Node.js and several npm packages for web scraping and file handling.</p>
    <h3>Prerequisites</h3>
    <ul>
        <li>Node.js installed on your machine. You can download it from <a href="https://nodejs.org/">nodejs.org</a>.</li>
    </ul>
    <h3>Installation</h3>
    <ol>
        <li>Clone or download the repository to your local machine.</li>
        <li>Navigate to the project directory in your terminal.</li>
    </ol>
    <h3>Setup</h3>
    <ol>
        <li>Install the required npm packages by running the following command:
            <pre>npm install</pre>
        </li>
    </ol>
    <h3>Usage</h3>
    <ol>
        <li>Open the <code>vote.js</code> file in a text editor.</li>
        <li>Update the <code>urls</code> array with the URLs you want to scrape data from.</li>
        <li>Run the script using the following command:
            <pre>node vote.js</pre>
        </li>
        <li>The script will scrape data from the provided URLs, remove duplicate usernames, sort posts by score, add ranking, and save the usernames, scores, and ranks to a JSON file located at <code>all.json</code>.</li>
    </ol>
    <h3>Automating Updates</h3>
    <p>You can automate the script to update data periodically by modifying the <code>setInterval</code> function call at the end of the <code>vote.js</code> file. By default, it updates every 3 minutes.</p>
    <h3>Notes</h3>
    <ul>
        <li>Make sure to adjust file paths and URLs according to your environment and requirements.</li>
        <li>Ensure that you have proper authorization to scrape data from the provided URLs.</li>
    </ul>
</body>
</html>
