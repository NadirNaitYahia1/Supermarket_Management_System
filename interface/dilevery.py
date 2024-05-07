from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from showAll import ShowTable 
from db.archieve import *


class DeliveryPage(tk.Toplevel):
    def __init__(self, master, models_instance, nosqlbd_instance):
        super().__init__(master)
        self.title("Livraison")
        self.geometry("600x400")
        self.models = models_instance
        self.nosqldb = nosqlbd_instance 
        self.label_font = ("Arial", 18) 
        self.entry_width = 20

        self.frame5 = ttk.Frame(self, padding=10)
        self.frame5.pack(padx=10, pady=10)
        self.label1 = ttk.Label(self.frame5, text="Livraison", font=self.label_font)
        self.label1.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(self.frame5, text='Produit').grid(row=1, column=0)
        self.e51 =   ttk.Combobox(self.frame5, values=self.get_product_names())
        self.e51.grid(row=1,column=1)

        ttk.Label(self.frame5, text='Fournisseur').grid(row=2, column=0)
        self.e52 =   ttk.Combobox(self.frame5, values=self.get_supplier_names())
        self.e52.grid(row=2,column=1)
    
        ttk.Label(self.frame5, text='Date de Livraison').grid(row=3, column=0)
        self.e53 =   ttk.Entry(self.frame5, width=self.entry_width)
        self.e53.grid(row=3,column=1)

        ttk.Label(self.frame5, text='Prix').grid(row=4, column=0)
        self.e54 =   ttk.Entry(self.frame5, width=self.entry_width)
        self.e54.grid(row=4,column=1)

        ttk.Label(self.frame5, text='Quantitie').grid(row=5, column=0)
        self.e55 =   ttk.Entry(self.frame5, width=self.entry_width)
        self.e55.grid(row=5,column=1)

        ttk.Label(self.frame5, text='Invoice').grid(row=6, column=0)
        self.file_entry = ttk.Entry(self.frame5, width=30, state='disabled')
        self.file_entry.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
        ttk.Button(self.frame5, text='Browse', command=self.browse_file).grid(row=7, column=0, columnspan=2, pady=5)

        ttk.Button(self, text="Retour à l'Accueil", command=self.back_to_home).pack(pady=10)
        ttk.Button(self.frame5, text='Ajouter', width=10,  command=self.add_delivery).grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(self.frame5, text='Rechercher', width=10).grid(row=2, column=3, padx=5, pady=5)
        ttk.Button(self.frame5, text='Supprimer', width=10).grid(row=3, column=3, padx=5, pady=5)
        ttk.Button(self.frame5, text='Afficher Tous', width=10, command=self.show_table).grid(row=4, column=3, padx=5, pady=5)
        ttk.Button(self.frame5, text='Reset', width=10,  ).grid(row=5, column=3, padx=5, pady=5)
        ttk.Button(self.frame5, text='Migrate', width=10,  command=self.migrate_deliveries).grid(row=6, column=3, padx=5, pady=5)
    
    def back_to_home(self):
        self.destroy()
        self.master.deiconify()

    def get_supplier_names(self):
        suppliers = self.models.get_all_supplier()
        suppliers = [supplier[1]+" " + supplier[2] for supplier in suppliers]
        return suppliers
    
    def get_supplier_id_by_name(self, name):
        name = name.split(' ')
        suppliers = self.models.get_all_supplier()
        for supplier in suppliers:
            if supplier[1] == name[0] and supplier[2] == name[1]:
                return supplier[0]
        return None
    
    def reset_frame5(self):
        self.e51.delete(0, tk.END)
        self.e52.delete(0, tk.END)
        self.e53.delete(0, tk.END)
        self.e54.delete(0, tk.END)
        self.e55.delete(0, tk.END)


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
    
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path = file_path
        if file_path:
            self.file_entry.config(state='normal')  
            self.file_entry.delete(0, tk.END)   
            self.file_entry.insert(0, file_path)  
            self.file_entry.config(state='disabled')
    # def add_delivery(self, idSupplier, idProduct, dateOfDelivery, priceOfDelivery, quantity):
    # def add_invoice(self, idDelivery, file_name, file_path, file_data):
    def save_pdf(self, idDelivery):
        path = self.file_path
        with open(path, "rb") as f:
            data = f.read()
            try:
                self.nosqldb.add_invoice(idDelivery, self.e51.get(), path, data)
                print('Invoice saved')
            except:
                print('Invoice not saved')

    def add_delivery(self):
        product = self.get_product_id_by_name(self.e51.get())
        supplier = self.get_supplier_id_by_name(self.e52.get())
        date = self.e53.get()
        price = self.e54.get()
        quantity = self.e55.get()
        try:
            if not product or not supplier or not date or not price or not quantity:
                raise Exception('All fields are required')
            result = self.models.add_delivery(supplier, product, date, price, quantity)
            if result:
                self.save_pdf(result["id"])

            print('Delivery added successfully')
        except:
            print('All fields are required')
        self.reset_frame5() 



    def migrate_deliveries(self):
        archieve_deliveries()
        print('Deliveries migrated successfully')


    def show_table(self):
        self.withdraw()
        ShowTable(self, self.models, self.nosqldb, 'Delivery')