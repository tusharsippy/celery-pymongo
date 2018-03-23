# this python file call task functions defined in tasks directory
from app.tasks.examples.basic import add, add_and_save

add.delay(2, 3)
add_and_save.delay(2, 3)
