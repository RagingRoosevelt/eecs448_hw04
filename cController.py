class Controller:
    def __init__(self):
        from cView import View
        from cModel import Model
        
        model = Model()
        view = View()
        
        while True:
            action = view.main()
            
            if action == "quit":
                quit()
            elif action[0] == "r":
                self.RemoveFromOrder(model, int(action[1:]))
            elif action[0] == "a":
                self.AddToOrder(model, int(action[1:]))
            elif action[0] == "d":
                self.DisplayBook(model, view, action[1:])
            elif action == "order":
                self.GetOrderList(model, view)
            elif action == "cost":
                self.GetOrderCost(model,view)
                
    
    def DisplayBook(self, model, view, genre):
        BookList = model.GetBookList(genre)
        view.GeneralDisplay(BookList)
        
    def AddToOrder(self, model, BookID):
        model.AddToOrder(BookID)
        return "Added book #" + str(BookID) + " to the order."
    
    def RemoveFromOrder(self, model, BookID):
        model.RemoveFromOrder(BookID)
        return "Removed book #" + str(BookID) + " from the order."
        
    def GetOrderCost(self, model, view):
        cost = model.CalculateOrderCost()
        view.GeneralDisplay(cost)
        
    def GetOrderList(self, model, view):
        OrderList = model.GetOrder()
        view.GeneralDisplay(OrderList)