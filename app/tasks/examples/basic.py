from __future__ import absolute_import
from bs4 import BeautifulSoup

from app.celery import app
from app.libs.mongo import Mongo
from app.libs.scraper import Scraper


@app.task
def add(x, y):
    """
    basic sum function to test our deployment
    """
    return x + y


@app.task
def add_and_save(x, y):
    """
    sum function which store results in mongodb
    """
    sum = x + y
    """
    a new task to save results in mongodb. This will add results in queue (dev_save_in_mongo) and worker listening on that queue will save data in mongodb.
    """
    save_in_mongo.delay({'x': x, 'y': y, 'sum': sum})
    return True


@app.task
def save_in_mongo(data_to_save):
    """
    This will store results in mongo using function created in libs/mongo.py
    """
    mongo = Mongo()
    inserted_id = mongo.save_addition(data_to_save)
    return inserted_id


@app.task
def get_title(url):
    """
    It scrape title be opening url and store results in mongo
    Return dict containing url and title
    """

    # Create Scraper class object, located at libs/scraper.py
    scraper = Scraper()

    # Calling get_page function to get scraped page
    response = scraper.get_page(url)
    data_to_save = {
        'url': url,
        'title': None
    }

    # Checking page content exists or not
    if response['page'] is not None:
        # Creating tree lxml tree
        soup = BeautifulSoup(response['page'], 'lxml')

        # Getting title from scraped page
        data_to_save['title'] = soup.title.string

    # Save results in mongo
    mongo = Mongo()
    mongo.save_titles(data_to_save)
    return data_to_save
