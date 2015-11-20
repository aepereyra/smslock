#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('accesslist.db')


conn.execute('''CREATE TABLE USUARIO
       (CELLPHONE CHAR(11) PRIMARY KEY     NOT NULL,
       PASSWD     CHAR(138)    NOT NULL);''')

print "Table created successfully";

conn.close()
