from flask import Flask, request
from rangescore.utils import percentiles

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/lemmatize/<string:lang>', methods=['POST'])
def lemmmatize(lang):
    if lang == 'ru' and request.method == 'POST':
        print(request.json)
        return percentiles(request.json['text'])
    return lang
