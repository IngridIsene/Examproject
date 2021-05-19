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
        print("DU SUGE!!!!")
        try:
            sql = (
                """
                (SELECT username, password FROM addresses WHERE user = ?")
                """
            )
            curr.execute(sql, (username,))
            data=curr.fetchall()
            if len(data) != 0: 
                print("Hello")
            else:
                print("Okay")
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("Login sucess")
            return curr.lastrowid 
        finally:
            curr.close()
            
