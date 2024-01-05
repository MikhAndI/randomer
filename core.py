from random import choice
from time import sleep

items = ['apple', 'pear', 'metal', 'slime']
time_2 = range(10)

while True:
    print(choice(items))
    sleep(choice(time_2))
