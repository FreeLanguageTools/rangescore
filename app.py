from flask import Flask, request
from rangescore.utils import coverages
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/healthcheck')
def healthcheck():
    return "Hello"

@app.route('/analyze/<string:lang>', methods=['POST'])
def lemmmatize(lang):
    if lang == 'ru' and request.method == 'POST':
        print(request.json)
        print(p:=coverages(request.json['text']))
        return p
    return lang
