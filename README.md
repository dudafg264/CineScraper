# 100 Movies that You Must Watch


## Overview

This Python program scrapes a list of movies from an archived webpage that ranks the "100 Best Movies" from *Empire Online*. It extracts the movie titles and stores them in a text file. The program uses the following libraries:

- **requests**: To send an HTTP request and fetch the webpage.
- **BeautifulSoup**: To parse the HTML content of the webpage and extract movie titles.

## Features

- Fetches a list of movie titles from the specified URL.
- Extracts titles from `h3` HTML tags with the class `title`.
- Saves the extracted movie titles in a text file called `100 movies.txt` in reverse order (from the last to the first movie).

## Requirements

To run this program, you need Python installed along with the following libraries:

- **requests**
- **beautifulsoup4**

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4
```

## How to Use

1. Download or clone this repository to your local machine.
2. Make sure you have the required Python libraries installed (see Requirements section).
3. Run the script:

```bash
python movie_scraper.py
```

4. After execution, the movie titles will be saved in a file called `100 movies.txt`. Each movie title will appear on a new line, listed from the 1st to the 100th movie.

## Code Walkthrough

- **URL**: The program begins by setting the `URL` variable to the link of the archived webpage containing the movie list.
  
- **requests.get**: The program sends an HTTP request to the URL using the `requests` library to fetch the content of the page.
  
- **BeautifulSoup**: The HTML content is parsed using `BeautifulSoup` to search for all `h3` tags with the class `title`, which contains the movie titles.

- **Appending Titles**: The program iterates through all the found movie titles, extracts the text, and appends it to a list called `movies`.

- **Saving Data**: Finally, the program saves the movie titles in reverse order (from last to first) to a text file named `100 movies.txt`.

## Output

After running the program, you'll find a text file `100 movies.txt` with the following content:

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
... and so on
```

## Notes

- This program is designed to scrape the specific archived webpage provided in the URL. If the structure of the page changes, the program may need to be updated to correctly extract the data.
- Ensure that the webpage you're scraping is publicly accessible and that you are compliant with any applicable terms of service when scraping content.

