class Cart:
  def __init__(self):
    self.items={}
    self.price_details={"book":10,"laptop":30000}
  def add_item(self,item_name,quantity):
    self.items[item_name]=quantity
  def remove_item(self,item_name):
    del self.items[item_name]
  def update_quantity(self,item_name,quantity):
    self.items[item_name]=qantity
  def get_cartitems(self):
    cart_items=list(self.items.keys())
    return cart_items
  def get_total_price(self):
    total_price=0
    for item,quantity in self.items.items():
      total_price+=quantity*self.price_details[item]
    return total_price
cart_obj=Cart()
cart_obj.add_item(book,10)
cart_obj.add_item(laptop,1)
print(cart_obj.get_total_price())
cart_obj.update_quantity(book,5)
print(cart_obj.get_cartitems())
cart_obj.remove_item(laptop)
print(cart_obj.get_cartitems())
  
    
