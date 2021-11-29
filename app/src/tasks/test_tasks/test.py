import time
import random
from app.src import celery


@celery.task(bind=True)
def test_task(self):
    print('instant')
    time.sleep(3)
    print('delayed')
