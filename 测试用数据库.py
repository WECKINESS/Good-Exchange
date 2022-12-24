import sqlite3     
        
conn = sqlite3.connect('helping.db')
cur = conn.cursor()
cur.execute('create table if not exists book (name text, quantity text, clarify text, author text, publisher text, id text, address text, communication text);')
cur.execute('create table if not exists food (name text, quantity text, clarify text, use_by_date text, id text, address text, communication text);')