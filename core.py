from random import choice, randrange
from time import sleep

items = ['apple', 'pear', 'metal', 'slime']
while True:
    print(choice(items))
    sleep(randrange(10))
