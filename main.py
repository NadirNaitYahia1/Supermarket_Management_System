import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import filedialog
import pymongo
from interface.vente import SalesPage
from interface.product import ProductsPage
from interface.dilevery import DeliveryPage
from interface.categorie import CategoriePage
from interface.suplier import VendorsPage
from db.sql import Models
from db.mongo import NosqlModel
# from db.archieve import
 


class HomePage(tk.Tk):
    def __init__(self, master, menubar,models_instance,nosqlbd_instance):
        super().__init__()
        self.title("Gestionnaire de Supermarché")
        self.geometry("600x400")
        self.nosqldb=nosqlbd_instance
        self.models = models_instance


        self.label = ttk.Label(self, text="Bienvenue dans le Gestionnaire de Supermarché", font=("Arial", 18))
        self.label.pack(pady=20)

        ttk.Button(self, text="Produits", command=self.open_products).pack(pady=10)
        ttk.Button(self, text="Fournisseurs", command=self.open_vendors).pack(pady=10)
        ttk.Button(self, text="Ventes", command=self.open_sales).pack(pady=10)
        ttk.Button(self, text="Categorie", command=self.open_categorie).pack(pady=10)
        ttk.Button(self, text="Livraison", command=self.open_delivery).pack(pady=10)

    def open_categorie(self): 
        self.withdraw()
        CategoriePage(self, self.models, self.nosqldb)
    def open_products(self):
        self.withdraw()
        ProductsPage(self, self.models, self.nosqldb)

    def open_vendors(self):
        self.withdraw()
        VendorsPage(self, self.models, self.nosqldb)

    def open_sales(self):
        self.withdraw()
        SalesPage(self, self.models, self.nosqldb)
    def open_delivery(self):
        self.withdraw()
        DeliveryPage(self, self.models, self.nosqldb)


    def back_to_home(self):
        self.destroy()
        self.master.deiconify()





def main():
    db_models = Models()
    nosqlbd = NosqlModel()
    app = HomePage(None, None, db_models, nosqlbd)    
    app.mainloop()

if __name__ == "__main__":
    main()