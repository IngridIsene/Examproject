from flask import render_template, Response ,redirect, request, url_for, flash, jsonify
import sys
from flaskr import app
from .dbfunctions import userfunction


# All functions using the POST method retrieves the data from functions in user.services.js and passes them to the functions that is located in the dbfunctions folder(userfunction.py).
# All functions using the GET method calls on functions located in the dbfunctions (userfunction.py)
# The responses from the database functions are then passed on to the user.services.js (frontend)


@app.route("/")
def index():
  return "Return production build here"

# Calls on new_user function located in 
@app.route("/api/register", methods=["POST"])
def register():
  if request.method == "POST":
    userdata = request.get_json()
    result = userfunction.new_user(userdata)
    if result != -1: 
      return Response(status=200)
    else:
      return Response(status=400)



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
    productname = info[1]
    myUser = info[2]
    startdate = info[3]
    enddate = info[4]
    result = userfunction.book_product(productId,productname,myUser,startdate,enddate)
    return Response(status=200)


@app.route("/api/updatesort", methods=["POST"])
def updatesort():
  if request.method == "POST":
    info = request.get_json()
    username = info[0]
    sort_state = info[1]
    result = userfunction.update_sort_state(username,sort_state)
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
    result = userfunction.delete_product(productId)
    
    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)


@app.route("/api/removebooking", methods = ["POST"])
def removebooking():
  if request.method == "POST":
    IDs = request.get_json()
    bookingId = IDs[0]
    productId = IDs[1]
    result = userfunction.delete_booking(bookingId, productId)

    if result != -1: 
      return jsonify(result), 200
    else:
      return Response(status=400)