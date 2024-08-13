import requests
from bs4 import BeautifulSoup
import json

# List of URLs to scrape
urls = [
    "https://www.scmturbo.com/find-your-turbo/alfa-romeo",
    "https://www.scmturbo.com/find-your-turbo/audi",
    "https://www.scmturbo.com/find-your-turbo/bentley",
    "https://www.scmturbo.com/find-your-turbo/bmw",
    "https://www.scmturbo.com/find-your-turbo/chrysler",
    "https://www.scmturbo.com/find-your-turbo/citroen",
    "https://www.scmturbo.com/find-your-turbo/daihatsu",
    "https://www.scmturbo.com/find-your-turbo/fiat",
    "https://www.scmturbo.com/find-your-turbo/fiat-iveco",
    "https://www.scmturbo.com/find-your-turbo/ford",
    "https://www.scmturbo.com/find-your-turbo/honda",
    "https://www.scmturbo.com/find-your-turbo/hyundai",
    "https://www.scmturbo.com/find-your-turbo/isuzu",
    "https://www.scmturbo.com/find-your-turbo/jaguar",
    "https://www.scmturbo.com/find-your-turbo/jeep",
    "https://www.scmturbo.com/find-your-turbo/kia",
    "https://www.scmturbo.com/find-your-turbo/land-rover",
    "https://www.scmturbo.com/find-your-turbo/ldv",
    "https://www.scmturbo.com/find-your-turbo/lotus",
    "https://www.scmturbo.com/find-your-turbo/mazda",
    "https://www.scmturbo.com/find-your-turbo/mini",
    "https://www.scmturbo.com/find-your-turbo/mitsubishi",
    "https://www.scmturbo.com/find-your-turbo/nissan",
    "https://www.scmturbo.com/find-your-turbo/peugeot",
    "https://www.scmturbo.com/find-your-turbo/porsche",
    "https://www.scmturbo.com/find-your-turbo/renault",
    "https://www.scmturbo.com/find-your-turbo/rover",
    "https://www.scmturbo.com/find-your-turbo/saab",
    "https://www.scmturbo.com/find-your-turbo/seat",
    "https://www.scmturbo.com/find-your-turbo/skoda",
    "https://www.scmturbo.com/find-your-turbo/smart",
    "https://www.scmturbo.com/find-your-turbo/ssangyong",
    "https://www.scmturbo.com/find-your-turbo/subaru",
    "https://www.scmturbo.com/find-your-turbo/suzuki",
    "https://www.scmturbo.com/find-your-turbo/toyota",
    "https://www.scmturbo.com/find-your-turbo/vauxhall",
    "https://www.scmturbo.com/find-your-turbo/volkswagen",
    "https://www.scmturbo.com/find-your-turbo/volvo",

    # Add more URLs here...
]

for url in urls:
    # Send a GET request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize a list to store model data
    models = []

    # Extract brand name from the URL (e.g., "audi")
    brand = url.split('/')[-1]

    # Find all vehicle model sections
    for vehicle in soup.find_all('div', class_='scm-part-vehicle'):
        model_info = {
            "model": vehicle.find('a', class_='spv-model').text.strip(),
            "engine": vehicle.find('a', class_='spv-engine').text.strip(),
            "engineCode": vehicle.find('div', class_='spv-detail spv-mb-hide').find('p').text.strip(),
            "power": vehicle.find('div', class_='spv-detail left').find('p').text.strip(),
            "year": vehicle.find('div', class_='spv-detail right').find('p').text.strip(),
            "turboModel": vehicle.find_all('div', class_='spv-detail left')[1].find('p').text.strip(),
            "oemPartNo": vehicle.find_all('div', class_='spv-detail-large')[0].find('p').text.strip(),
            "baseCode": vehicle.find_all('div', class_='spv-detail-large')[1].find('p').text.strip()
        }
        
        models.append(model_info)
    
    # Save the data as a JSON file
    with open(f'{brand}.json', 'w') as json_file:
        json.dump({"brand": brand.capitalize(), "models": models}, json_file, indent=4)

    print(f"Data saved to {brand}.json")
