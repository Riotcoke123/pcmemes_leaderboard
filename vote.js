// Import required modules
const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

// Function to fetch and scrape post data from a URL
async function getPostData(url) {
    const headers = {
        'Authorization': 'uVQuT5zBpHnSaJpmJkKolramkwIUCTX4pAuYTUK4SnrCngk5Lp-w1QjMfLSskQrv-ljbRwUN6af40g8mH0XA8j0BYxmdxxTQgCF3GfKh6ucXd-v9LBYdvd4_D45sABHN'
    };

    try {
        const { data } = await axios.get(url, { headers });
        const $ = cheerio.load(data);

        const posts = [];

        $('.card').each((i, element) => {
            const postData = {};

            // Scrape voting element
            const votingElement = $(element).find('.voting.my-2.d-none.d-md-flex.pr-2');

            if (votingElement.length) {
                // Scrape upvotes
                const upvotesText = votingElement.find('.post--up').text().trim();
                const upvotes = upvotesText && !isNaN(upvotesText) ? parseInt(upvotesText) : 0;
                const upvoteScore = upvotes * 0.0023547;

                // Scrape downvotes
                const downvotesText = votingElement.find('.post--down').text().trim();
                const downvotes = downvotesText && !isNaN(downvotesText) ? parseInt(downvotesText) : 0;
                const downvotePenalty = downvotes * 0.01234;

                // Calculate combined score
                const score = upvoteScore - downvotePenalty;
                postData.score = score;
            }

            // Scrape username
            const usernameElement = $(element).find('div.card-block.text-left.x-scroll-parent.w-100 > div > div > a > span');
            const username = usernameElement.text().trim();
            postData.username = username;

            posts.push(postData);
        });

        return posts;

    } catch (error) {
        console.error(`Error fetching data from ${url}:`, error);
        return [];
    }
}

// Function to sort posts by score
function sortPostsByScore(posts) {
    return posts.sort((a, b) => b.score - a.score);
}

// Function to add ranking to posts
function addRanking(posts) {
    posts.forEach((post, index) => {
        post.rank = index + 1;
    });
}

// Function to save usernames and scores to JSON file
function saveToJson(posts) {
    // Remove duplicate usernames
    const uniquePosts = posts.filter((post, index, self) =>
        index === self.findIndex(p => p.username === post.username)
    );

    const usernamesAndScores = uniquePosts.map(post => {
        return {
            username: post.username,
            score: post.score,
            rank: post.rank
        };
    });

    const filePath = path.join('C:\\', 'Users', 'srrm4', 'OneDrive', 'Desktop', 'all.json');
    fs.writeFile(filePath, JSON.stringify(usernamesAndScores, null, 4), (err) => {
        if (err) {
            console.error('Error saving usernames and scores to JSON file:', err);
        } else {
            console.log(`Usernames, scores, and ranks saved to ${filePath}`);
        }
    });
}

// Main function to handle the scraping and saving of data
async function main() {
    const urls = [
        { url: 'https://pcmemes.net/?ccmode=&sort=hot&t=day' },
        { url: 'https://pcmemes.net/?ccmode=&sort=new&t=day' }
    ];

    let allPosts = [];

    for (const { url } of urls) {
        const posts = await getPostData(url);
        allPosts = allPosts.concat(posts);
        await sleep(1000);  // Sleep for 1 second to avoid rate limiting
    }

    const sortedPosts = sortPostsByScore(allPosts);
    addRanking(sortedPosts);
    saveToJson(sortedPosts);
}

// Sleep function
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Execute main function initially
main();

// Update every 120 seconds
setInterval(main, 120 * 1000); // 120 seconds