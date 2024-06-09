from django.shortcuts import render
from .scraping_script import scrape_website
import logging

# Configure the logger
logger = logging.getLogger('scraper')

def scrape_view(request):
    url = 'https://www.property24.com/apartments-for-sale/royal-ascot/milnerton/western-cape/10769?sp=bd%3d2#114459350'  # The URL you want to scrape
    logger.debug(f'Received request to scrape {url}')
    
    data, soup_dump = scrape_website(url)
    
    if data:
        logger.debug('Scraping successful, rendering results')
    else:
        logger.error('Scraping failed')
    
    return render(request, 'scraper/results.html', {'data': data, 'soup_dump': soup_dump})
