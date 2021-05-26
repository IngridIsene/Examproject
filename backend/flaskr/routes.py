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
    if result != -1: 
      return Response(status=200)
    else:
      return Response(status=400)
    #return Response(status=200)



@app.route("/api/profile", methods=["POST"])
def profile():
  if request.method == "POST":
    productdata = request.get_json()
    result = userfunction.new_product(productdata)
    return Response(status=200)

@app.route("/api/booking", methods=["POST"])
def booking():
  if request.method == "POST":
    info = request.get_json()
    productId = info[0]
    myUser = info[1]
    startdate = info[2]
    enddate = info[3]
    result = userfunction.book_product(productId,myUser,startdate,enddate)
    return Response(status=200)

@app.route("/api/bookings", methods=["GET"])
def bookings():
  if request.method == "GET":
    result = userfunction.get_bookings()
    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)



@app.route("/api/login", methods = ["POST"])
def login():
  if request.method == "POST":
    userdata = request.get_json()
    result = userfunction.check_user(userdata)
    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)


@app.route("/api/products", methods = ["GET"])
def products():
  if request.method == "GET":
    result = userfunction.get_products()
    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)


@app.route("/api/remove/<productId>", methods = ["DELETE"])
def remove(productId):
  if request.method == "DELETE":
    #productId = request.get_json()
    result = userfunction.delete_product(productId)
    
    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)


    