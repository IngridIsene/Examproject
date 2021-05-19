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

        curr = get_db()
        try: 
            sql = (
                """
                INSERT INTO users
                (username, password, firstname, lastname, email) 
                VALUES(?, ?, ?, ? ,?)
                """
            )
            curr.execute(sql, (username, password, firstname, lastname, email)) 
            curr.commit()
        except sqlite3.Error as err:
            print("Error: {}".format(err))
            return -1 
        else:
            print("User created")
            return curr.lastidrow 
        finally:
            curr.close()
