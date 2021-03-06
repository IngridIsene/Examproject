import os
from flask import Flask, g
from flask_cors import CORS
from config import DevelopmentConfig

import sqlite3

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config.from_object(DevelopmentConfig)


def get_db():
  db = getattr(g, "_database", None)

  if db is None:
    db = g._database = sqlite3.connect(app.config['DATABASE'])
  
  db.row_factory = sqlite3.Row # get dictionary cursor

  return db


def init_db():
  with app.app_context():
    db = get_db()

    with app.open_resource("schema.sql", mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

@app.teardown_appcontext
def teardown_db(error):
  """Closes the db conn at the end of the request."""
  db = getattr(g, "__database", None)
  if db is not None:
    print("Closing connection")
    db.close()

 #initialize db if it does not exist
if not os.path.exists(app.config['DATABASE']):
  init_db()

from flaskr import routes