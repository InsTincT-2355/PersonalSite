#!/usr/bin/env python3
import csv


def write_trips(trips):
    with open('miles.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)



def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    trips=[]
    trip=[]

    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
        trip.append(miles_driven)
        trip.append(gallons_used)
        trips.append(trip)
        
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ")
        
        
        
    write_trips(trips)
    print("Bye")

if __name__ == "__main__":
    main()

