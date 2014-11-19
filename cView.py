#--Display Books--
def dbooks():
    print("Select genre:")
    print("1.    Science Fiction")
    print("2.    Travel")
    print("3.    Software Engineering")
    uchoice = input("Please input the number of your choice: ")
    #print(DisplayBooks(uchoice))
    #^ should print the booklist to the screen (somehow)
    
    print(uchoice)
    main()
    
#--Add Book to Order--
def abook():
    uchoice = input("Please input BookID: ")
    if (1 <= int(uchoice) <= 60):
        #AddToOrder(int(uchoice))
        print("Added " + uchoice + " to order.")
        main()
    else:
        print("Invalid BookID.")
        abook()

    #^ this will pass bookid to other thing

#--Remove Book from Order--
def rbook():
    uchoice = input("Please input BookID: ")
    if (1 <= int(uchoice) <= 60):
        #RemoveFromOrder(int(uchoice))
        print ("Removed " + uchoice + " from order.")
        main()
    else:
        print("Invalid BookID.")
        rbook()
        
#--Calculate Cost of Order--
def ccost():
    #GetOrderCost()
    print("calc cost")
    main()

#Main thing
def main():
    print ("1.    Display Books")
    print ("2.    Add Book to Order")
    print ("3.    Remove Book from Order")
    print ("4.    Calculate Order Cost")
    print ("5.    Quit")
    uchoice = input("Please input the number of your choice: ")
    if uchoice == '1':
        dbooks()
    elif uchoice == '2':
        abook()
    elif uchoice == '3':
        rbook()
    elif uchoice == '4':
        ccost()
    elif uchoice == '5':
        quit
    else:
        print("Invalid input.")
        main()
        
main()