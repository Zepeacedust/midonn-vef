from flask import Flask, render_template as rend
import requests,json
app = Flask(__name__)

stodvar = json.load(requests.get("https://apis.is/petrol").content)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()