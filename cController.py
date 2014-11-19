def cController:
    
    def DisplayBook(genre):
        return model.GetGookList(genre)
        
    def AddToOrder(BookID):
        model.AddToOrder(BookID)
        return "Added book #" + str(BookID) + " to the order."
    
    def RemoveFromOrder(BookID):
        model.RemoveFromOrder(BookID)
        return "Removed book #" + str(BookID) + " from the order."
        
    def GetOrderCost()
        return model.CalculateOrderCost()