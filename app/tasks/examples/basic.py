from __future__ import absolute_import

from app.celery import app
from app.libs.mongo import Mongo


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

    """
    mongo = Mongo()
    inserted_id = mongo.save_addition(data_to_save)
    return inserted_id
