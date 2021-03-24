from flask.templating import render_template
from flask import Flask
from views.extract_item import extract_item_blueprint

app = Flask(__name__)

app.register_blueprint(extract_item_blueprint, url_prefix="/item_extract")


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
