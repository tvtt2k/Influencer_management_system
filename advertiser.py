from tkinter import *
import tkinter.messagebox
import adv_backend
from tkinter import ttk
from ttkthemes import themed_tk as tk
from infsearch import infrch
import backend
from contract import make_contract
class adv():
  def __init__(self):
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme('radiance')
    root.title('Advertiser System')

    def callback():
      if tkinter.messagebox.askokcancel("quit", "Do You really want to quit?"):
        root.destroy()

    def clear():
      e1.delete(0, END)
      e2.delete(0, END)
      e3.delete(0, END)
      e4.delete(0, END)

    def add_entry():
      adv_backend.insert(adv_name_txt.get(), inf_cat_txt.get(), adv_phone_txt.get(), comp_name_txt.get())
      listing.delete(0, END)
      listing.insert(END, (adv_name_txt.get(), inf_cat_txt.get(), adv_phone_txt.get(), comp_name_txt.get()))
      clear()

    def view_all():
      listing.delete(0, END)
      for row in adv_backend.view():
        listing.insert(END, row)
      clear()

    def update():
      global selected_tuple
      adv_backend.update(selected_tuple[0], adv_name_txt.get(), inf_cat_txt.get(), adv_phone_txt.get(), comp_name_txt.get())
      view_all()

    def get_selected_row(event):
      global selected_tuple
      clear()
      index = listing.curselection()[0]
      selected_tuple = listing.get(index)
      e1.insert(END, selected_tuple[1])
      e2.insert(END, selected_tuple[3])
      e3.insert(END, selected_tuple[2])
      e4.insert(END, selected_tuple[4])

    def delete():
      global selected_tuple
      adv_backend.delete(selected_tuple[0])
      view_all()

    def search():
      listing.delete(0, END)
      search_data = adv_backend.search(adv_name_txt.get(), inf_cat_txt.get(), adv_phone_txt.get(), comp_name_txt.get())
      if len(search_data) != 0:
        for row in search_data:
          listing.insert(END, row)
      else:
        tkinter.messagebox.showinfo('Message', 'NO RESULT FOUND')
      clear()

    selected_tuple = tuple()
    adv_name_txt = StringVar()
    inf_cat_txt = StringVar()
    adv_phone_txt = StringVar()
    comp_name_txt = StringVar()
    l = ttk.Label(root, text='advertiser Name', relief=RAISED)
    l.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
    l = ttk.Label(root, text='Genre/Category', relief=RAISED)
    l.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')

    e1 = Entry(root, textvariable=adv_name_txt)
    e1.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')

    e2 = ttk.Combobox(root, textvariable=inf_cat_txt)
    e2['values'] = ('Select Category',
                    'Vlogger',
                    'Photographer',
                    'StandUp Comedian',
                    'Reality Show',
                    'Activist',
                    'Journalist',
                    'Sports',
                    'Food Blogger',
                    'Videographer',
                    'Beauty',
                    'Gamer')
    e2.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')
    e2.current(0)

    l = ttk.Label(root, text='Company Name', relief=RAISED)
    l.grid(row=0, column=2, padx=5, pady=5, sticky='nswe')
    l = ttk.Label(root, text='Phone Number', relief=RAISED)
    l.grid(row=1, column=2, padx=5, pady=5, sticky='nswe')
    e3 = Entry(root, textvariable=comp_name_txt)
    e3.grid(row=0, column=3, padx=5, pady=5, sticky='nswe')
    e4 = Entry(root, textvariable= adv_phone_txt)
    e4.grid(row=1, column=3, padx=5, pady=5, sticky='nswe')

    b1 = ttk.Button(root, text='View All advertisers', command=view_all)
    b1.grid(row=2, column=4, padx=5, pady=5, sticky='nswe')
    b2 = ttk.Button(root, text='Search advertiser', command=search)
    b2.grid(row=3, column=4, padx=5, pady=5, sticky='nswe')
    b3 = ttk.Button(root, text='Add advertiser', command=add_entry)
    b3.grid(row=4, column=4, padx=5, pady=5, sticky='nswe')
    b4 = ttk.Button(root, text='             Update Influencer Data             ', command=update)
    b4.grid(row=5, column=4, padx=5, pady=5, sticky='nswe')
    b5 = ttk.Button(root, text='Delete advertiser Data', command=delete)
    b5.grid(row=6, column=4, padx=5, pady=5, sticky='nswe')
    b6 = ttk.Button(root, text='Exit', command=root.destroy)
    b6.grid(row=7, column=4, padx=5, pady=5, sticky='nswe')
    def xyz():
      a=infrch()
    def abc():
      b=make_contract()
    b7 = ttk.Button(root, text='Search Influencer', command=xyz)
    b7.grid(row=0, column=4, padx=5, pady=5, sticky='nswe')

    b8 = ttk.Button(root, text='Make a Contract', command=abc)
    b8.grid(row=1, column=4, padx=5, pady=5, sticky='nswe')

    listing = Listbox(root)
    listing.grid(row=2, column=0, rowspan=6, columnspan=4, padx=5, pady=5, sticky='nswe')
    listing.bind('<<ListboxSelect>>', get_selected_row)

    for i in range(4):
      root.grid_columnconfigure(i, weight=1)
    for i in range(8):
      root.grid_rowconfigure(i, weight=1)

    root.protocol("WM_DELETE_WINDOW", callback)
    root.mainloop()