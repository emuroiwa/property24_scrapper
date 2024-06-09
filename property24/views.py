from django.shortcuts import render
from .scraping_script import scrape_website

def scrape_view(request):
    url = 'https://www.property24.com/apartments-for-sale/royal-ascot/milnerton/western-cape/10769?sp=bd%3d2#114459350'  # The URL you want to scrape
    data = scrape_website(url)
    return render(request, 'scraper/results.html', {'data': data})
