from db.sql import Models
from db.mongo import NosqlModel

def archieve_deliveries():
    db_models = Models()
    nosqlbd = NosqlModel()
    deliveries = db_models.get_all_deliveries()
    for delivery in deliveries:
        nosqlbd.archieve_delivery(delivery[0], delivery[1], delivery[2], delivery[3])
        db_models.drop_delivery(delivery[0])
    print("Deliveries archieved")

def archieve_sales():
    db_models = Models()
    nosqlbd = NosqlModel()
    sales = db_models.get_all_sales()
    for sale in sales:
        nosqlbd.archieve_sale(sale[0], sale[1], sale[2])
        db_models.drop_sales(sale[0])
    print("Sales archieved")