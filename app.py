from flask import Flask, request
from rangescore.utils import percentiles
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze/<string:lang>', methods=['POST'])
def lemmmatize(lang):
    if lang == 'ru' and request.method == 'POST':
        print(request.json)
        return percentiles(request.json['text'])
    return lang
