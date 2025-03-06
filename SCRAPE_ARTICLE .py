# Python script to scrape an article given the url of the article and store the extracted text in a file
# Url: https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7

import os #create folder and save files
import requests # helps fetch web pages from internet
import re #to clean up the extracted text

from bs4 import BeautifulSoup #to extract meaningful content from webpage


# function to get the html source text of the medium article
def get_page():
    global url

    #Ask the user to input "Enter url of a medium article: " and collect it in url
    url = input("Enter url of a medium article: ")

    # handling possible error (checks if user has entered valid medium article url)
    if not re.match(r'https?://medium.com/', url):
        print('Please enter a valid website, or make sure it is a medium article')
        sys.exit(1)

    # Call get method in requests object, pass url and collect it in res
    res = requests.get(url) #script downloads the article using it

    res.raise_for_status() #If the page doesn’t exist or has issues,it stops program
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


# function to remove all the html tags and replace some with specific strings
def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>": "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text


def collect_text(soup):
    text = f'url: {url}\n\n'
    para_text = soup.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        text += f"{para.text}\n\n"
    return text


# function to save file in the current directory
def save_file(text):
    if not os.path.exists('./SCRAPED'):
        os.mkdir('./SCRAPED')
    name = url.split("/")[-1]
    print(name)
    fname = f'SCRAPED/{name}.txt'

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f'File saved in directory {fname}')


if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)
# Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7