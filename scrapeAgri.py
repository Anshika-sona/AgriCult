import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.magicbricks.com/agricultural-land-for-sale-in-patna-pppfs'

# Fetch the webpage
response = requests.get(url)

if response.status_code == 200:
    html = response.text

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Initialize lists to store data
    property_names = []
    owners = []
    locations = []
    areas = []
    dimensions = []
    prices = []

    # Find all listings
    listings = soup.find_all('div', class_='mb-srp__list')

    for listing in listings:
        # Extract the required information
        name = listing.find('h2', class_='mb-srp__card--title')
        owner = listing.find('div', class_='mb-srp__card__ads--name')
        location = listing.find('p', class_='plot-desc')
        area = listing.find('div', class_='mb-srp__card__summary--value')
        dimension = listing.find('div', class_='mb-srp__card__summary--value')
        price = listing.find('div', class_='mb-srp__card__price--amount')

        # Append the information to respective lists
        property_names.append(name.text.strip() if name else 'N/A')
        owners.append(owner.text.strip() if owner else 'N/A')
        locations.append(location.text.strip() if location else 'N/A')
        areas.append(area.text.strip() if area else 'N/A')
        dimensions.append(dimension.text.strip() if dimension else 'N/A')
        prices.append(price.text.strip() if price else 'N/A')

    # Create a DataFrame
    data = {
        'Property Name': property_names,
        'Owner': owners,
        'Location': locations,
        'Area': areas,
        'Dimension': dimensions,
        'Price': prices
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('agricultural_land_bihar.csv', index=False)

    print("Data has been successfully scraped and saved to 'agricultural_land_bihar.csv'")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
