from tkinter import *
import tkinter.messagebox
import adv_backend
from tkinter import ttk
from ttkthemes import themed_tk as tk
import backend

class make_contract:
    def __init__(self):
        root = tk.ThemedTk()
        root.get_themes()
        root.set_theme('radiance')
        root.title('Make a Contract')

        def callback():
          if tkinter.messagebox.askokcancel("quit", "Do You really want to quit?"):
            root.destroy()

        def clear():
          e1.delete(0, END)
          e2.delete(0, END)

        def add_entry():
            backend.con_insert(self.id_txt.get(),self.adv_id_txt.get(), self.inf_name_txt.get(), self.comp_name_txt.get(), self.inf_cat_txt.get(),
                           self.duration_txt.get(), self.budget_txt.get())
            self.listing.delete(0, END)
            self.listing.insert(END, (
                self.id_txt.get(),self.adv_id_txt.get(), self.inf_name_txt.get(), self.comp_name_txt.get(), self.inf_cat_txt.get(),
                self.duration_txt.get(), self.budget_txt.get()))

            clear()

        def view_all():
          self.listing.delete(0, END)
          for row in backend.view():
            self.listing.insert(END, row)
          clear()

        def get_selected_row(event):
          global selected_tuple
          clear()
          index = self.listing.curselection()[0]
          selected_tuple = self.listing.get(index)
          e2.insert(END, selected_tuple[0])
          e1.insert(END, selected_tuple[1])

        def tcontract():
            search_data = backend.inf_cont(self.id_txt.get())
            e2.insert(0, search_data)

        def view_all():
            self.listing.delete(0, END)
            for row in backend.view():
                self.listing.insert(END, row)
            clear()


        selected_tuple = tuple()
        self.inf_name_txt = StringVar(root)
        self.inf_cat_txt = StringVar(root)
        self.adv_id_txt = IntVar(root)
        self.comp_name_txt = StringVar(root)
        self.duration_txt = StringVar(root)
        self.budget_txt = IntVar(root)
        self.id_txt = IntVar(root)

        l = ttk.Label(root, text='Select influencer', relief=RAISED)
        l.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Influencer Name', relief=RAISED)
        l.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Influencer ID', relief=RAISED)
        l.grid(row=2, column=0, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Company Name', relief=RAISED)
        l.grid(row=3, column=0, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Influencer Category', relief=RAISED)
        l.grid(row=2, column=0, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Enter Budget', relief=RAISED)
        l.grid(row=2, column=2, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Duration', relief=RAISED)
        l.grid(row=1, column=2, padx=5, pady=5, sticky='nswe')
        l = ttk.Label(root, text='Advertiser ID', relief=RAISED)
        l.grid(row=3, column=2, padx=5, pady=5, sticky='nswe')

        e1 = ttk.Entry(root, textvariable=self.inf_name_txt)
        e1.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')
        e3 = ttk.Entry(root, textvariable=self.comp_name_txt)
        e3.grid(row=3, column=1, padx=5, pady=5, sticky='nswe')
        e5 = ttk.Entry(root, textvariable=self.budget_txt)
        e5.grid(row=2, column=3, padx=5, pady=5, sticky='nswe')
        e6 = ttk.Combobox(root, textvariable=self.duration_txt)
        e6.grid(row=1, column=3, padx=5, pady=5, sticky='nswe')
        e6['values'] = ('3 Months',
                        '6 Months',
                        '12 Months',
                        '24 Months',
                        )

        e2 = ttk.Combobox(root, textvariable=self.id_txt)
        e2['values'] = backend.view_cont()
        e2.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')
        e2.current(0)
        e4 = ttk.Combobox(root, textvariable=self.inf_cat_txt)
        e4['values'] = ('Select Category',
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
        e4.grid(row=2, column=1, padx=5, pady=5, sticky='nswe')
        e4.current(0)

        e7 = ttk.Entry(root, textvariable=self.adv_id_txt)
        e7.grid(row=3, column=3, padx=5, pady=5, sticky='nswe')

        b1 = ttk.Button(root, text='View All Influencers', command=lambda: view_all())
        b1.grid(row=0, column=2, padx=5, pady=5, sticky='nswe')
        b2 = ttk.Button(root, text='Enter Contract', command=lambda: add_entry())
        b2.grid(row=0, column=3, padx=5, pady=5, sticky='nswe')
        b3 = ttk.Button(root, text='Exit', command=root.destroy)
        b3.grid(row=7, column=3, padx=5, pady=5, sticky='nswe')


        self.listing = Listbox(root)
        self.listing.grid(row=6, column=0, rowspan=1, padx=2, pady=2, sticky='nswe')
        self.listing.bind('<<ListboxSelect>>', get_selected_row)

        for i in range(4):
          root.grid_columnconfigure(i, weight=1)
        for i in range(8):
          root.grid_rowconfigure(i, weight=1)

        root.protocol("WM_DELETE_WINDOW", callback)
        root.mainloop()

