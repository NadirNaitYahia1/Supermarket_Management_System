import tkinter as tk
from tkinter import ttk
import mysql.connector

class Models:
    def __init__(self, db_name='db'):
        self.db_name = db_name
        self.connection =  mysql.connector.connect(host='localhost',user='root',password='')                                              
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE DATABASE IF NOT EXISTS {}
        '''.format(self.db_name))
        self.create_tables()

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
                date DATE,
                FOREIGN KEY (idVendor) REFERENCES Vendor(idVendor),
                FOREIGN KEY (idProduct) REFERENCES Products(idProduct)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sales (
                idSales INT AUTO_INCREMENT PRIMARY KEY,
                idProduct INT,
                dateOfSales DATE,
                priceOfSales INT,
                FOREIGN KEY (idProduct) REFERENCES Products(idProduct)
            )
        ''')

        self.connection.commit()

    def add_vendor(self,nameVendor,firstNameVendor): 
        sql = "INSERT INTO Vendor values(%s,%s,%s)"
        params = (nameVendor,firstNameVendor)
        try: 
            self.cursor.execute(sql,params)
            return {"msg":"succes :vendor added","status":200}
        except: 
            return {"msg":"failure: vendor not added","status":400}

            

    def add_product(self,nameProduct,categories,priceUnitaire): 
            #         CREATE TABLE IF NOT EXISTS Products (
            #     idProduct INT AUTO_INCREMENT PRIMARY KEY,
            #     nameProduct VARCHAR(20),
            #     categories VARCHAR(20),
            #     priceUnitaire INT,
            #     idVendor INT,
            #     FOREIGN KEY (idVendor) REFERENCES Vendor(idVendor)
            # )

        sql = "INSERT INTO Products Values(%s,%s,%s,%s,%s)"
        param =(nameProduct,categories,priceUnitaire)
        return
        

    def close_connection(self):
        self.connection.close()

def main(): 
    model =Models('db')


if __name__ == "__main__":
    main()
