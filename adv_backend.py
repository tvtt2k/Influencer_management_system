import sqlite3

def connection_m():
  conn=sqlite3.connect('manage.db')
  conn.execute('CREATE TABLE if not exists advertise(adv_id integer PRIMARY KEY AUTOINCREMENT, inf_cat text not null, comp_name text not null, adv_phone integer, adv_name text)')
  conn.commit()
  conn.close()

def insert(adv_name,inf_cat,adv_phone,comp_name):
  conn=sqlite3.connect('manage.db')
  conn.execute("INSERT INTO advertise VALUES (NULL,?,?,?,?)",(adv_name,inf_cat,adv_phone,comp_name))
  conn.commit()
  conn.close()


def view():
  conn=sqlite3.connect('manage.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from advertise")
  rows=cur_obj.fetchall()
  conn.close()
  return rows

def update(adv_id,adv_name,inf_cat,adv_phone,comp_name):
  conn=sqlite3.connect('manage.db')
  conn.execute("UPDATE advertise SET adv_name=?,inf_cat=?,adv_phone=?,comp_name=? WHERE adv_id=?",(adv_name,inf_cat,adv_phone,comp_name,adv_id))
  conn.commit()
  conn.close()

def delete(adv_id):
  conn=sqlite3.connect('manage.db')
  conn.execute("DELETE from advertise WHERE adv_id=?",(adv_id,))
  conn.commit()
  conn.close()

def search(adv_name='',inf_cat='',adv_phone='',comp_name=''):
  conn=sqlite3.connect('manage.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from advertise WHERE adv_name=? OR inf_cat=? OR adv_phone=? OR comp_name=?",(adv_name,inf_cat,adv_phone,comp_name))
  rows=cur_obj.fetchall()
  conn.close()
  return rows

connection_m()