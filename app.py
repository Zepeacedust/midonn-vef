from flask import Flask, render_template as rend
import requests, json
app = Flask(__name__)

with requests.get('https://apis.is/petrol') as response:
    if response:
        print('API Succesfully loaded')
        stodvar = response.json()['results']
    else:
        print('API error')
        exit()


@app.route("/debug")
def debug():
    return str(stodvar)
@app.route('/')
def hello():
    return rend("index.html", adilar=set(map(lambda x: x["company"], stodvar)), min_dies = max(stodvar, key=lambda x: x["diesel"]), min_bens=max(stodvar, key=lambda x: x["bensin95"]))
@app.route("/<adili>")
def adili(adili):
    return rend("adili.html", company=adili, stadir=stodvar)
@app.route("/stadur/<stadur>")
def stadur(stadur):
    for stad in stodvar:
        if stad["key"] == stadur:
            return rend("stadur.html", stadur=stad)
    rend('404.html')
@app.errorhandler(404)
def page_not_found(e):
    return rend('404.html')

if __name__ == '__main__':
    app.run()