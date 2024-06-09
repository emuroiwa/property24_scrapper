import requests
from bs4 import BeautifulSoup
import logging

# Configure the logger
logger = logging.getLogger('scraper')

def scrape_website(url):
    logger.debug(f'Starting to scrape the website: {url}')
    
    response = requests.get(url)
    if response.status_code == 200:
        logger.debug(f'Successfully fetched the content from {url}')
        
        soup = BeautifulSoup(response.content, 'html.parser')
        logger.debug('Created BeautifulSoup object')

        properties = []
        listings_container = soup.find('div', class_='js_listingResultsContainer')
        
        if listings_container:
            property_elements = listings_container.find_all('div', class_='YieldingUploads js_resultTile p24_tileContainer')
            for element in property_elements:
                title = element.find('meta', itemprop='name')['content'] if element.find('meta', itemprop='name') else 'N/A'
                price = element.find('span', class_='p24_price').text.strip() if element.find('span', class_='p24_price') else 'N/A'
                location = element.find('span', class_='p24_location').text.strip() if element.find('span', class_='p24_location') else 'N/A'
                address = element.find('span', class_='p24_address').text.strip() if element.find('span', class_='p24_address') else 'N/A'
                bedrooms = element.find('span', class_='p24_featureDetails', title='Bedrooms').text.strip() if element.find('span', class_='p24_featureDetails', title='Bedrooms') else 'N/A'
                bathrooms = element.find('span', class_='p24_featureDetails', title='Bathrooms').text.strip() if element.find('span', class_='p24_featureDetails', title='Bathrooms') else 'N/A'
                parking = element.find('span', class_='p24_featureDetails', title='Parking Spaces').text.strip() if element.find('span', class_='p24_featureDetails', title='Parking Spaces') else 'N/A'
                size = element.find('span', class_='p24_size').text.strip() if element.find('span', class_='p24_size') else 'N/A'
                description = element.find('span', class_='p24_excerpt').text.strip() if element.find('span', class_='p24_excerpt') else 'N/A'

                properties.append({
                    'title': title,
                    'price': price,
                    'location': location,
                    'address': address,
                    'bedrooms': bedrooms,
                    'bathrooms': bathrooms,
                    'parking': parking,
                    'size': size,
                    'description': description
                })
                logger.debug(f'Found property: {title}, {price}, {location}, {address}, {bedrooms}, {bathrooms}, {parking}, {size}, {description}')
        else:
            logger.error('No listings container found')
        
        return properties, soup.prettify()
    else:
        logger.error(f'Failed to fetch the content from {url} with status code {response.status_code}')
        return None, None
