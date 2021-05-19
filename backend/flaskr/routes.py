#from backend.dbfunctions import userfunction
from flask import render_template, Response ,redirect, request, url_for, flash
import sys
from flaskr import app
from .dbfunctions import userfunction



@app.route("/")
def index():
  return "Return production build here"

@app.route("/api/register", methods=["POST"])
def register():
  if request.method == "POST":
    userdata = request.get_json()
    result = userfunction.new_user(userdata)
    return Response(status=200)