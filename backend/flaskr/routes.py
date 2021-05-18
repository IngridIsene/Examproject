from flask import render_template, Response ,redirect, request, url_for, flash
from flaskr import app


@app.route("/")
def index():
  return "Return production build here"

@app.route("/api/register", methods=["POST"])
def login():
  if request.method == "POST":
    print(request.get_json())
    return Response(status=200)