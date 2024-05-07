import tkinter as tk
from tkinter import ttk
from showAll import ShowTable
 

class CategoriePage(tk.Toplevel):
    def __init__(self, master, models_instance, nosqlbd_instance):
        super().__init__(master)
        self.title("Categorie")
        self.geometry("600x400")
        self.models = models_instance
        self.nosqldb = nosqlbd_instance 
        self.label_font = ("Arial", 18) 
        self.entry_width = 20

        self.frame4 = ttk.Frame(self, padding=10)
        self.frame4.pack(padx=10, pady=10)
        self.label1 = ttk.Label(self.frame4, text="Categorie", font=self.label_font)
        self.label1.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        ttk.Label(self.frame4, text='Nom Categorie').grid(row=1, column=0)
        self.e41 = ttk.Entry(self.frame4, width=self.entry_width)
        self.e41.grid(row=1,column=1)
        ttk.Button(self, text="Retour à l'Accueil", command=self.back_to_home).pack(pady=10)
        ttk.Button(self.frame4, text='Ajouter', width=10, command=self.add_categorie ).grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(self.frame4, text='Rechercher', width=10).grid(row=2, column=3, padx=5, pady=5)
        ttk.Button(self.frame4, text='Supprimer', width=10).grid(row=3, column=3, padx=5, pady=5)
        ttk.Button(self.frame4, text='Afficher Tous', width=10, command=self.show_table).grid(row=4, column=3, padx=5, pady=5)
        ttk.Button(self.frame4, text='Reset', width=10,  ).grid(row=5, column=3, padx=5, pady=5)
    def back_to_home(self):
        self.destroy()
        self.master.deiconify()

    def reset_frame4(self):
        # Reset entry fields in frame 4
        self.e41.delete(0, tk.END)

    def add_categorie(self):
        name_categorie = self.e41.get()
        try:
            result = self.models.add_product_category(name_categorie)
            print(result)
        except Exception as e:
            print(e)
        self.reset_frame4()

    def show_table(self):
        self.withdraw()
        ShowTable(self, self.models, self.nosqldb,'ProductCategory')