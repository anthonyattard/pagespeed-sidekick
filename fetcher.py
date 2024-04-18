import requests
import json
import os
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
def save_results(data, directory, filename):
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
    save_results(results, 'reports', 'pagespeed_reports.json')
    print("Reports saved successfully.")

if __name__ == "__main__":
    main()
