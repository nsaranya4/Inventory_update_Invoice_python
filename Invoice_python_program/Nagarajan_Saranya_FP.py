#Author: Saranya Nagarajan
#Assignment Number & Name: Final Project
#Due Date: No Due Date
#Program Description: To create a program that processes transactions and displays invoice


#import the classes and required modules
import inventory
import transactionitem
import functions
import os


def main():
    
    #Create a variable to hold the inventory instances
    Menu = functions.ProcessInventory()

    #print the inventory menu 
    print("\nID \t Item \t \t \t \t Price \t \t \t Qty Available")
    functions.PrintInventory(Menu)


    #create an empty list to hold the TransactionItem instances
    TransactionList = []
    

    #set the ItemID and ItemQty to a arbitrary bad value    
    ItemID = -1
    ItemQty = -1000

    #create a variable to determine if the inventory needs to be updated
    Flag = True

    #loop until user quits 
    while ItemID != 0:

        #loop until product ID is valid
        while ItemID == -1:
            #get the product ID
            strItemID = input("Which Product ID would you like to purchase? Enter 0 to exit. ")

            #check if the product ID is valid    
            ItemID = functions.CheckItemID(strItemID)

            #if not valid, print an error message
            if ItemID == -1:
                print("Invalid Product ID. Please try again.")
                #set quantity = 0, to stop prompting for quantity
                ItemQty = 0
                #set flag = false to not update the file
                Flag = False

            #if user wants to quit after doing some transaction, stop looping
            elif (ItemID == 0 and len(TransactionList) != 0):
                ItemQty = 0
                Flag = False
                break

            #if user wants to quit without doing any transaction, print a nice message and stop looping
            elif (ItemID == 0 and len(TransactionList) == 0):
                    print ("Thank you for visiting!")
                    ItemID = 0
                    ItemQty = 0
                    #copy the inventory data to UpdatedInventory.txt as per specification
                    functions.UpdateInventory(ItemID,ItemQty)
                    Flag = False
                    break

            #if user has entered a valid product ID and doesnt't want to quit, prompt for quantity
            else:
                #update the ItemQty to a bad arbitrary value 
                ItemQty = -1000
                Flag = True
                       
            #loop until quantity entered is valid
            while ItemQty == -1000:

                #get the product quantity
                strItemQty = input("How many items would you like to purchase? Enter a negative number for a return. ")

                #check if the quantity is valid
                ItemQty = functions.CheckItemQty(ItemID,strItemQty)

                #if quantity not valid, print an error message
                if ItemQty == -1000:
                    print("That is not a valid quantity. Try again.")
                    
                #if not enough stock in the inventory, print a message and break to go back to the ID loop
                elif ItemQty == -5000:
                    print("There is not enough inventory to purchase this many of the items. Try again.")
                    ItemID = -1
                    Flag = False
                    break


            #if both product ID and product quantity are valid, update the inventory file
            if(Flag == True):
                #update inventory 
                UpdatedMenu = functions.UpdateInventory(ItemID,ItemQty)

                #print the updated inventory
                print("\n ID \t Item \t \t \t \t Price \t \t Qty Available")
                functions.PrintInventory(UpdatedMenu)

                #create an instance of the transaction
                TransactionObject = functions.OrderDetails(ItemID,ItemQty)

                #append this transaction instance to a list of TransactionItem instances
                TransactionList.append(TransactionObject)

                #reset the ID and quantity values back to a bad value to contine looping
                ItemID = -1
                ItemQty = -1000



    #When the user quits after doing some transaction, generate invoice
    if (ItemID == 0 and len(TransactionList) != 0):

        #print thetransaction details
        print("\nOrder Complete. See Invoice Below:\n")
        print("ID \t Name \t \t \t Quantity \t  Price \t Extended Price")
        functions.PrintInventory(TransactionList)

        #create a list to store the calculated totals 
        TransactionSummary = []
        TransactionSummary = functions.OrderSummary(TransactionList)

        #print invoice
        print("Total Items:", TransactionSummary[0])
        print("Sub Total: $", format(TransactionSummary[1],'.2f'),sep = '')
        print("Sales Tax: $", format(TransactionSummary[2],'.2f'),sep = '')
        print("Grand Total: $", format(TransactionSummary[3],'.2f'),sep = '')
        
    
    
#call main
main()
