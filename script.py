import requests
from bs4 import BeautifulSoup

def get_html_page(url):
    response = requests.get(url)
    return response.text

def extract_ids(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Find all elements with an 'id' attribute
    ids = [element.get('id') for element in soup.find_all(id=True)]
    return ids

def save_ids_to_txt(ids, output_file):
    with open(output_file, 'w') as file:
        for _id in ids:
            file.write(_id + '\n')

def main():
    # Replace 'your_url_here' with the actual URL of the HTML page you want to scrape
    url = 'https://wordwarriors.wayne.edu/list'
    html_page = get_html_page(url)

    # Extract IDs from the HTML page
    ids = extract_ids(html_page)

    # Replace 'output.txt' with the desired output file name
    output_file = 'output2.txt'
    save_ids_to_txt(ids, output_file)

if __name__ == "__main__":
    main()