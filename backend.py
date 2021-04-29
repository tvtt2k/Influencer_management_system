import sqlite3

def connection():
  conn=sqlite3.connect('manage.db')
  #conn.execute('CREATE TABLE if not exists influencer (id integer PRIMARY KEY AUTOINCREMENT, inf_name text not null, inf_smh text not null, inf_dob integer, inf_foll text)')
  #conn.execute('ALTER TABLE influencer ADD COLUMN inf_cat text')
  #conn.execute('ALTER TABLE influencer ADD COLUMN inf_pwd text')
  #conn.execute('ALTER TABLE influencer ADD COLUMN inf_use text')
  #conn.execute('CREATE TABLE if not exists contract (con_id integer PRIMARY KEY AUTOINCREMENT, id INTEGER NOT NULL, adv_id INTEGER NOT NULL, inf_name TEXT NOT NULL, comp_name TEXT NOT NULL, inf_cat TEXT NOT NULL, duration INTEGER NOT NULL, FOREIGN KEY(adv_id) REFERENCES advertise(adv_id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(id) REFERENCES influencer(id) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(comp_name) REFERENCES advertise(comp_name) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(inf_cat) REFERENCES influencer(inf_cat) ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY(inf_name) REFERENCES influencer(inf_name) ON UPDATE CASCADE ON DELETE CASCADE)')
  conn.commit()
  conn.close()

def insert(inf_name,inf_smh,inf_dob,inf_foll,inf_cat):
  conn=sqlite3.connect('manage.db')
  conn.execute("INSERT INTO influencer VALUES (NULL,?,?,?,?,?)",(inf_name,inf_smh,inf_dob,inf_foll,inf_cat))
  conn.commit()
  conn.close()

def view():
  conn=sqlite3.connect('manage.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from influencer")
  rows=cur_obj.fetchall()
  conn.close()
  return rows

def update(id,inf_name,inf_smh,inf_dob,inf_foll,inf_cat):
  conn=sqlite3.connect('manage.db')
  conn.execute("UPDATE influencer SET inf_name=?,inf_smh=?,inf_dob=?,inf_foll=?,inf_cat=? WHERE id=?",(inf_name,inf_smh,inf_dob,inf_foll,inf_cat,id))
  conn.commit()
  conn.close()

def delete(id):
  conn=sqlite3.connect('manage.db')
  conn.execute("DELETE from influencer WHERE id=?",(id,))
  conn.commit()
  conn.close()

def search(inf_name='',inf_smh='',inf_dob='',inf_foll='',inf_cat=''):
  conn=sqlite3.connect('manage.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from influencer WHERE inf_name=? OR inf_smh=? OR inf_dob=? OR inf_foll=? OR inf_cat=?",(inf_name,inf_smh,inf_dob,inf_foll,inf_cat))
  rows=cur_obj.fetchall()
  conn.close()
  return rows

def inf_search(start_range,end_range,inf_name=''):
  print(start_range,end_range,inf_name)
  conn=sqlite3.connect('manage.db')
  cur_obj=conn.cursor()
  cur_obj.execute("SELECT * from influencer WHERE inf_foll BETWEEN ? AND ? OR inf_name=?",(start_range,end_range,inf_name))
  rows = cur_obj.fetchall()
  conn.close()
  return rows

def con_insert(id,adv_id,inf_name,comp_name,inf_cat,duration,budget):
  conn=sqlite3.connect('manage.db')
  conn.execute("INSERT INTO contract VALUES (NULL,?,?,?,?,?,?,?)",(id,adv_id,inf_name,comp_name,inf_cat,duration,budget,))
  conn.commit()
  conn.close()

def view_cont():
  conn = sqlite3.connect('manage.db')
  cur_obj = conn.cursor()
  cur_obj.execute("SELECT * from influencer")
  rows = cur_obj.fetchall()
  result = []
  for row in rows:
    result.append(row[0])
  conn.close()
  return result

def inf_cont(id):
  conn = sqlite3.connect('manage.db')
  cur_obj = conn.cursor()
  cur_obj.execute("SELECT inf_name from influencer WHERE id=?",(id,))
  row=cur_obj.fetchall()
  return row
  conn.close()



connection()
