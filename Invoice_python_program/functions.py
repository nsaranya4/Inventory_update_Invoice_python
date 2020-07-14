#Author: Saranya Nagarajan
#Assignment Number & Name: Final Project
#Due Date: No Due Date
#Program Description: To create methods to be used in the main program

#this file contains the followig methods
#ProcessInventory() - to copy the inventory available into a list of object instances
#PrintInventory(ObjectList) - to print the inventory list to the user
#CheckItemID(strID) - to veify if the product id entered by the user is valid
#CheckItemQty(ID,strQty) - to verify if the inventory has enough number of the items the user wants to purchase
#UpdateInventory(ItemID,ItemQty) - to update the inventory stock after every purchase/return
#OrderDetails(ItemID,ItemQty) - to create instances for every transaction made by the user
#OrderSummary(TransactionObject) - to calculate the subtotal, sales tax and grand totol for all transactions done



#import the classes and required modules
import inventory
import transactionitem
import os



#method to copy the inventory available into a list of object instances
def ProcessInventory():

    #create an empty list 
    InventoryObjectsList = []
    
    #Open the Inventory.txt file in read mode
    InventoryFile = open('Inventory.txt','r')
      
    #Read the first item from the file
    ItemID = InventoryFile.readline()

    #Read the rest of the file
    while ItemID!= '':

        ItemID = int(ItemID)

        #Read the item name
        ItemName = InventoryFile.readline().rstrip('\n')

        #Read the item's quantity in stock
        ItemStock = int(InventoryFile.readline())

        #read the item's price
        ItemPrice = float(InventoryFile.readline())

        #apppend this inventory instance to the inventory objects list
        InventoryObjectsList.append(inventory.Inventory(ItemID, ItemName, ItemStock, ItemPrice))

        #Read the next item
        ItemID = InventoryFile.readline()

    #Close the file
    InventoryFile.close()

    #return the list of object instances
    return InventoryObjectsList






#method to print the inventory list to the user
def PrintInventory(ObjectList):
   
    #print the inventory items
    for obj in range(0,len(ObjectList)):
        print(ObjectList[obj])

    print("\n")






#method to veify if the product id entered by the user is valid
def CheckItemID(strID):

    #try statement to verify if ID is an integer value
    try:
        ID = int(strID)

    #except statement to catch any value error
    except:
        return -1

    #if user wants to quit, stop checking    
    if ID == 0:
        return 0

    #otherwise, proceed to check the file
    else:
        #set the found flag to false
        found = False
                
        #Open the Inventory.txt file in read mode
        InventoryFile = open('Inventory.txt','r')
                  
        #Read the first item from the file
        ItemID = InventoryFile.readline()

        #Read the rest of the file
        while ItemID!= '':

            ItemID = int(ItemID)

            #if ID is found, then set found flag to true
            if ItemID == ID:
                found = True
                    
            #Read the item name
            ItemName = InventoryFile.readline().rstrip('\n')

            #Read the item's quantity in stock
            ItemStock = int(InventoryFile.readline())

            #read the item's price
            ItemPrice = float(InventoryFile.readline())

            #Read the next item
            ItemID = InventoryFile.readline()

        #Close the file
        InventoryFile.close()

        #return -1, if ID  not found    
        if found == False:
            return -1

        #return ID if valid
        elif found == True:
            return ID






#method to verify if the inventory has enough number of the items the user wants to purchase
def CheckItemQty(ID,strQty):

    #try statement to verify if quantity is an integer value      
    try:
        Qty = int(strQty)

    #except statement to catch any value error        
    except:
        return -1000

    #return a bad value, if user 0 quantity 
    if Qty == 0:
            return -1000

    else:
        #create a variable to determine if this is the first transaction of a session 
        NewFileFound = os.path.exists('UpdatedInventory.txt')

        #if this is not the first transaction, refer UpdatedInventory.txt file for quantity
        if NewFileFound == True:
            #Open the UpdatedInventory.txt file in read mode
            InventoryFile = open('UpdatedInventory.txt','r')

        #if this is the first transaction, refer Inventory.txt file for quantity
        else:
            #Open the Inventory.txt file in read mode
            InventoryFile = open('Inventory.txt','r')

              
        #Read the first item from the file
        ItemID = InventoryFile.readline()

        #Read the rest of the file
        while ItemID!= '':

            ItemID = int(ItemID)

            #Read the item name
            ItemName = InventoryFile.readline().rstrip('\n')

            #Read the item's quantity in stock
            ItemStock = int(InventoryFile.readline())

            #read the item's price
            ItemPrice = float(InventoryFile.readline())

            #when the product ID is found, call the purchase method to validate the quantity against the inventory
            if ItemID == ID:
                Flag = inventory.Inventory(ItemID, ItemName, ItemStock, ItemPrice).purchase(Qty)

                #return a bad value, if not enough stock of the product available
                if Flag == False:
                    return -5000

                #return the quantity if enough stock available in inventory   
                elif Flag == True:
                     return Qty
                    
            #Read the next item
            ItemID = InventoryFile.readline()

        #Close the file
        InventoryFile.close()
            
        
        



