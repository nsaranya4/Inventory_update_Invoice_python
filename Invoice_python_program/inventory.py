#Author: Saranya Nagarajan
#Assignment Number & Name: Final Project
#Due Date: No Due Date
#Program Description: To create a class to store inventory information

class Inventory():
    #instantiate attribute variables
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price

    #define getters for all attributes
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_stock(self):
        return self.__stock

    def get_price(self):
        return self.__price

    #method to increase stock
    def restock(self, new_stock):
        if new_stock > 0:
            self.__stock += new_stock
            return True
        else:
            return False

    #method to decrease stock
    def purchase(self, purch_qty):
        if purch_qty <= self.__stock:
            self.__stock -= purch_qty
            return True
        else:
            return False

    #override str method to print all attributes
    def __str__(self):
        strInventory = format(self.__id,'.0f') + "\t" + f"{self.__name:<25}" + "\t"
        strInventory += "$" + format(self.__price,'8.2f') + "\t \t" + format(self.__stock,'4,.0f')
        return strInventory
        
        
    
    
        
        
