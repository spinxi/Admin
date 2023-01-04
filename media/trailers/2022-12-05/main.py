import time
from flask import Flask

app = Flask(__name__)

def gio():
    i = 0
    while True:
        print(f'i == {i}')
        i+=1
        time.sleep(2)
@app.route('/')
def hello():
    return gio()

