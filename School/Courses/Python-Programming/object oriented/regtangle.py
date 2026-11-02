from object import Rectangle


# Asks User for Width and Height and calculates the Perimeter and Area
def calcFunctions():
        
    width = input("Enter Width:  ")
    length = input("Enter length:  ")
 
    
    rect = Rectangle(length,width)
    perimeter = rect.calcPerimeter()
    area = rect.calcArea()
    
    
    print("Perimeter:  ", perimeter)
    print("Area:  ", area)
    print(rect.getStr())
  

  
# Main Program
def main():

    print("Rectangle Area and Perimeter Calculator")
    print()
    
    
    calcFunctions()

    
    while True:
        command = input("Continue? (y/n):  ").lower()
        if command == "y":
            calcFunctions()

        elif command == "n":
            print("Goodbye! ")
            break
        
        else:
            print("Invalid choice please try again")
            
    
    
if __name__ == "__main__":
    main()