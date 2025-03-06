# Python Script for Scraping Medium Articles

## Purpose
I created this Python script to help me scrape the content of Medium articles, extract their text, and save it into a text file. It's a quick way for me to download articles for offline reading or for later use in other projects.

## Libraries Used
- **os**: This library is used to handle file and folder operations, like creating directories and saving files.
- **requests**: I use this to fetch the HTML content of the article from the URL.
- **re**: I use regular expressions here to clean up the text and remove unnecessary HTML tags.
- **BeautifulSoup** (from `bs4`): This is my go-to tool for parsing the HTML and extracting the meaningful content from the article.

## Functions

### `get_page()`
- **Description**: This function asks me to input the URL of a Medium article and then fetches the HTML content of the page.
- **How it works**:
  - I simply enter the URL of the Medium article when prompted.
  - The script checks if it's a valid Medium URL and fetches the HTML content.
  - It returns the parsed `BeautifulSoup` object, which I can use to extract the content.

### `clean(text)`
- **Description**: This function helps me clean up the text by removing unnecessary HTML tags and replacing certain tags with readable strings.
- **How it works**:
  - It replaces `<br>`, `<br/>`, and `<li>` tags with newline characters for better formatting.
  - It removes all other HTML tags using regular expressions, leaving me with only the readable content.

### `collect_text(soup)`
- **Description**: This function extracts the actual article text from the parsed HTML.
- **How it works**:
  - It finds all the `<p>` tags in the HTML, which contain the article's paragraphs.
  - It collects all of the text from these tags and concatenates them into a single string.
  - The article URL is added as a header so I know where the content came from.

### `save_file(text)`
- **Description**: This function saves the extracted text into a `.txt` file in a folder named `SCRAPED`.
- **How it works**:
  - It checks if the `SCRAPED` folder exists. If not, it creates one.
  - The script names the text file based on the article's URL.
  - Finally, it saves the text into that `.txt` file.

## Script Execution Flow
Here’s how the script works when I run it:
1. I enter the URL of the Medium article when prompted.
2. The script fetches the HTML content of the article and parses it.
3. It cleans up the content by removing unnecessary HTML tags.
4. The content is saved into a `.txt` file inside the `SCRAPED` folder.
5. Once everything is done, I see a confirmation message telling me the file has been saved.

## Example Usage

### Input:
When prompted, I enter the URL of a Medium article:
https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7

### Output:
The script will save a `.txt` file named `c5e5cc427c7.txt` in the `SCRAPED` folder, containing the full text of the article.
### In my case its papa-what-is-a-neural-network-c5e5cc427c7.txt


