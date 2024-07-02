import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_follower_count(company_url):
    """
    Scrape the follower count from the company Linkedin URL.
    """
    try:
        # Headers can be customized to mimic different browsers and operating systems
        # By default the generic one is used, visit 'https://user-agents.net/' for specific
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(company_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Convert the BeautifulSoup object to a string for easier text processing
        soup_string = str(soup)
        
        # Initialize followers as None
        followers = None
        # Find the index of the word 'followers' in the HTML string
        followers_index = soup_string.lower().find('followers')
        if followers_index != -1:
            # Extract a substring around the found index and filter digits to get the follower count
            start_index = max(0, followers_index - 20)
            followers_substring = soup_string[start_index:followers_index]
            followers = ''.join(filter(str.isdigit, followers_substring))
        
        return followers
    except requests.exceptions.RequestException as e:
        print(f"Request error for URL {company_url}: {e}")
        return None
    except AttributeError:
        print(f"Follower count not found for URL {company_url}")
        return None


def save_to_csv(data, file_path):
    """
    Save the data to a CSV file.
    """
    df = pd.DataFrame(data, columns=['company_name', 'company_url', 'follower_counts'])
    df.to_csv(file_path, index=False)


def main(input_csv, output_csv):
    # Read the input CSV file
    companies = pd.read_csv(input_csv)
    results = []

    # Iterate over each company and scrape the follower count
    for _, row in companies.iterrows():
        company_name = row['company_name']
        company_url = row['company_url']
        follower_count = scrape_follower_count(company_url)
        print(f"Follower count for company {company_name} is: {follower_count}\n")
        if follower_count is not None:
            results.append((company_name, company_url, follower_count))
        else:
            results.append((company_name, company_url, 'N/A'))

    # Save the results to the output CSV file
    save_to_csv(results, output_csv)


if __name__ == "__main__":
    # Define paths to your companies and followers CSV files
    input_csv = 'companies.csv'
    output_csv = 'followers.csv'
    main(input_csv, output_csv)