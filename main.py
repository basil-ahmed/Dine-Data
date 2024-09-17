import requests
from bs4 import BeautifulSoup
import csv
import random
from requests.exceptions import RequestException

# URL of the TripAdvisor page
url = 'https://www.tripadvisor.com/Restaurants-g32655-Los_Angeles_California.html'

# List of user agents to rotate
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
]

# Headers to make the request look more like a browser request
headers = {
    'User-Agent': random.choice(user_agents),
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/'
}

try:
    # Send a request to fetch the HTML content of the page
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

except RequestException as e:
    print(f"Error fetching the webpage: {e}")
else:
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store extracted restaurant data
    restaurants = []

    # Find all restaurants based on the updated class
    for restaurant_item in soup.find_all('div', class_='vIjFZ Gi o VOEhq'):
        restaurant = {}

        # Extract restaurant name
        name_tag = restaurant_item.find('a', class_='BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS')
        if name_tag:
            restaurant['name'] = name_tag.text.strip()
        else:
            restaurant['name'] = "N/A"

        # Extract reviews
        review_tag = restaurant_item.find('span', class_='IiChw')
        if review_tag:
            restaurant['reviews'] = review_tag.text.strip()
        else:
            restaurant['reviews'] = "N/A"

        # Extract price level
        price_tag = restaurant_item.find('span', text=lambda x: '$' in x if x else False)
        if price_tag:
            restaurant['price_level'] = price_tag.text.strip()
        else:
            restaurant['price_level'] = "N/A"

        restaurants.append(restaurant)

    csv_file = "TripAdvisor_LA_new.csv"

    try:
        # Write the restaurant data into a CSV file
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "reviews", "price_level"])
            writer.writeheader()
            writer.writerows(restaurants)

        print(f"Restaurant data successfully written to {csv_file}")

    except IOError as e:
        print(f"Error writing to CSV file: {e}")
