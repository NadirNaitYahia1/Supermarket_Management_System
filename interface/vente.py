import tkinter as tk
from tkinter import ttk
from showAll import ShowTable 
from db.archieve import *

class SalesPage(tk.Toplevel):
    def __init__(self, master, models_instance, nosqlbd_instance):
        super().__init__(master)
        self.title("Ventes")
        self.geometry("600x400")
        self.models = models_instance
        self.nosqldb = nosqlbd_instance 
        self.entry_width = 20
        self.nameTable = 'Sales'
        self.frame3 = ttk.Frame(self, padding=10)
        self.frame3.grid(row=0, column=2, padx=10, pady=10)

        self.label3 = ttk.Label(self.frame3, text="Ventes", font=("Arial", 18))
        self.label3.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(self.frame3, text='Produit').grid(row=1, column=0)
        self.listeProducts  = ttk.Combobox(self.frame3, values=self.get_product_names())
        self.listeProducts.grid(row=1, column=1)

        ttk.Label(self.frame3, text='Date du Ventes').grid(row=2, column=0)
        ttk.Label(self.frame3, text='Prix').grid(row=3, column=0)
        ttk.Label(self.frame3, text='Quantité').grid(row=4, column=0)
         


        ttk.Button(self.frame3, text='Ajouter', width=10, command=self.add_sales).grid(row=1, column=4, padx=5, pady=5)
        ttk.Button(self.frame3, text='Rechercher', width=10).grid(row=2, column=4, padx=5, pady=5)
        ttk.Button(self.frame3, text='Supprimer', width=10).grid(row=3, column=4, padx=5, pady=5)
        ttk.Button(self.frame3, text='Afficher Tous', width=10, command=self.show_table).grid(row=4, column=4, padx=5, pady=5)
        ttk.Button(self.frame3, text='Reset', width=10, command=self.reset_frame3).grid(row=5, column=4, padx=5, pady=5)
        ttk.Button(self.frame3, text="Archiver", width=10, command=self.archieve()).grid(row=6,column=4, padx=5, pady=5)
        
        self.e10 = ttk.Entry(self.frame3, width=self.entry_width )
        self.e11 = ttk.Entry(self.frame3, width=self.entry_width)
        self.e12 = ttk.Entry(self.frame3, width=self.entry_width)
        self.e10.grid(row=2, column=1, padx=5, pady=5)
        self.e11.grid(row=3, column=1, padx=5, pady=5)
        self.e12.grid(row=4, column=1, padx=5, pady=5)
        


        ttk.Button(self, text="Retour à l'Accueil", command=self.back_to_home).grid(row=4,column=2)

    def back_to_home(self):
        self.destroy()
        self.master.deiconify()
    def reset_frame3(self):
        self.listeProducts.delete(0,tk.END)
        self.e10.delete(0, tk.END)
        self.e11.delete(0, tk.END)

    def get_product_names(self):
        products = self.models.get_all_products()
        products = [product[1] for product in products]
        return products
    
    def get_product_id_by_name(self, name):
        products = self.models.get_all_products()
        for product in products:
            if product[1] == name:
                return product[0]
        return None
    
    def add_sales(self):
        product = self.get_product_id_by_name(self.listeProducts.get())
        date = self.e10.get()
        price = self.e11.get()
        quantity = self.e12.get()
        if product and date and price:
            self.models.add_sales(product, date, price,quantity)
            print("Sales added successfully")
            self.reset_frame3()
        else:
            print("All fields are required")

    def archieve(self):
        archieve_sales()
        print("Data archieved successfully")

    def show_table(self):
        self.withdraw()
        ShowTable(self, self.models, self.nosqldb,self.nameTable)  
