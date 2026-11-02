import csv

FILENAME = "monthly_sales.csv"


#Read items stored in monthly sales file and store them into a 2d list
def read_sales():
        sales = []
        with open("monthly_sales.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                 sales.append(row)
            
        return sales
                 
#Reads through the first row which stores all the sales and calculates the average           
def display_avg_sales(sales):
    total_sales = 0
    count = 0
    for row in sales:
        total_sales+= int(row[1])
        count+=1
    avg_sales = round(total_sales / count, 2)
    print("average sale: ", avg_sales)
                 


# main and calls both functions created above.
def main():

    sales=read_sales()

# Main program asking the user 

    more = "y"
    while more.lower() == "y":
         command = (input("What would you like to do? (R)ead or (D)isplay Average?:  ")).lower()
         if command == "r":
            sales=read_sales()
            print(sales)
            
            
         elif command == "d":
                sales=read_sales()
                display_avg_sales(sales)
                
        
         else:
            print("error, invalid input")
            
            
         more = input("Would you like to try again? (y or n): ")
         
         if more =="y":
            continue
         
         elif more=="n":
            print("Goodbye")

         else:
            print("Error, invalid input")
            return
        






    
    






if __name__ == "__main__":
        main()