from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from tkinter import ttk
from ttkthemes import themed_tk as tk
from influencer import management
from advertiser import adv
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('manage.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS inf_user (inf_use text not null, inf_pwd text not null);')
c.execute('CREATE TABLE IF NOT EXISTS adv_user (adv_use text not null, adv_pwd text not null);')
db.commit()
db.close()


# main Class
class main:
    def __init__(self, master):
        # Window
        self.master = master

        # Some Useful variables
        self.inf_use = StringVar()
        self.inf_pwd = StringVar()
        self.adv_use = StringVar()
        self.adv_pwd = StringVar()
        self.n_inf_use = StringVar()
        self.n_inf_pwd = StringVar()
        self.n_adv_use = StringVar()
        self.n_adv_pwd = StringVar()
        # Create Widgets
        self.widgets()

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('manage.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM inf_user WHERE inf_use = ? and inf_pwd = ?')
        c.execute(find_user, [(self.inf_use.get()), (self.inf_pwd.get())])
        result = c.fetchall()
        if result:

            self.logf.pack_forget()
            self.master.destroy()
            aryan = management()
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def adv_login(self):
        # Establish Connection
        with sqlite3.connect('manage.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM adv_user WHERE adv_use = ? and adv_pwd = ?')
        c.execute(find_user, [(self.adv_use.get()), (self.adv_pwd.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.master.destroy()
            aryan = adv()
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('manage.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT inf_use FROM inf_user WHERE inf_use = ?')
        c.execute(find_user, [(self.n_inf_use.get())])
        if c.fetchall():
            ms.showerror('Error!', 'inf_use Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO inf_user(inf_use,inf_pwd) VALUES(?,?)'
        c.execute(insert, [(self.n_inf_use.get()), (self.n_inf_pwd.get())])
        db.commit()

    def new_adv_user(self):
        # Establish Connection
        with sqlite3.connect('manage.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT adv_use FROM adv_user WHERE adv_use = ?')
        c.execute(find_user, [(self.n_inf_use.get())])
        if c.fetchall():
            print(c.fetchall())
            ms.showerror('Error!', 'adv_use Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        # Create New Account
        insert = 'INSERT INTO adv_user(adv_use,adv_pwd) VALUES(?,?)'
        c.execute(insert, [(self.n_inf_use.get()), (self.n_inf_pwd.get())])
        db.commit()

        # Frame Packing Methods

    def log(self):
        self.inf_use.set('')
        self.inf_pwd.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()

    def cr(self):
        self.n_inf_use.set('')
        self.n_inf_pwd.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = ttk.Label(self.master, text='LOGIN')
        self.head.pack()
        self.logf = ttk.Frame(self.master)
        ttk.Label(self.logf, text='Username: ',).grid(sticky=W)
        Entry(self.logf, textvariable=self.inf_use, bd=5,).grid(row=0, column=1)
        ttk.Label(self.logf, text='Password: ',).grid(sticky=W)
        Entry(self.logf, textvariable=self.inf_pwd, bd=5, show='*').grid(row=1, column=1)
        ttk.Button(self.logf, text=' Login as Influencer ', command=self.login).grid()
        ttk.Button(self.logf, text=' Login as Advertiser', command=self.adv_login).grid(row=2, column=1)
        ttk.Button(self.logf, text=' Create Account ', command=self.cr).grid(row=3, columnspan=2)
        self.logf.pack()

        self.crf = Frame(self.master  , pady=10)
        ttk.Label(self.crf, text='Username: ').grid(sticky=W)
        Entry(self.crf, textvariable=self.n_inf_use,).grid(row=0, column=1)
        ttk.Label(self.crf, text='Password: ').grid(sticky=W)
        Entry(self.crf, textvariable=self.n_inf_pwd, show='*').grid(row=1, column=1)
        ttk.Button(self.crf, text='Create Account as Influencer', command=self.new_user).grid()
        ttk.Button(self.crf, text='Create Account as Advertiser', command=self.new_adv_user).grid(row=2, column=1)
        ttk.Button(self.crf, text='Go to Login', command=self.log).grid(row=3, columnspan=2)



if __name__ == '__main__':
    # Create Object
    # and setup window
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme('radiance')
    root.title('Login Form')
    # root.geometry('400x350+300+300')
    main(root)
    root.mainloop()