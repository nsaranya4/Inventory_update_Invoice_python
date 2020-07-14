#Author: Saranya Nagarajan
#Assignment Number & Name: Final Project
#Due Date: No Due Date
#Program Description: To create a class to store the transaction details

class TransactionItem():

    #instantiate attribute variables
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__quantity = 0
        self.__price = 0.0

    #defince getters and setters for all attributes
    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_qty(self):
        return self.__quantity

    def set_qty(self,  new_qty):
        self.__quantity = new_qty

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    #method to calculate the cost of an item
    def calc_cost(self):
        cost = self.__price * self.__quantity
        return cost
    
    #override str method to print output
    def __str__(self):
        transDetails = format(self.__id,'.0f') + "\t" + f"{self.__name:<25}" 
        transDetails += format(self.get_qty(),'4,.0f') + "\t \t $" + format(self.get_price(),'8.2f')
        transDetails += "\t $" + format(self.calc_cost(),'8.2f')
        return transDetails

















