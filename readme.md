# Celery-Pymongo
---
Celery-pymongo is a deployment of celery which uses RabbitMQ as message broker, pymongo for storing task results in MongoDb.

## Features
---
- Separate queues according to application environment.
- Configurable database and collection for storing data in mongodb.
- Easily manageable tasks and configurations.

## Dev Requirements
---
- [Install Python 3](https://www.python.org/downloads/)
- [Install MongoDb](https://docs.mongodb.com/manual/installation/)
- [Install RabbitMQ](https://www.rabbitmq.com/download.html)
- [Install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
- [Enable RabbitMQ Management Plugin](https://www.rabbitmq.com/management.html)

### Installation
---
- clone repo (https://github.com/tusharsippy/celery-pymongo) in a directory
- cd celery-pymongo
- setup virtualenv
    - virtualenv -p python3 envname
- activate virtualenv
    - source envname/bin/activate
- install required packages
    - pip3 install -r requirements.txt

### Running celery-pymongo
---
- Goto root directory i.e. celery-pymongo
- Use following command to run celery
    - celery -A app worker -l info -Q dev_save_in_mongo,celery
- Open another terminal
- Goto root directory
- Activate virtualenv
- Use following command to add tasks
    - python feeder.py
- start flower by using following command
    - flower -A app --port=5555

### Directory Structure
├── app
│   ├── __init__.py
│   ├── celery.py (celery configuration)
│   ├── config (contain all configurations)
│   │   ├── __init__.py
│   │   ├── sample.config.ini (contain sample config, rename to config.ini for your application)
│   │   └── config.py (default configuration, read configuration from config.ini)
│   ├── libs (contain all libraries)
│   │   ├── __init__.py
│   │   └── mongo.py (class for mongo specific operations)
│   └── tasks (contain all tasks)
│       ├── __init__.py
│       └── examples (example tasks)
│           ├── __init__.py
│           └── basic.py (basic example task)
├── feeder.py (add task to queue for processing)
├── readme.md
├── requirements.txt (requirements for application)

### Monitoring
[RabbitMQ Monitoring](http://localhost:15672/)
[Flower Monitoring](http://localhost:5555/)

### TODO
- add scraping example
- add celery logger for logging
- add multiple mongodb database options
- add supervisor to run celery
