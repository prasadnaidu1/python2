class Product:
    def __init__(self,id, name,price):
        self.item_id=id
        self.item_name=name
        self.item_price=price
    def show(self):
        print('item id no : ',self.item_id)
        print('item name : ', self.item_name)
        print('item price : ', self.item_price)