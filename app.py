from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap5(app)   # Bootstrap base template & helpers
moment = Moment(app)          # Makes "moment(...)" available in templates

@app.route("/")
def index():
    name = "Mustafa Nisar"
    return render_template(
        "index.html",
        name=name,
        current_time=datetime.utcnow()  # server sends UTC; browser formats locally
    )

if __name__ == "__main__":
    app.run(debug=True)
