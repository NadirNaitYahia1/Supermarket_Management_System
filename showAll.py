import tkinter as tk
from tkinter import ttk



class ShowTable(tk.Toplevel):
    def __init__(self, master, models_instance, nosqlbd_instance, nameTable):
        super().__init__(master)
        self.title("Afficher Tous")
        self.geometry("600x400")
        self.models = models_instance
        self.nosqldb = nosqlbd_instance 
        self.label_font = ("Arial", 18) 
        self.entry_width = 20
        self.nameTable = nameTable

        if self.nameTable == "Supplier":
            self.tree = ttk.Treeview(self, columns=("idSupplier", "firstName", "lastName", "companyName"), show="headings")
            self.tree.heading("idSupplier", text="ID")
            self.tree.heading("firstName", text="Prénom")
            self.tree.heading("lastName", text="Nom")
            self.tree.heading("companyName", text="Nom de l'entreprise")
            data = models_instance.get_all_supplier()
            print('data',data)
            for row in data:
                self.tree.insert("", "end", values=row)
                self.tree.pack(expand=True, fill="both")

        elif self.nameTable == "ProductCategory":
            self.tree = ttk.Treeview(self, columns=("idCategory", "nameCategory"), show="headings")
            self.tree.heading("idCategory", text="ID")
            self.tree.heading("nameCategory", text="Nom de la catégorie")
            data = models_instance.get_all_product_category()
            print('data',data)
            for row in data:
                self.tree.insert("", "end", values=row)
                self.tree.pack(expand=True, fill="both")

        elif self.nameTable == "Products":
            self.tree = ttk.Treeview(self, columns=("idProduct", "nameProduct", "priceUnitaire", "categories"), show="headings")
            self.tree.heading("idProduct", text="ID")
            self.tree.heading("nameProduct", text="Nom du produit")
            self.tree.heading("priceUnitaire", text="Prix unitaire")
            self.tree.heading("categories", text="Catégories")
            # get data
            data = models_instance.get_all_products()
            print('data',data)
            for row in data:
                self.tree.insert("", "end", values=row)
                self.tree.pack(expand=True, fill="both")
        

        elif self.nameTable == "Delivery":
            self.tree = ttk.Treeview(self, columns=("idDelivery", "idSupplier", "idProduct", "dateOfDelivery", "priceOfDelivery", "quantity", "idInvoice"), show="headings")
            self.tree.heading("idDelivery", text="ID")
            self.tree.heading("idSupplier", text="ID du fournisseur")
            self.tree.heading("idProduct", text="ID du produit")
            self.tree.heading("dateOfDelivery", text="Date de livraison")
            self.tree.heading("priceOfDelivery", text="Prix de livraison")
            self.tree.heading("quantity", text="Quantité")
            self.tree.heading("idInvoice", text="ID de la facture")
            data = models_instance.get_all_deliveries()
            mongo_data = nosqlbd_instance.get_all_deliveries()
            for d in mongo_data:
                data.append((d["sqlID"], d["dateOfDelivery"], d["quantity"], d["idProduct"],None, d["quantity"]))
            print('data',data)
            for row in data:
                self.tree.insert("", "end", values=row)
                self.tree.pack(expand=True, fill="both")

        elif self.nameTable == "Sales":
            self.tree = ttk.Treeview(self, columns=("idSales", "idProduct", "dateOfSales", "priceOfSales", "quantity"), show="headings")
            self.tree.heading("idSales", text="ID")
            self.tree.heading("idProduct", text="ID du produit")
            self.tree.heading("dateOfSales", text="Date de vente")
            self.tree.heading("priceOfSales", text="Prix de vente")
            self.tree.heading("quantity", text="Quantité")
            data = models_instance.get_all_sales()
            mongo_data = nosqlbd_instance.get_all_sales()
            for d in mongo_data:
                data.append((d["sqlID"], d["dateOfSale"], d["priceOfSales"], d["quantity"]))
            print('data',data)
            for row in data:
                self.tree.insert("", "end", values=row)
                self.tree.pack(expand=True, fill="both")
        



  
 

        # Bouton de retour
        ttk.Button(self, text="Retour", command=self.back_to_home).pack(pady=10)

    def back_to_home(self):
        self.destroy()
        self.master.deiconify()
