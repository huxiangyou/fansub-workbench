from flask import Flask
from flask import request

app = Flask(__name__,
            template_folder="../client/dist",
            static_folder="../client/dist/static")

from views import app

@app.route('/test', methods=["POST"])
def test():
    text = request.json.get("text")
    res = text + '-response'
    return res
