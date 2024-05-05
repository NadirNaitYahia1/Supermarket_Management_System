import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import filedialog
import pymongo


class Models:
    def __init__(self, db_name='db'):
        self.db_name = db_name
        self.connection = mysql.connector.connect(host='localhost', user='root', password='')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE DATABASE IF NOT EXISTS {}
        '''.format(self.db_name))
        self.create_tables()
        print('sql db created great')


    def create_tables(self):
        self.connection.database = self.db_name
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vendor (
                idVendor INT AUTO_INCREMENT PRIMARY KEY,
                nameVendor VARCHAR(20),
                firstNameVendor VARCHAR(20)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                idProduct INT AUTO_INCREMENT PRIMARY KEY,
                nameProduct VARCHAR(20),
                categories VARCHAR(20),
                priceUnitaire INT,
                idVendor INT,
                FOREIGN KEY (idVendor) REFERENCES Vendor(idVendor)
            )
        ''')
        self.connection.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Deliver (
                idDeliver INT AUTO_INCREMENT PRIMARY KEY,
                idVendor INT,
                idProduct INT,
                date VARCHAR(20),
                FOREIGN KEY (idVendor) REFERENCES Vendor(idVendor),
                FOREIGN KEY (idProduct) REFERENCES Products(idProduct)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sales (
                idSales INT AUTO_INCREMENT PRIMARY KEY,
                idProduct INT,
                dateOfSales VARCHAR(20),
                priceOfSales INT,
                FOREIGN KEY (idProduct) REFERENCES Products(idProduct)
            )
        ''')
        print('tabels crated great')
        self.connection.commit()

    def add_vendor(self, nameVendor, firstNameVendor):
        if (nameVendor.strip() and firstNameVendor.strip() ):
            sql = "INSERT INTO Vendor (nameVendor, firstNameVendor) VALUES (%s, %s)"
            params = (nameVendor, firstNameVendor)
            try:
                self.cursor.execute(sql, params)
                self.connection.commit()
                return {"msg": "Succès: fournisseur ajouté", "status": 200}
            except Exception as e:
                print("Error:", e)
                return {"msg": "Échec: fournisseur non ajouté", "status": 400}
        else:
            print('write the name and the firstname')

            # CREATE TABLE IF NOT EXISTS Products (
            #     idProduct INT AUTO_INCREMENT PRIMARY KEY,
            #     nameProduct VARCHAR(20),
            #     categories VARCHAR(20),
            #     priceUnitaire INT,
            #     idVendor INT,
            #     FOREIGN KEY (idVendor) REFERENCES Vendor(idVendor)
            # )


    def add_product(self, nameProduct, categories, priceUnitaire,idVendor):
        sql = "INSERT INTO Products (nameProduct, categories, priceUnitaire,idVendor) VALUES (%s, %s, %s,%s)"
        params = (nameProduct, categories, priceUnitaire,idVendor)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: produit ajouté", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: produit non ajouté", "status": 400}

    def add_sales(self, idProduct, dateOfSales,priceOfSales):
        print('im here')
        print(dateOfSales)
        sql = "INSERT INTO Sales (idProduct, dateOfSales, priceOfSales) VALUES (%s, %s, %s)"
        params = (idProduct, dateOfSales,priceOfSales)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: vente ajoute", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: vente non ajouté", "status": 400}
        
    def get_vendor(self):
        sql ="select * from Vendor"
        try :
            self.cursor.execute(sql)
            vendors = self.cursor.fetchall()
            return vendors
        except:
            print("Error:", e)
            return None
   
    def get_products(self):
        sql ="select * from Products"
        try :
            self.cursor.execute(sql)
            products = self.cursor.fetchall()
            return products
        except:
            print("Error:", e)
            return None



    def close_connection(self):
        self.connection.close()
 

class NosqlModel: 
    def __init__(self):
        try:
            self.client =pymongo.MongoClient("mongodb://localhost:27017/")
            self.db = self.client["NoSQlDb"]
            self.collection =self.db["Invoice"]
            self.collection.insert_one({"azul":"azyl"})
            print('no sql db created great')
        except: 
            print('error no sql not created')
    def add_invoice(self,idVendor,file_name,file_path,file_data): 
        document ={"idVendo":idVendor,"file_name":file_name,"file_path":file_path,
                   "file_data":file_data}
        try:
            self.collection.insert_one(document)
            print("file added")
        except:
            print('file not added error')



class SuperMarketManagerApp:
    def __init__(self, master, models_instance,nosqlbd_instance):
        self.master = master
        self.models = models_instance
        self.nosqldb=nosqlbd_instance

       
        self.style = ttk.Style()
        self.style.theme_use("clam")   

       
        self.label_font = ("Arial", 20)
        self.entry_width = 25
        self.button_padx = 10
        self.button_pady = 5

# _________________________________________________________________________________________
        self.frame1 = ttk.Frame(master, padding=10)
        self.frame1.grid(row=0, column=0, padx=10, pady=10)

        self.label1 = ttk.Label(self.frame1, text="Produits", font=self.label_font)
        self.label1.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(self.frame1, text='Nom Du Produit').grid(row=1, column=0)
        ttk.Label(self.frame1, text='Catégorie').grid(row=2, column=0)
        ttk.Label(self.frame1, text='Prix Unitaire').grid(row=3, column=0)
        ttk.Label(self.frame1, text='Fournisseur').grid(row=4, column=0)
        ttk.Label(self.frame1, text='Etat du Paiement').grid(row=5, column=0)
        ttk.Label(self.frame1, text='Facture').grid(row=6, column=0)

        ttk.Button(self.frame1, text='Ajouter', width=10, command=self.add_product).grid(row=1, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame1, text='Rechercher', width=10).grid(row=2, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame1, text='Supprimer', width=10).grid(row=3, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame1, text='Afficher Tous', width=10).grid(row=4, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame1, text='Reset', width=10,command=self.reset_frame1).grid(row=4, column=3, padx=self.button_padx, pady=self.button_pady)

        self.e1 = ttk.Entry(self.frame1, width=self.entry_width)
        self.e2 = ttk.Entry(self.frame1, width=self.entry_width)
        self.e3 = ttk.Entry(self.frame1, width=self.entry_width)
        self.listeCombo  = ttk.Combobox(self.frame1, values=self.models.get_vendor())
        


        self.e1.grid(row=1, column=1, padx=5, pady=5)
        self.e2.grid(row=2, column=1, padx=5, pady=5)
        self.e3.grid(row=3, column=1, padx=5, pady=5)
        self.listeCombo.grid(row=4, column=1, padx=5, pady=5)
        self.choice = tk.BooleanVar()
        self.e4 =ttk.Checkbutton(self.frame1, text='Effectuer', variable=self.choice, command=self.toggle_entry)
        self.e4.grid(row=5, column=1, columnspan=1, pady=5, sticky=tk.W)
        
        

        # Entry widget for file path (initially disabled)
        self.file_entry = ttk.Entry(self.frame1, width=30, state='disabled')
        self.file_entry.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
        ttk.Button(self.frame1, text='Browse', command=self.browse_file).grid(row=7, column=0, columnspan=2, pady=5 ,)
 


   

# __________________________________________________________________________________
        self.frame2 = ttk.Frame(master, padding=10)
        self.frame2.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = ttk.Label(self.frame2, text="Fournisseur", font=self.label_font)
        self.label2.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(self.frame2, text='Nom du Fournisseur').grid(row=1, column=0)
        ttk.Label(self.frame2, text='Prenom du Fournisseur').grid(row=2, column=0)

        ttk.Button(self.frame2, text='Ajouter', width=10, command=self.add_vendor).grid(row=1, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame2, text='Rechercher', width=10).grid(row=2, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame2, text='Supprimer', width=10).grid(row=3, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame2, text='Afficher Tous', width=10).grid(row=4, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame2, text='Reset', width=10,command=self.reset_frame2).grid(row=4, column=3, padx=self.button_padx, pady=self.button_pady)

        self.e7 = ttk.Entry(self.frame2, width=self.entry_width)
        self.e8 = ttk.Entry(self.frame2, width=self.entry_width)

        self.e7.grid(row=1, column=1, padx=5, pady=5)
        self.e8.grid(row=2, column=1, padx=5, pady=5)

# _________________________________________________________________________________
        self.frame3 = ttk.Frame(master, padding=10)
        self.frame3.grid(row=0, column=2, padx=10, pady=10)

        self.label3 = ttk.Label(self.frame3, text="Ventes", font=self.label_font)
        self.label3.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        ttk.Label(self.frame3, text='Produit').grid(row=1, column=0)
        self.listeProducts  = ttk.Combobox(self.frame3, values=self.models.get_products())
        self.listeProducts.grid(row=1, column=1)

        ttk.Label(self.frame3, text='Date du Ventes').grid(row=2, column=0)
        ttk.Label(self.frame3, text='Prix').grid(row=3, column=0)
 
                
 
        ttk.Button(self.frame3, text='Ajouter', width=10,command=self.add_sales).grid(row=1, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame3, text='Rechercher', width=10).grid(row=2, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame3, text='Supprimer', width=10).grid(row=3, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame3, text='Afficher Tous', width=10).grid(row=4, column=3, padx=self.button_padx, pady=self.button_pady)
        ttk.Button(self.frame3, text='Reset', width=10 ,command=self.reset_frame3).grid(row=4, column=3, padx=self.button_padx, pady=self.button_pady)
        
        self.e10 = ttk.Entry(self.frame3, width=self.entry_width )
        self.e11 = ttk.Entry(self.frame3, width=self.entry_width)

        # self.e10.grid(row=1, column=1, padx=5, pady=5)
        self.e10.grid(row=2, column=1, padx=5, pady=5)
        self.e11.grid(row=3, column=1, padx=5, pady=5)

# ___________________________________________________________________________________________________________
        self.frame4 = ttk.Frame(master, padding=10)
        self.frame4.grid(row=1, columnspan=4, padx=10, pady=10)

        self.label4 = ttk.Label(self.frame4, text="Affichage des Données", font=self.label_font)
        self.label4.grid(row=0, column=0, pady=(0, 10))

        self.textbox = tk.Text(self.frame4, height=10, width=50)
        self.textbox.grid(row=1, column=0, padx=10, pady=10)
# ________________________________________________________________________________________________________________
    def add_vendor(self):
        name_vendor = self.e7.get()
        first_name_vendor = self.e8.get()
        result = self.models.add_vendor(name_vendor, first_name_vendor)
        print(result)
        self.reset_frame2()    

    def add_sales(self):
        idProduct = self.listeProducts.get().split(' ')[0]
        dateOfSales = self.e10.get()
        priceOfSales = self.e11.get()
        print(idProduct,dateOfSales,priceOfSales)
        result = self.models.add_sales(idProduct, dateOfSales,priceOfSales)
        print(result)
        self.reset_frame3()    

    def add_product(self):
        name_product = self.e1.get()
        categories = self.e2.get()
        price_unitaire = self.e3.get()
        idVendor = self.listeCombo.get().split(' ')[0]
        result = self.models.add_product(name_product, categories, price_unitaire,idVendor)
        if self.file_path: 
            with open(self.file_path, "rb") as file:
                file_data = file.read()
                vendor_id = 1  
                file_name = self.file_path.split("/")[-1] 
            self.nosqldb.add_invoice(vendor_id, file_name, self.file_path, file_data)
            self.reset_frame1()    
        print(result)   
   
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
        self.listeCombo.set('')  # Reset the combobox selection
        self.file_entry.config(state='normal')
        self.file_entry.delete(0, tk.END)
        self.file_entry.config(state='disabled')

    def reset_frame2(self):
        # Reset entry fields in frame 2
        self.e7.delete(0, tk.END)
        self.e8.delete(0, tk.END)

    def reset_frame3(self):
        # Reset entry fields in frame 3
        self.listeProducts.delete(0,tk.END)
        self.e10.delete(0, tk.END)
        self.e11.delete(0, tk.END)


    

def main():
    db_models = Models()
    nosqlbd =NosqlModel()
    root = tk.Tk()
    app = SuperMarketManagerApp(root, db_models,nosqlbd)
    root.mainloop()

if __name__ == "__main__":
    main()
