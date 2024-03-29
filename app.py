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
    return rend("index.html", adilar=set(map(lambda x: x["company"], stodvar)), min_dies = min(stodvar, key=lambda x: x["diesel"]), min_bens=min(stodvar, key=lambda x: x["bensin95"]))
@app.route("/<adili>")
def adili(adili):
    if adili in map(lambda x: x["company"],stodvar):
        return rend("adili.html", company=adili, stadir=stodvar)
    else: return page_not_found(404)
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