import mysql.connector
class Models:
    def __init__(self, db_name='SuperMarketDb'):
        self.db_name = db_name
        self.connection = mysql.connector.connect(host='localhost',port=3306, user='root', password='')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE DATABASE IF NOT EXISTS {}
        '''.format(self.db_name))
        self.create_tables()
        print('sql db created great')


    def create_tables(self):
        self.connection.database = self.db_name
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Supplier (
                idSupplier INT AUTO_INCREMENT PRIMARY KEY,
                firstName VARCHAR(50) NOT NULL,
                lastName VARCHAR(50) NOT NULL,
                companyName VARCHAR(50) NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ProductCategory (
                idCategory INT AUTO_INCREMENT PRIMARY KEY,
                nameCategory VARCHAR(50) NOT NULL
            )
        """)

        self.connection.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                idProduct INT AUTO_INCREMENT PRIMARY KEY,
                nameProduct VARCHAR(20),
                priceUnitaire INT,
                categories INT,
                image VARCHAR(100),
                FOREIGN KEY (categories) REFERENCES ProductCategory(idCategory)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Delivery (
                idDelivery INT AUTO_INCREMENT PRIMARY KEY,
                idSupplier INT,
                idProduct INT,
                dateOfDelivery VARCHAR(20),
                priceOfDelivery INT,
                quantity INT,
                idInvoice INT,
                FOREIGN KEY (idSupplier) REFERENCES Supplier(idSupplier),
                FOREIGN KEY (idProduct) REFERENCES Products(idProduct)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sales (
                idSales INT AUTO_INCREMENT PRIMARY KEY,
                idProduct INT,
                dateOfSales VARCHAR(20),
                priceOfSales INT,
                quantity INT,
                FOREIGN KEY (idProduct) REFERENCES Products(idProduct)
            )
        ''')
        print('tabels crated great')
        self.connection.commit()

    def add_supplier(self, firstName, lastName, companyName):
        sql = "INSERT INTO Supplier (firstName, lastName, companyName) VALUES (%s, %s, %s)"
        params = (firstName, lastName, companyName)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: fournisseur ajouté", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: fournisseur non ajouté", "status": 400}
        
    def get_all_supplier(self):
        sql ="select * from Supplier"
        try :
            self.cursor.execute(sql)
            suppliers = self.cursor.fetchall()
            return suppliers
        except Exception as e:
            print("Error:", e)
            return None

    def get_supplier(self, idSupplier):
        sql = "SELECT * FROM Supplier WHERE idSupplier = %s"
        params = (idSupplier,)
        try:
            self.cursor.execute(sql, params)
            supplier = self.cursor.fetchone()
            return supplier
        except Exception as e:
            print("Error:", e)
            return None
        

    def search_supplier(self, str):
        sql = "SELECT * FROM Supplier WHERE firstName LIKE %s OR lastName LIKE %s OR companyName LIKE %s"
        params = (str, str, str)
        try:
            self.cursor.execute(sql, params)
            suppliers = self.cursor.fetchall()
            return suppliers
        except Exception as e:
            print("Error:", e)
            return None



    def drop_supplier(self, idSupplier):
        sql = "DELETE FROM Supplier WHERE idSupplier = %s"
        params = (idSupplier,)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: fournisseur supprimé", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: fournisseur non supprimé", "status": 400}
        
    def add_product_category(self, nameCategory):
        sql = "INSERT INTO ProductCategory (nameCategory) VALUES (%s)"
        params = (nameCategory,)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: catégorie ajoutée", "status": 200, "id": self.cursor.lastrowid}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: catégorie non ajoutée", "status": 400}
    
    def get_all_product_category(self):
        sql ="select * from ProductCategory"
        try :
            self.cursor.execute(sql)
            categories = self.cursor.fetchall()
            return categories
        except Exception as e:
            print("Error:", e)
            return None
        
    def get_product_category(self, idCategory):
        sql = "SELECT * FROM ProductCategory WHERE idCategory = %s"
        params = (idCategory,)
        try:
            self.cursor.execute(sql, params)
            category = self.cursor.fetchone()
            return category
        except Exception as e:
            print("Error:", e)
            return None
        
    def search_product_category(self, str):
        sql = "SELECT * FROM ProductCategory WHERE nameCategory LIKE %s"
        params = (str,)
        try:
            self.cursor.execute(sql, params)
            categories = self.cursor.fetchall()
            return categories
        except Exception as e:
            print("Error:", e)
            return None
        
    def drop_product_category(self, idCategory):
        sql = "DELETE FROM ProductCategory WHERE idCategory = %s"
        params = (idCategory,)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()

            return {"msg": "Succès: catégorie supprimée", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: catégorie non supprimée", "status": 400}
        
    def add_product(self, nameProduct, categories, priceUnitaire):
        sql = "INSERT INTO Products (nameProduct, categories, priceUnitaire) VALUES (%s, %s, %s)"
        params = (nameProduct, categories, priceUnitaire)
        try:
            result = self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: produit ajouté", "status": 200, "id": self.cursor.lastrowid}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: produit non ajouté", "status": 400}

    def get_all_products(self):
        sql ="select * from Products"
        try :
            self.cursor.execute(sql)
            products = self.cursor.fetchall()
            return products
        except Exception as e:
            print("Error:", e)
            return None
        
    def get_product(self, idProduct):
        sql = "SELECT * FROM Products WHERE idProduct = %s"
        params = (idProduct,)
        try:
            self.cursor.execute(sql, params)
            product = self.cursor.fetchone()
            return product
        except Exception as e:
            print("Error:", e)
            return None
        
    def search_product(self, str):
        sql = "SELECT * FROM Products WHERE nameProduct LIKE %s"
        params = (str,)
        try:
            self.cursor.execute(sql, params)
            products = self.cursor.fetchall()
            return products
        except Exception as e:
            print("Error:", e)
            return None
        
    def drop_product(self, idProduct):
        sql = "DELETE FROM Products WHERE idProduct = %s"
        params = (idProduct,)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: produit supprimé", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: produit non supprimé", "status": 400}
        
    def substraction(self, idProduct, quantity):
        sql = "SELECT quantity FROM Products WHERE idProduct = %s"
        params = (idProduct,)
        try:
            self.cursor.execute(sql, params)
            product = self.cursor.fetchone()
            if product[0] < quantity:
                return {"msg": "Échec: stock insuffisant", "status": 400}
            else:
                sql = "UPDATE Products SET quantity = quantity - %s WHERE idProduct = %s"
                params = (quantity, idProduct)
                self.cursor.execute(sql, params)
                self.connection.commit()
                return {"msg": "Succès: stock mis à jour", "status": 200}
        except Exception as e:
            print("Error:", e)
            print("Échec: stock non mis à jour")

    def add_delivery(self, idSupplier, idProduct, dateOfDelivery, priceOfDelivery, quantity):
        sql = "INSERT INTO Delivery (idSupplier, idProduct, dateOfDelivery, priceOfDelivery, quantity) VALUES (%s, %s, %s, %s, %s)"
        params = (idSupplier, idProduct, dateOfDelivery, priceOfDelivery, quantity)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: livraison ajoutée", "status": 200, "id": self.cursor.lastrowid}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: livraison non ajoutée", "status": 400}
        
    def get_all_deliveries(self):
        sql ="select * from Delivery"
        try :
            self.cursor.execute(sql)
            deliveries = self.cursor.fetchall()
            return deliveries
        except Exception as e:
            print("Error:", e)
            return None
        
    def get_delivery(self, idDelivery):
        sql = "SELECT * FROM Delivery WHERE idDelivery = %s"
        params = (idDelivery,)
        try:
            self.cursor.execute(sql, params)
            delivery = self.cursor.fetchone()
            return delivery
        except Exception as e:
            print("Error:", e)
            return None
        
    def drop_delivery(self, idDelivery):
        sql = "DELETE FROM Delivery WHERE idDelivery = %s"
        params = (idDelivery,)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: livraison supprimée", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: livraison non supprimée", "status": 400}
        
    def add_sales(self, idProduct, dateOfSales, priceOfSales, quantity):
        sql = "INSERT INTO Sales (idProduct, dateOfSales, priceOfSales, quantity) VALUES (%s, %s, %s, %s)"
        params = (idProduct, dateOfSales, priceOfSales, quantity)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: vente ajoutée", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: vente non ajoutée", "status": 400}
        
    def get_all_sales(self):
        sql ="select * from Sales"
        try :
            self.cursor.execute(sql)
            sales = self.cursor.fetchall()
            return sales
        except Exception as e:
            print("Error:", e)
            return None
        
    def get_sale(self, idSales):
        sql = "SELECT * FROM Sales WHERE idSales = %s"
        params = (idSales,)
        try:
            self.cursor.execute(sql, params)
            sale = self.cursor.fetchone()
            return sale
        except Exception as e:
            print("Error:", e)
            return None
    
    def drop_sales(self, idSales):
        sql = "DELETE FROM Sales WHERE idSales = %s"
        params = (idSales,)
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return {"msg": "Succès: vente supprimée", "status": 200}
        except Exception as e:
            print("Error:", e)
            return {"msg": "Échec: vente non supprimée", "status": 400}
        
    def close_connection(self):
        self.connection.close()