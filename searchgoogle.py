#! python3
# searchgoogle.py - Opens top search results from Google 

import requests, bs4, webbrowser

def main():
    search_phrase = input('What do you want to search?\n')
    soup = get_html_soup(search_phrase)
    result_urls = get_result_urls(soup)
    
    for i in range(5): # Open browser for top 5 results
        open_browser(result_urls[i])


# Make soup from main Google search page
def get_html_soup(search_phrase: str):
    res = requests.get('https://www.google.com/search?q=' + search_phrase)
    res.raise_for_status()
    print('Searching... ')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    return soup


# Get result page url
def get_result_urls(soup: bs4.BeautifulSoup):
    result_links = soup.find_all('h3')
    result_urls = []
    for result_link in result_links:
        result = result_link.find_next_sibling("div")
        if result and ('youtube' not in result):   # ignore youtube links because they don't work
            result_url = result.text.replace(' › ', '/')
            result_urls.append(result_url)
    return result_urls


# Open a browser tab for each result url
def open_browser(result_url: str):
    print('Opening', result_url)
    webbrowser.open(result_url)

if __name__ == "__main__":
    main()
