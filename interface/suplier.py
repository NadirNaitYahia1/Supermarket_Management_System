import tkinter as tk
from tkinter import ttk
from showAll import ShowTable 

class VendorsPage(tk.Toplevel):
    def __init__(self, master, models_instance, nosqlbd_instance):
        super().__init__(master)
        self.title("Fournisseurs")
        self.geometry("600x400")
        self.models = models_instance
        self.nosqldb = nosqlbd_instance 
        self.entry_width = 20

        self.frame2 = ttk.Frame(self, padding=10)
        self.frame2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.nameTable = 'Supplier'

        self.label2 = ttk.Label(self, text="Fournisseur", font=("Arial", 18))
        self.label2.grid(row=0, column=0, columnspan=3)


        ttk.Label(self.frame2, text='Nom du Fournisseur').grid(row=2, column=0)
        ttk.Label(self.frame2, text='Prenom du Fournisseur').grid(row=3, column=0)
        ttk.Label(self.frame2, text='Nom  entreprise').grid(row=4, column=0)

        self.e7 = ttk.Entry(self.frame2, width=20)
        self.e7.grid(row=2, column=1)
        self.e8 = ttk.Entry(self.frame2, width=20)
        self.e8.grid(row=3, column=1)
        self.e21 = ttk.Entry(self.frame2, width=20)
        self.e21.grid(row=4, column=1)

        ttk.Button(self.frame2, text='Ajouter', width=10, command=self.add_vendor).grid(row=1, column=3, padx=5, pady=5)
        ttk.Button(self.frame2, text='Rechercher', width=10).grid(row=2, column=3, padx=5, pady=5)
        ttk.Button(self.frame2, text='Supprimer', width=10).grid(row=3, column=3, padx=5, pady=5)
        ttk.Button(self.frame2, text='Afficher Tous', width=10,command=self.show_table).grid(row=4, column=3, padx=5, pady=5)
        ttk.Button(self.frame2, text='Reset', width=10, command=self.reset_frame2).grid(row=5, column=3, padx=5, pady=5)

        ttk.Button(self, text="Retour à l'Accueil", command=self.back_to_home).grid(row=2, column=1, columnspan=3, pady=10)

    def back_to_home(self):
        self.destroy()
        self.master.deiconify()

    def add_vendor(self):
        name_vendor = self.e7.get()
        first_name_vendor = self.e8.get()
        company_name = self.e21.get()
        try:
            result = self.models.add_supplier(name_vendor, first_name_vendor, company_name)
            print(result)
        except Exception as e:
            print(e)
        self.reset_frame2()  
    def reset_frame2(self):
        # Reset entry fields in frame 2
        self.e7.delete(0, tk.END)
        self.e8.delete(0, tk.END)  

    def show_table(self):
        self.withdraw()
        ShowTable(self, self.models, self.nosqldb,self.nameTable)  
