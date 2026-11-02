class Rectangle:
    
    
    #Constructor with 2 attributes width and length
    def __init__(self,length=0,width=0):
        self.length = length
        self.width = width
        
    #function to calculate perimeter
    def calcPerimeter(self):
        return  2 * (int(self.length) + int(self.width))
    
    #function to calculate area
    def calcArea(self):
        return int(self.length) * int(self.width)





    #Method that prints the rectangle
    def getStr(self):
        rectStr = ''
        for i in range(int(self.length)):
            rectStr += '*   '  * int(self.width) + '\n'
        return rectStr
        