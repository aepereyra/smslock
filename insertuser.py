#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import sys
conn = sqlite3.connect('accesslist.db')
with conn:    
    conn.execute("INSERT INTO USUARIO VALUES ('arg1','arg2');")

