from flaskr import get_db
import sys
#from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

class User: 
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
                (username, password, firstname, lastname, email) 
                VALUES(?, ?, ?, ? ,?)
                """
            )
            curr.execute(sql, (username, password, firstname, lastname, email)) 
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("User created")
            return curr.lastrowid 
        finally:
            curr.close()


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
          }
            return -1 
        finally:
            curr.close()
    

    def new_product(self, Data):
        username = Data["username"]
        productname = Data["productname"] 
        price = Data["price"]
        start_date = Data["start_date"]
        end_date = Data["end_date"]
        description = Data["description"]

        conn = get_db()
        curr = conn.cursor()

        try: 
            sql = (
                """
                INSERT INTO products
                (username, productname, description, price, startdate, enddate) 
                VALUES(?, ?, ?, ? ,?,?)
                """
            )
            curr.execute(sql, (username, productname, description, price, start_date, end_date) ) 
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Product Added from userfunction")
            return curr.lastrowid 
        finally:
            curr.close()

    
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
                        {'productId':row['productId'],'name': row['productname'], 'description': row['description'], 'img': "frostsko.jpeg", 'username': row['username'], 'price': row['price'], 'startdate':row['startdate'], 'enddate': row['enddate']}
                    )
                
                return productList
            return -1 
        finally:
            curr.close()


    def delete_product(self,productId):
        conn = get_db()
        curr = conn.cursor()
        try:
            sql = (
                """
                DELETE FROM products WHERE productId = ?
                """
            )
            sql2 = (
                """
                DELETE FROM booking WHERE productId = ?
                """
            )

            curr.execute(sql, (productId,))
            curr.execute(sql2,(productId,))
            conn.commit()
        
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Product Removed from db.")
            return curr.lastrowid 
        finally:
            curr.close()


    def book_product(self,productId,myUser,startdate,enddate):
        conn = get_db()
        curr = conn.cursor()

        try: 
            sql = (
                """
                INSERT INTO booking
                (productId, username, startdate, enddate) 
                VALUES(?, ?, ?, ?)
                """
            )
            curr.execute(sql, (productId, myUser, startdate, enddate) ) 
            conn.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Booked from userfunction")
            return curr.lastrowid 
        finally:
            curr.close()

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
                    productname = self.get_productName(row['productId'])
                    #print('PRODUCTNAME',productname[0])
                    bookingList.append(
                        {'bookingId':row['bookingId'],'productId': row['productId'], 'username': row['username'], 'startdate': row["startdate"], 'enddate': row['enddate'], 'productname': productname}
                    )
                return bookingList
            return -1 
        finally:
            curr.close()

    def get_productName(self, productId):
        conn = get_db()
        curr = conn.cursor()
        try:
            sql = (
                """
                SELECT productname FROM products WHERE productId = ?
                """
            )

            curr.execute(sql, (productId,) ) 
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            data=curr.fetchall()
            if len(data) != 0: 
                for row in data:
                    productname = row['productname']
                return productname
            
        finally:
            curr.close()
        
        
