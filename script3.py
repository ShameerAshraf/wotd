import requests
from bs4 import BeautifulSoup
import json

def get_html_page(url):
    response = requests.get(url)
    return response.text

def extract_list_elements(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Find all list elements
    list_elements = soup.find_all('li')
    return list_elements

def create_json_object(list_elements):
    json_object = {}
    for element in list_elements:
        # Use the 'id' attribute as the key
        element_id = element.get('id')
        if element_id:
            # Create a dictionary with class names as keys and content as values
            class_content_dict = {class_name: content.strip() for class_name, content in zip(element['class'], element.stripped_strings)}
            # Store the dictionary under the key (id)
            json_object[element_id] = class_content_dict
    return json_object

def save_json_to_file(json_object, output_file):
    with open(output_file, 'w') as file:
        json.dump(json_object, file, indent=2)

def main():
    # Replace 'your_url_here' with the actual URL of the HTML page you want to scrape
    url = 'https://wordwarriors.wayne.edu/list'
    html_page = get_html_page(url)

    # Extract list elements from the HTML page
    list_elements = extract_list_elements(html_page)

    # Create a JSON object using the list elements
    json_object = create_json_object(list_elements)

    # Replace 'output.json' with the desired output file name
    output_file = 'output.json'
    save_json_to_file(json_object, output_file)

if __name__ == "__main__":
    main()