class Calculator(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def sum(self):      
        return self.first + self.second
        
    def divide(self):      
        return float(self.first / self.second)
    
    def multip(self):      
        return self.first * self.second
    
    def subtraction(self):      
        return float(self.first - self.second)
 
