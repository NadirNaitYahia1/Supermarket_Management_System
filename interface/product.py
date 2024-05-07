from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from showAll import ShowTable
 

class ProductsPage(tk.Toplevel):
    def __init__(self, master, models_instance, nosqlbd_instance):
        super().__init__(master)
        self.title("Produits")
        self.geometry("600x400")
        self.models = models_instance
        self.nosqldb = nosqlbd_instance 
        self.label_font = ("Arial", 18) 
        self.entry_width = 20
        self.nameTable = 'Products'



        self.frame1 = ttk.Frame(self, padding=10)
        self.frame1.pack(padx=10, pady=10)

        self.label1 = ttk.Label(self.frame1, text="Produits", font=self.label_font)
        self.label1.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(self.frame1, text='Nom Du Produit').grid(row=1, column=0)
        ttk.Label(self.frame1, text='Catégorie').grid(row=2, column=0)
        ttk.Label(self.frame1, text='Prix Unitaire').grid(row=3, column=0)
        # ttk.Label(self.frame1, text='Etat du Paiement').grid(row=5, column=0)
        ttk.Label(self.frame1, text='Image').grid(row=6, column=0)

        ttk.Button(self.frame1, text='Ajouter', width=10, command=self.add_product).grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(self.frame1, text='Rechercher', width=10).grid(row=2, column=3, padx=5, pady=5)
        ttk.Button(self.frame1, text='Supprimer', width=10).grid(row=3, column=3, padx=5, pady=5)
        ttk.Button(self.frame1, text='Afficher Tous', width=10, command=self.show_table).grid(row=4, column=3, padx=5, pady=5)
        ttk.Button(self.frame1, text='Reset', width=10, command=self.reset_frame1).grid(row=5, column=3, padx=5, pady=5)

        self.e1 = ttk.Entry(self.frame1, width=self.entry_width)
        self.e2 =   ttk.Combobox(self.frame1, values=self.get_categories_names()) 
        self.e3 = ttk.Entry(self.frame1, width=self.entry_width)
        
        self.e1.grid(row=1, column=1, padx=5, pady=5)
        self.e2.grid(row=2, column=1, padx=5, pady=5)
        self.e3.grid(row=3, column=1, padx=5, pady=5)
        
        self.file_entry = ttk.Entry(self.frame1, width=30, state='disabled')
        self.file_entry.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
        ttk.Button(self.frame1, text='Browse', command=self.browse_file).grid(row=7, column=0, columnspan=2, pady=5)

        ttk.Button(self, text="Retour à l'Accueil", command=self.back_to_home).pack(pady=10)

    def back_to_home(self):
        self.destroy()
        self.master.deiconify()

        #  ___________________________________________________________________________________________________________________________

    # def save_image()

    def get_categories_names(self):
        categories = self.models.get_all_product_category()
        categories = [category[1] for category in categories]
        return categories
    
    def get_category_id_by_name(self, name):
        categories = self.models.get_all_product_category()
        for category in categories:
            if category[1] == name:
                return category[0]
        return None
    
    def save_image(self, idProduct):
        path = self.file_path
        with open(path, "rb") as f:
            data = f.read()
            try:
                self.nosqldb.add_product_image(idProduct, self.e1.get(), path, data)
                print('Image saved')
            except:
                print('Image not saved')
    def add_product(self):
        name = self.e1.get()
        category = self.get_category_id_by_name(self.e2.get())
        price = self.e3.get()
        image = self.file_path
        if name and category and price and image:
            result = self.models.add_product(name, category, price)
            if result:
                self.save_image(result["id"])
                print('Product added successfully')
            self.reset_frame1()
        else:
            print('All fields are required')

    # add_product(self, nameProduct, categories, priceUnitaire):
   
    def toggle_entry(self):
        if self.choice.get():
            self.e4.config(state='normal')   
        else:
            self.e4.config(state='disabled')  
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path = file_path
        if file_path:
                    self.file_entry.config(state='normal')  
                    self.file_entry.delete(0, tk.END)   
                    self.file_entry.insert(0, file_path)  
                    self.file_entry.config(state='disabled')
    def reset_frame1(self):
        # Reset entry fields in frame 1
        self.e1.delete(0, tk.END)
        self.e2.delete(0, tk.END)
        self.e3.delete(0, tk.END)
        self.file_entry.config(state='normal')
        self.file_entry.delete(0, tk.END)
        self.file_entry.config(state='disabled')

    def reset_frame2(self):
        # Reset entry fields in frame 2
        self.e7.delete(0, tk.END)
        self.e8.delete(0, tk.END)

    def show_table(self):
        self.withdraw()
        ShowTable(self, self.models, self.nosqldb,self.nameTable)  
