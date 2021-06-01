DROP TABLE IF EXISTS [booking];
DROP TABLE IF EXISTS [products];
DROP TABLE IF EXISTS [users];




CREATE TABLE IF NOT EXISTS users (
  username TEXT NOT NULL PRIMARY KEY UNIQUE,
  password TEXT NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  sort_state TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS products ( 
productId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
productname TEXT NOT  NULL, 
description TEXT NOT NULL, 
price INTEGER NOT NULL, 
startdate TEXT NOT NULL, 
enddate TEXT NOT NULL, 
booked INTEGER NOT NULL,
productImg TEXT NOT NULL,
FOREIGN KEY (username) REFERENCES [users](username)
);

CREATE TABLE IF NOT EXISTS booking ( 
bookingId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
productId INTEGER NOT NULL,
productname TEXT NOT NULL, 
username TEXT NOT NULL,
startdate TEXT NOT NULL, 
enddate TEXT NOT NULL, 
FOREIGN KEY (username) REFERENCES [users](username),
FOREIGN KEY (productId) REFERENCES [products](productId)
);