#method to update the inventory stock after every purchase/return
def UpdateInventory(ItemID,ItemQty):

    #create an empty list 
    UpdatedInventoryObjectsList = []
    
    #create a variable to determine if this is the first transaction of the session
    NewFileFound = os.path.exists('UpdatedInventory.txt')

    #if this is not the first transaction, refer UpdatedInventory.txt file
    if NewFileFound == True:
        #Open the UpdatedInventory.txt file in read mode
        InventoryFile = open('UpdatedInventory.txt','r')

    #if this is the first transaction, refer Inventory.txt file
    else:
        #Open the Inventory.txt file in read mode
        InventoryFile = open('Inventory.txt','r')
        

    #Open a temp file in write mode
    TempFile= open('temp.txt','w')

    #Read the first item from the file
    ID = InventoryFile.readline()

    #Read the rest of the file
    while ID != '':

        #Strip the \n from the values before searching
        ID = int(ID)
        Name = InventoryFile.readline().rstrip('\n')
        Qty = int(InventoryFile.readline())
        Price = float(InventoryFile.readline())

        
        #when the product ID matches, subtract the purchase quantity from the inventory
        if ID == ItemID:
            New_Qty = Qty - ItemQty
            
            #write the updated values to the new file
            TempFile.write(str(ID) + '\n')
            TempFile.write(Name+ '\n')
            TempFile.write(str(New_Qty) + '\n')
            TempFile.write(str(Price) + '\n')

            #apppend this inventory instance to the inventory objects list
            UpdatedInventoryObjectsList.append(inventory.Inventory(ID, Name, New_Qty, Price))
            
        
        #if the product ID doesn't match, then write the values as such
        else:

            TempFile.write(str(ID) + '\n')
            TempFile.write(Name+ '\n')
            TempFile.write(str(Qty) + '\n')
            TempFile.write(str(Price) + '\n')

            #apppend this inventory instance to the inventory objects list
            UpdatedInventoryObjectsList.append(inventory.Inventory(ID, Name, Qty, Price))

        #Read the next item
        ID = InventoryFile.readline()

    #Close the files
    InventoryFile.close()
    TempFile.close()
    

    #delete the original UpdatedInventory.txt file
    if NewFileFound == True:
        os.remove('UpdatedInventory.txt')

    #rename the temp.txt file as UpdatedInventory.txt
    os.rename('temp.txt','UpdatedInventory.txt')

    #return the updated iventory list
    return UpdatedInventoryObjectsList






#method to create instances for every transaction made by the user
def OrderDetails(ItemID,ItemQty):

    #create an instance of the TransactionItem class
    TransactionItemObject = transactionitem.TransactionItem()

    #set the ID and Quantity attributes
    TransactionItemObject.set_id(ItemID)
    TransactionItemObject.set_qty(ItemQty)

    #Open the updated inventory to look up the product name and price
    DataFile = open('UpdatedInventory.txt','r')

    #Read the first line
    ID = DataFile.readline()

    #Read the rest of the file
    while ID != '':

        #Strip the \n from the values before searching
        ID = int(ID)
        Name = DataFile.readline().rstrip('\n')
        Qty = int(DataFile.readline())
        Price = float(DataFile.readline())

        
        #When the product ID matches, set the Name and Price attributes
        if ID == ItemID:

            TransactionItemObject.set_name(Name)
            TransactionItemObject.set_price(Price)
            
            #Set the found flag to True
            found = True
            break
            
        #Read the next line
        ID = DataFile.readline()

    #Close the files
    DataFile.close()

    #return this object instance
    return TransactionItemObject





#method to calculate the subtotal, sales tax and grand totol for all  the transactions done
def OrderSummary(TransactionObject):

    #create required variables
    SalesTax = 0.085
    TotalItems = 0
    SubTotal = 0.0
    TaxAmount  =0.0
    GrandTotal = 0.0

    #loop through the TransactionItem instances and calculate the subtotal and total # of items
    for obj in range (0, len(TransactionObject)):

       TotalItems +=  TransactionObject[obj].get_qty()
       SubTotal += (TransactionObject[obj].get_qty() * TransactionObject[obj].get_price())

    #calculate tax amount and grand total
    TaxAmount = SubTotal * SalesTax
    GrandTotal = SubTotal + TaxAmount

    #return all calculated values
    return TotalItems, SubTotal, TaxAmount, GrandTotal

    
    
        
        
        
    
    
                
