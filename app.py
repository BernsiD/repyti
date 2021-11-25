from flask.templating import render_template
from flask import Flask
from views.extract_item import extract_item_blueprint
from views.extract_effectivity import extract_effectivity_blueprint

app = Flask(__name__)

app.register_blueprint(extract_item_blueprint, url_prefix="/item_extract")
app.register_blueprint(extract_effectivity_blueprint, url_prefix="/effectivity_extract")


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
