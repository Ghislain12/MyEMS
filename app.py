from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
# app.template_folder = 'template'


@app.route('/')
def index():
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
