from random import choice, randrange
from time import sleep

items = ['apple', 'pear', 'metal', 'slime']
while True:
    print(choice(items))
    for _ in range(randrange(10)):
        print('.', end='')
        sleep(1)
    print()
