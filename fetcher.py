import requests
import json
import os

# Function to fetch PageSpeed Insights
def fetch_pagespeed_results(url, api_key):
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    # Parameters for the API
    params = {
        "url": url,
        "key": api_key
    }
    # Make the GET request
    response = requests.get(endpoint, params=params)
    return response.json()  # Return the JSON response

# Function to save the results
def save_results(data, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create directory if it does not exist
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)  # Write data to a file in JSON format

# Main execution
def main():
    url = input("Enter the URL to analyze: ")
    api_key = input("Enter your API key: ")
    result = fetch_pagespeed_results(url, api_key)
    save_results(result, 'reports', 'pagespeed_report.json')
    print("Report saved successfully.")

if __name__ == "__main__":
    main()
