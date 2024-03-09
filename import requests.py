import requests
from bs4 import BeautifulSoup

def get_google_results(query, num_results=10):
    results = []
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for result in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
            result_text = result.get_text(strip=True)
            results.append(result_text)
            if len(results) == num_results:
                break

    return results

def extract_social_media_links(company_name):
    social_media_links = []
    social_media_query = f"{company_name} social media"

    # Get links from Google search
    links = get_google_results(social_media_query, num_results=5)

    for link in links:
        # Extract social media links from the search results
        if "twitter.com" in link or "linkedin.com" in link or "facebook.com" in link or "instagram.com" in link:
            social_media_links.append(link)

    return social_media_links

def scrape_companies_interested_in_smm(keyword, num_results=50):
    # Define the search query
    search_query = f"{keyword} companies interested in small language models"

    # Get company names from Google search results
    company_names = get_google_results(search_query, num_results=num_results)

    # Print the company names and their social media links
    print("Found companies interested in small language models:")
    for company_name in company_names:
        print(f"Company Name: {company_name}")
        
        # Extract and print social media links
        social_media_links = extract_social_media_links(company_name)
        if social_media_links:
            print("Social Media Links:")
            for social_media_link in social_media_links:
                print(social_media_link)
        else:
            print("No social media links found.")
        
        print("=" * 50)

if __name__ == "__main__":
    # Specify the keyword related to small language models
    keyword = "small language"

    # Scrape company names and social media links interested in small language models
    scrape_companies_interested_in_smm(keyword)
