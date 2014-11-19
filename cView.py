class cView:
    def __init__(self):
        controller = cController()
        

    #--Display Books--
    def DisplayBooks(self):
        print("Select genre:")
        print("1.    Science Fiction")
        print("2.    Travel")
        print("3.    Software Engineering")
        uchoice = input("Please input the number of your choice: ")
        controller.DisplayBook(uchoice)
        self.main()
        
    #--Add Book to Order--
    def AddToOrder(self):
        uchoice = input("Please input BookID: ")
        if (1 <= int(uchoice) <= 60):
            controller.AddToOrder(int(uchoice))
            print("Added " + uchoice + " to order.")
            self.main()
        else:
            print("Invalid BookID.")
            AddToOrder()

        #^ this will pass bookid to other thing

    #--Remove Book from Order--
    def RemoveFromOrder(self):
        uchoice = input("Please input BookID: ")
        if (1 <= int(uchoice) <= 60):
            controller.RemoveFromOrder(int(uchoice))
            print ("Removed " + uchoice + " from order.")
            self.main()
        else:
            print("Invalid BookID.")
            RemoveFromOrder()
            
    #--Calculate Cost of Order--
    def DisplayOrderCost(self):
        controller.GetOrderCost()
        self.main()

    #Main thing
    def main(self):
        print ("1.    Display Books")
        print ("2.    Add Book to Order")
        print ("3.    Remove Book from Order")
        print ("4.    Calculate Order Cost")
        print ("5.    Quit")
        uchoice = input("Please input the number of your choice: ")
        print("")
        if uchoice == '1':
            self.DisplayBooks()
        elif uchoice == '2':
            self.AddToOrder()
        elif uchoice == '3':
            self.RemoveFromOrder()
        elif uchoice == '4':
            self.DisplayOrderCost()
        elif uchoice == '5':
            quit
        else:
            print("Invalid input.")
            self.main()
        
        
view = cView()
view.main()