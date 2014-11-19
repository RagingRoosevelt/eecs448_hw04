def cController:
    def __init__(self):
        model = cModel()
        view = cView()
    
    def DisplayBook(genre):
        return model.GetBookList(genre)
        
    def AddToOrder(BookID):
        model.AddToOrder(BookID)
        return "Added book #" + str(BookID) + " to the order."
    
    def RemoveFromOrder(BookID):
        model.RemoveFromOrder(BookID)
        return "Removed book #" + str(BookID) + " from the order."
        
    def GetOrderCost()
        return model.CalculateOrderCost()