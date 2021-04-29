from tkinter import *
import tkinter.messagebox
import adv_backend
from tkinter import ttk
from ttkthemes import themed_tk as tk
import backend

class infrch:
    def __init__(self):
        root = tk.ThemedTk()
        root.get_themes()
        root.set_theme('radiance')
        root.title('Advertiser System')

        def callback(self):
          if tkinter.messagebox.askokcancel("quit", "Do You really want to quit?"):
            root.destroy()

        def clear(self):
          e1.delete(0, END)
          e2.delete(0, END)
          e3.delete(0, END)
          e4.delete(0, END)

        def view_all():
          self.listing.delete(0, END)
          for row in backend.view():
            self.listing.insert(END, row)
          self.clear()

        def get_selected_row(self,event):
          global selected_tuple
          self.clear()
          index = self.listing.curselection()[0]
          selected_tuple = self.listing.get(index)
          e1.insert(END, selected_tuple[1])
          e2.insert(END, selected_tuple[3])
          e3.insert(END, selected_tuple[2])
          e4.insert(END, selected_tuple[4])


        def search():
          print(self.start_foll_txt.get(),self.end_foll_txt.get())
          self.listing.delete(0, END)
          search_data = backend.inf_search(self.start_foll_txt.get(),self.end_foll_txt.get(),self.inf_name_txt.get())
          print(search_data)
          if len(search_data) != 0:
            for row in search_data:
              self.listing.insert(END, row)
          else:
            tkinter.messagebox.showinfo('Message', 'NO RESULT FOUND')
            self.clear()

        selected_tuple = tuple()
        self.inf_name_txt = StringVar(root)
        self.inf_cat_txt = StringVar(root)
        self.adv_phone_txt = StringVar(root)
        self.comp_name_txt = StringVar(root)
        self.start_foll_txt = IntVar(root)
        self.end_foll_txt = IntVar(root)
        l = ttk.Label(root, text='Influencer Name', relief=RAISED)
        l.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Genre/Category', relief=RAISED)
        l.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')

        e1 = Entry(root, textvariable=self.inf_name_txt)
        e1.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')

        e2 = ttk.Combobox(root, textvariable=self.inf_cat_txt)
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

        l = ttk.Label(root, text='Start Range', relief=RAISED)
        l.grid(row=0, column=2, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='End Range', relief=RAISED)
        l.grid(row=1, column=2, padx=5, pady=5, sticky='nswe')
        e3 = Entry(root, textvariable=self.start_foll_txt)
        e3.grid(row=0, column=3, padx=5, pady=5, sticky='nswe')
        e4 = Entry(root, textvariable= self.end_foll_txt)
        e4.grid(row=1, column=3, padx=5, pady=5, sticky='nswe')

        b1 = ttk.Button(root, text='View All Influencers', command=lambda: view_all())
        b1.grid(row=2, column=3, padx=5, pady=5, rowspan=2, sticky='nswe')
        b2 = ttk.Button(root, text='Search Influencers', command=lambda: search())
        b2.grid(row=4, column=3, padx=5, pady=5, rowspan=2, sticky='nswe')
        b6 = ttk.Button(root, text='Exit', command=root.destroy)
        b6.grid(row=6, column=3, padx=5, pady=5, rowspan=2, sticky='nswe')

        self.listing = Listbox(root)
        self.listing.grid(row=2, column=0, rowspan=6, columnspan=3, padx=5, pady=5, sticky='nswe')
        self.listing.bind('<<ListboxSelect>>', get_selected_row)

        for i in range(4):
          root.grid_columnconfigure(i, weight=1)
        for i in range(8):
          root.grid_rowconfigure(i, weight=1)

        root.protocol("WM_DELETE_WINDOW", callback)
        root.mainloop()

