from __future__ import absolute_import

from celery import Celery

from app.config.config import defaults, queues

app = Celery(
    'app',
    broker=defaults['broker'],
    include=[
        'app.tasks.examples.basic',
    ],
    CELERY_ROUTES={
        'app.tasks.save_in_mongo': {'queue': queues['save_in_mongo']}
    }
)


if __name__ == '__main__':
    app.start()
