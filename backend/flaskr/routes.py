#from backend.dbfunctions import userfunction
from flask import render_template, Response ,redirect, request, url_for, flash, jsonify
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

@app.route("/api/login", methods = ["POST"])
def login():
  if request.method == "POST":
    userdata = request.get_json()
    result = userfunction.check_user(userdata)
    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)

    