class View:
    #--Display Books--
    def DisplayBooks(self):
        print("\n\nSelect genre:")
        print("1.    Science Fiction")
        print("2.    Travel")
        print("3.    Software Engineering")
        try: #python 2.x
            uchoice = raw_input("Please input the number of your choice: ")
        except: #python 3.x
            uchoice = input("Please input the number of your choice: ")
            
        print(uchoice)
        print()
        
        if uchoice == "1":
            return "dSciFi"
        elif uchoice == "2":
            return "dTravel"
        elif uchoice == "3":
            return "dSoftware"
        
    #--Add Book to Order--
    def AddToOrder(self):
        try: #python 2.x
            uchoice = raw_input("\n\nPlease input BookID to add: ")
        except: #python 3.x
            uchoice = input("Please input BookID: ")
            
        if (1 <= int(uchoice) <= 60):
            return "a" + str(uchoice)
        else:
            print("Invalid BookID, please try again.")
            return self.AddToOrder()

        #^ this will pass bookid to other thing

    #--Remove Book from Order--
    def RemoveFromOrder(self):
        try: #python v2.x
            uchoice = raw_input("\n\nPlease input BookID to remove: ")
        except: #python v3.x
            uchoice = input("Please input BookID: ")
            
        if (1 <= int(uchoice) <= 60):
            return "r" + str(uchoice)
        else:
            print("Invalid BookID, please try again.")
            return self.RemoveFromOrder()
        
    def GeneralDisplay(self, array):
        for entry in array:
            print(entry)

    #--menu--
    def menu(self):
        print ("\n\n================================================")
        print ("Available actions:")
        print ("1.    Display Books")
        print ("2.    Display Current Order")
        print ("3.    Add Book to Order")
        print ("4.    Remove Book from Order")
        print ("5.    Calculate Order Cost")
        print ("6.    Quit")
        try: #python v2.x
            uchoice = raw_input("Please input the number of your choice: ")
        except: #python v3.x
            uchoice = input("Please input the number of your choice: ")
            
        if uchoice == "1":
            return self.DisplayBooks()
        elif uchoice == "2":
            return "order"
        elif uchoice == "3":
            return self.AddToOrder()
        elif uchoice == "4":
            return self.RemoveFromOrder()
        elif uchoice == "5":
            return "cost"#self.DisplayOrderCost()
        elif uchoice == "6":
            return "quit"
        else:
            print("\n================================\nInvalid input, please try again.\n================================\n")
            return "invalid"
