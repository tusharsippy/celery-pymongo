#
# This python file is used for mongo specfic database operations.
# Use defaults and servers variable in config.ini to set configuration for app.

from pymongo import MongoClient

from app.config.config import defaults, servers


class Mongo:
    def __init__(self):
        self.conn = MongoClient(defaults['mongo_uri'], connect=False)

    def save_addition(self, data_to_save):
        """
        save results of task defined at tasks/examples/basic.py as add_and_save
        Return document inserted id
        """
        inserted_id = None
        try:
            inserted_id = self.conn[servers['task_addition']['db']
                                    ][servers['task_addition']['col']].insert_one(data_to_save).inserted_id
        except Exception as e:
            print (e)
            pass

        return inserted_id
