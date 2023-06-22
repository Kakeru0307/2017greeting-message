
from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    return message
 
def hello(name):
    message = 'Hello, ' + name + '-san!'
    return message

greet()


hello('Inoue')
