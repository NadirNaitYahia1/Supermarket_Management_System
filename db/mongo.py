import pymongo

class NosqlModel:
    def __init__(self):
        try:
            self.client =pymongo.MongoClient("mongodb://localhost:27017")
            self.db = self.client["SuperMarket"]

            collections = ["SalesArcheive", "DeliveryArcheive", "Invoice", "ProductImages", "Reviews"]
            for collection_name in collections:
                if collection_name not in self.db.list_collection_names():
                    self.db.create_collection(collection_name)
                    print(f"Collection '{collection_name}' created successfully.")
                else:
                    print(f"Collection '{collection_name}' already exists.")
        except:
            print('error no sql not created')

# ________________________________________________________________________________________________________________

    def add_invoice(self, idDelivery, file_name, file_path, file_data):
        document = {"idDelivery": idDelivery, "file_name": file_name, "file_path": file_path, "file_data": file_data}
        try:
            self.db["Invoice"].insert_one(document)
            print("Invoice added")
        except:
            print('Invoice not added error')
    
    def get_invoice(self, idDelivery):
        invoice = self.db["Invoice"].find_one({"idDelivery": idDelivery})
        return invoice
    
    def drop_invoice(self, idDelivery):
        try:
            self.db["Invoice"].delete_one({"idDelivery": idDelivery})
            print("Invoice dropped")
        except:
            print('Invoice not dropped error')

# ________________________________________________________________________________________________________________
    
    def add_product_image(self, idProduct, file_name, file_path, file_data):
        document = {"idProduct": idProduct, "file_name": file_name, "file_path": file_path, "file_data": file_data}
        try:
            result = self.db["ProductImages"].insert_one(document)
            print("Product image added")
            return result.inserted_id
        except:
            print('Product image not added error')

    def get_image(self, idProduct):
        image = self.db["ProductImages"].find_one({"idProduct": idProduct})
        return image
    
    def drop_image(self, idProduct):
        try:
            self.db["ProductImages"].delete_one({"idProduct": idProduct})
            print("Image dropped")
        except:
            print('Image not dropped error')

# ________________________________________________________________________________________________________________

    def archieve_delivery(self, sqlID=1, dateOfDelivery="", quantity="", idProduct=""):
        document = {"sqlID": sqlID, "dateOfDelivery": dateOfDelivery, "quantity": quantity, "idProduct": idProduct}
        try:
            self.db["DeliveryArcheive"].insert_one(document)
            print("Delivery archieved")
        except:
            print('Delivery not archieved error')

    def get_all_deliveries(self):
        deliveries = self.db["DeliveryArcheive"].find()
        return deliveries

# ________________________________________________________________________________________________________________
    
    def archieve_sale(self, sqlID=1, dateOfSale="", priceOfSales="", quantity=""):
        document = {"sqlID": sqlID, "dateOfSale": dateOfSale, "priceOfSales": priceOfSales, "quantity": quantity}
        try:
            self.db["SalesArcheive"].insert_one(document)
            print("Sale archieved")
        except:
            print('Sale not archieved error')

    def get_all_sales(self):
        sales = self.db["SalesArcheive"].find()
        return sales
    
    def get_sales_by_date(self, dateOfSale):
        sales = self.db["SalesArcheive"].find({"dateOfSale": dateOfSale})
        return sales


# ________________________________________________________________________________________________________________

def add_review(self, idProduct, review):
    document = {"idProduct": idProduct, "review": review}
    try:
        self.db["Reviews"].insert_one(document)
        print("Review added")
    except:
        print('Review not added error')

    
def get_reviews(self, idProduct):
    reviews = self.db["Reviews"].find({"idProduct": idProduct})
    return reviews

def drop_reviews(self, idProduct):
    try:
        self.db["Reviews"].delete_one({"idProduct": idProduct})
        print("Reviews dropped")

    except:
        print('Reviews not dropped error')