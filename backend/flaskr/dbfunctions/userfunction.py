from flaskr import get_db
import sys
import sqlite3

#


class User:

    # Userinput from register form is inserted into the database (users table).
    # Username is unique, and can therefor only be created one time. If username already exists, the function will return an error.
    def new_user(self, Data):
        username = Data["username"]
        password = Data["password"] 
        firstname = Data["firstname"]
        lastname = Data["lastname"]
        email = Data["email"] 

        conn = get_db()
        curr = conn.cursor()
        try: 
            sql = (
                """
                INSERT INTO users
                (username, password, firstname, lastname, email, sort_state, grid_state) 
                VALUES(?, ?, ?, ? ,?, ?, ?)
                """
            )
            curr.execute(sql, (username, password, firstname, lastname, email, "sortNewOld","grid")) 
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("User created")
            return curr.lastrowid 
        finally:
            curr.close()


    # Updates the users sort selection.
    def update_sort_state(self, username, sort_state):
        conn = get_db()
        curr = conn.cursor()

        try: 
            sql = (
                """
                UPDATE users SET sort_state = ? WHERE username = ?
                """
            )
            curr.execute(sql, (sort_state,username,) )
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Sort state updated from db.")
            print(sort_state)
            
            return curr.lastrowid 
        finally:
            curr.close()

  

        
    # Handles user authentication during Login.
    def check_user(self, Data):
        username = Data["username"]
        password = Data["password"] 

        conn = get_db()
        curr = conn.cursor()
        try:
            sql = (
                """
                SELECT * FROM users WHERE username=?
                """
            )
            curr.execute(sql, (username,))
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            data=curr.fetchall()
            if len(data) != 0: 
                if (data[0]["password"] == password):
                    return {
            "username" : data[0]["username"],
            "firstname" : data[0]["firstname"],
            "lastname" : data[0]["lastname"],
            "email" : data[0]["email"],
            "sort_state" :data[0]["sort_state"],
            "grid_state" :data[0]["grid_state"],
          }
            return -1 
        finally:
            curr.close()

    
    # Inserts new products created into the products table in database.
    def new_product(self, Data):
        username = Data["username"]
        productname = Data["productname"] 
        price = Data["price"]
        start_date = Data["start_date"]
        end_date = Data["end_date"]
        description = Data["description"]
        productImg = Data["productImg"]

        conn = get_db()
        curr = conn.cursor()

        try: 
            sql = (
                """
                INSERT INTO products
                (username, productname, description, price, startdate, enddate, booked, productImg) 
                VALUES(?, ?, ?, ? ,? ,? ,? ,? )
                """
            )
            curr.execute(sql, (username, productname, description, price, start_date, end_date, 0,productImg,) ) 
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Product Added from userfunction")
            return curr.lastrowid 
        finally:
            curr.close()

    # Selects all rows from products table
    def get_products(self):
        conn = get_db()
        curr = conn.cursor()

        try:
            sql = (
                """
                SELECT * FROM products
                """
            )
            curr.execute(sql)
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            data=curr.fetchall()
            print(data)
            productList = []
            if len(data) != 0: 
                for row in data:
                    productList.append(
                        {'productId':row['productId'],'name': row['productname'], 'description': row['description'], 'productImg': row["productImg"], 'username': row['username'], 'price': row['price'], 'startdate':row['startdate'], 'enddate': row['enddate'], 'booked':row['booked']}
                    )
                
                return productList
            return -1 
        finally:
            curr.close()

    # Deletes given product by specifying productId
    def delete_product(self,productId):
        conn = get_db()
        curr = conn.cursor()
        try:
            sql = (
                """
                DELETE FROM products WHERE productId = ?
                """
            )

            curr.execute(sql, (productId,))
            conn.commit()
        
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Product Removed from db.")
            return curr.lastrowid 
        finally:
            curr.close()

    # Adds a users booking to booking table in database.
    def book_product(self,productId,productname, myUser,startdate,enddate):
        conn = get_db()
        curr = conn.cursor()

        try: 
            sql = (
                """
                INSERT INTO booking
                (productId, productname, username, startdate, enddate) 
                VALUES(?, ?, ?, ?, ?)
                """
            )
            sql2 = (
                """
                UPDATE products SET booked = 1 WHERE productId = ?
                """
            )

            curr.execute(sql, (productId, productname,  myUser, startdate, enddate) )
            curr.execute(sql2, (productId,) ) 
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Booked from userfunction")
            return curr.lastrowid 
        finally:
            curr.close()

    # Selects all rows in booking table in database
    def get_bookings(self):
        conn = get_db()
        curr = conn.cursor()

        try:
            sql = (
                """
                SELECT * FROM booking
                """
            )
            curr.execute(sql)
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            data=curr.fetchall()
            print(data)
            bookingList = []
            if len(data) != 0: 
                for row in data:
                    
                    bookingList.append(
                        {'bookingId':row['bookingId'],'productId': row['productId'], 'username': row['username'], 'startdate': row["startdate"], 'enddate': row['enddate'], 'productname': row['productname']}
                    )
                return bookingList
            return -1 
        finally:
            curr.close()

    def delete_booking(self,bookingId, productId):
            conn = get_db()
            curr = conn.cursor()
            try:
                sql = (
                    """
                    DELETE FROM booking WHERE bookingId = ?
                    """
                )

                sql2 = (
                    """
                    UPDATE products SET booked = 0 WHERE productId = ?
                    """
                )

                curr.execute(sql, (bookingId,))
                curr.execute(sql2, (productId,))
                conn.commit()

            except sqlite3.Error as err:
                print("Error: {}".format(err))
                return -1 
            else:
                print("Booking Removed from db.")
                return curr.lastrowid 
            finally:
                curr.close()

    
    # Selects the row containg username input    
    def get_user_sort_state(self, username):
        conn = get_db()
        curr = conn.cursor()
        try:
            sql = (
                """
                SELECT * FROM users WHERE username=?
                """
            )
            curr.execute(sql, (username,))
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            data=curr.fetchall()
            if len(data) != 0: 
                if (data[0]["username"] == username):
                    return {
            "username" : data[0]["username"],
            "firstname" : data[0]["firstname"],
            "lastname" : data[0]["lastname"],
            "email" : data[0]["email"],
            "sort_state" :data[0]["sort_state"],
            "grid_state" :data[0]["grid_state"],
          }
            return -1 
        finally:
            curr.close()

    

    def update_grid_state(self,username,grid_state):
        conn = get_db()
        curr = conn.cursor()

        try: 
            sql = (
                """
                UPDATE users SET grid_state = ? WHERE username = ?
                """
            )
            curr.execute(sql, (grid_state,username,) )
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Grid state updated from db.")
            
            return curr.lastrowid 
        finally:
            curr.close()