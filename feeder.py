# this python file call task functions defined in tasks directory
from app.tasks.examples.basic import add, add_and_save,get_title

# basic sum example
add.delay(2, 3)

# basic sum example with results store in mongo
add_and_save.delay(2, 3)

# scraping following urls to get title and store in mongo
urls_to_scrape = [
    "http://tusharsharma.in/",
    "http://example.com/",
    "https://www.google.co.in/"
]
for url in urls_to_scrape:
    get_title.delay(url)
