import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to fetch PageSpeed Insights for multiple URLs
def fetch_pagespeed_results(urls, api_key):
    results = []
    for url in urls:
        endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
        params = {
            "url": url,
            "key": api_key
        }
        response = requests.get(endpoint, params=params)
        results.append(response.json())  # Append each result to the list
    return results

# Function to save the results
def save_results(data, url, directory_base='reports'):
    # Format directory path with date
    date_str = datetime.now().strftime('%m%d%y')
    time_str = datetime.now().strftime('%H%M%S')
    # Create a valid filename from the URL
    filename = f"{time_str}-{url.replace('http://', '').replace('https://', '').replace('/', '_')}-report.json"
    directory = os.path.join(directory_base, date_str)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

# Main execution
def main():
    urls = os.getenv("URLS")
    api_key = os.getenv("API_KEY")
    if not urls or not api_key:
        print("URLs or API Key not found in .env file.")
        return
    url_list = urls.split(',')  # Split the URL string into a list
    results = fetch_pagespeed_results(url_list, api_key)
    for result, url in zip(results, url_list):
        save_results(result, url)
    print("Reports saved successfully.")

if __name__ == "__main__":
    main()
