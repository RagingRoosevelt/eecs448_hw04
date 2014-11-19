class View:
    def __init__(self):
        from cController import Controller
		  
		  controller = Controller()
        

    #--Display Books--
    def DisplayBooks(self):
        print("Select genre:")
        print("1.    Science Fiction")
        print("2.    Travel")
        print("3.    Software Engineering")
        uchoice = input("Please input the number of your choice: ")
        print(uchoice)
        print()
        
        if uchoice == "1":
            return "dSciFi"
        elif uchoice == "2":
            return "dTravel"
        elif uchoice == "3":
            return "dSoftware"
        controller.DisplayBooks(uchoice)
    #--Add Book to Order--
    def AddToOrder(self):
        uchoice = input("Please input BookID: ")
        if (1 <= int(uchoice) <= 60):
            controller.AddToOrder(int(uchoice))
            print("Added BookID " + uchoice + " to order.")
            print()
            return "a" + str(uchoice)
        else:
            print("Invalid BookID.")
            return AddToOrder()

        #^ this will pass bookid to other thing

    #--Remove Book from Order--
    def RemoveFromOrder(self):
        uchoice = input("Please input BookID: ")
        if (1 <= int(uchoice) <= 60):
            controller.RemoveFromOrder(int(uchoice))
            print ("Removed BookID " + uchoice + " from order.")
            print()
            return "r" + str(uchoice)
        else:
            print("Invalid BookID.")
            return self.RemoveFromOrder()
            
    #--Calculate Cost of Order--
    def DisplayOrderCost(self):
        controller.GetOrderCost()
        print("calc cost")
        
    def GeneralDisplay(self, list):
        for entry in list:
            print(entry)

    #Main thing
    def main(self):
        print()
        print ("Avalible actions:")
        print ("1.    Display Books")
        print ("2.    Display Current Order")
        print ("3.    Add Book to Order")
        print ("4.    Remove Book from Order")
        print ("5.    Calculate Order Cost")
        print ("6.    Quit")
        uchoice = input("Please input the number of your choice: ")
        print("")
        if uchoice == '1':
            return self.DisplayBooks()
        elif uchoice == '2':
            return "order"
        elif uchoice == '3':
            return self.AddToOrder()
        elif uchoice == '4':
            return self.RemoveFromOrder()
        elif uchoice == '5':
            return "cost"#self.DisplayOrderCost()
        elif uchoice == '6':
            return "quit"
        else:
            print("Invalid input.")
            self.main()