# download_comics.py - Downloads 50 comics from XKCD

import os
import urllib
from bs4 import BeautifulSoup


BASE_URL = 'https://xkcd.com/'

NUMBER_OF_COMICS = 50

def prompt_folder_path():
    while True:
        folder_path = input('\nEnter the absolute folder path to store the comics: \n')
        if os.path.exists(folder_path):
            os.chdir(folder_path)
            break
        else:
            print('\nInvalid link. Please enter the absolute path of to store the comics: \n')

# Create an HTML soup
def make_soup(url: str):
    request_page = urllib.request.urlopen(url)
    page_html = request_page.read()
    request_page.close()
    html_soup = BeautifulSoup(page_html, 'html.parser')
    return html_soup


# Find the URL of the comic image
def find_image_ulr(html_soup: BeautifulSoup):
    comic = html_soup.find(id='comic')
    comic_title = comic.findChild('img')['alt']
    comic_image_url = 'https://' + comic.findChild('img')['src'][2:]
    return comic_title, comic_image_url


# Download & save the image
def download_image(comic_title: str, comic_image_url: str):
    image_file_name = comic_title + '.png'
    try:
        urllib.request.urlretrieve(comic_image_url, image_file_name)
        print('Downloading: ' + comic_title + ' from ' + comic_image_url)
    except urllib.error.URLError as e:
        print(f'URLError: {e.reason}')

# Find url of the previous comic
def find_prev_page_url(html_soup: BeautifulSoup) :
    prev_comic = html_soup.find('a', rel='prev')
    prev_comic_url = BASE_URL + prev_comic['href']
    return prev_comic_url


def main():
    prompt_folder_path()

    url_to_scrape = BASE_URL

    for i in range(NUMBER_OF_COMICS):
        html_soup = make_soup(url_to_scrape)
        comic_title, comic_image_url = find_image_ulr(html_soup)
        download_image(comic_title, comic_image_url)
        url_to_scrape = find_prev_page_url(html_soup)

if __name__ == "__main__":
    main()
