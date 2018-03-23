#
# This python file is a configuration file which is used to set default configuration.
# Define custom configuration in config.ini file, store those configurations in a variable and use
# it in your application.

import configparser


# defaults is used to set default configuration for your application.
defaults = {
    'environment': 'dev',
    'broker': 'amqp://myuser:mypassword@localhost:5672/myvhost',
    'mongo_uri': 'mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]',
    'database': 'celery_pymongo'
}

Config = configparser.ConfigParser(defaults=defaults)
Config.read('app/config/config.ini')

# defaults can be overrride to set values from config.ini
defaults = {
    'environment': Config.get('DEFAULT', 'environment'),
    'broker': Config.get('DEFAULT', 'broker'),
    'mongo_uri': Config.get('DEFAULT', 'mongo_uri'),
}

"""
queues is used to set different queues according to development environment.
App environment is prepended to queues so that different queues can be used
according to app running environment.
"""
queues = {
    # default: dev_save_in_mongo
    'save_in_mongo': defaults['environment'] + '_save_in_mongo'
}


# servers is used to set database and collection for different tasks.
servers = {
    'task_addition': {
        'db': Config.get('SERVERS', 'db_task_addition'),
        'col': Config.get('SERVERS', 'col_task_addition'),
    }
}
