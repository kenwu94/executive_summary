import requests
from bs4 import BeautifulSoup
import re

def get_law_firms_with_keyword(keyword):
    url = "https://en.wikipedia.org/wiki/List_of_largest_law_firms_by_revenue"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the relevant table containing law firm information
    table = soup.find("table", class_="wikitable sortable")

    law_firms = []
    for row in table.find_all("tr")[1:]:  # Skip the header row
        columns = row.find_all("td")
        if len(columns) >= 2:
            rank = columns[0].text.strip()
            name = columns[1].text.strip()
            if keyword.lower() in name.lower():
                law_firms.append(name)

    return law_firms

def search_keyword_on_firm_website(firm_name, keyword):
    # Replace with the actual URL of the firm's website
    firm_website_url = "https://www.example.com"  # Replace with the actual URL

    try:
        # Fetch the content of the firm's website
        response = requests.get(firm_website_url)
        response.raise_for_status()

        # Check if the keyword is present in the website content
        if keyword.lower() in response.text.lower():
            print(f"The keyword '{keyword}' was found on {firm_name}'s website.")
        else:
            print(f"The keyword '{keyword}' was not found on {firm_name}'s website.")

    except requests.RequestException as e:
        print(f"Error during the request to {firm_website_url}: {e}")

if __name__ == "__main__":
    keyword = "ai"
    law_firms_list = get_law_firms_with_keyword(keyword)
    print(f"Law firms related to '{keyword}':")
    for i, firm in enumerate(law_firms_list[:20], start=1):
        print(f"{i}. {firm}")
        search_keyword_on_firm_website(firm, keyword)
