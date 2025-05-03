import sqlite3

conn = sqlite3.connect('rpg_databace.db')
cursor = conn.cursor()

name = input('Введите имя ')
race = input('Введите расу ')
gender = input('Введите пол ')

cursor.execute('''
               INSERT INTO items(name, type, attacl_bonus, hp_bonus, price)
               VALUES (?,?,?,?,?)
               ''',(name,'poition', 0, 45, 120 ))
conn.commit()

conn.close()
