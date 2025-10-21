"""Prompts the user to insert its car info"""

from Car_structure import Car 
from collections import Counter

my_cars = []

print("Hello, this program will store the information about your cars.")

# This is the main function.
def main():
    while True:
        brand = input("What is the car brand?\n")
        model = input("What is the model of the car?\n")
        year = input("From which year is the car?\n")

        write_on_data_base(brand, model, year)
        
        answer = add_more_cars()

        if answer == 'yes':
            continue 

        elif answer == 'no':
            break
    
    see_car_brand_and_number = see_brands_and_numbers()

    if see_car_brand_and_number == 'yes':
        brands_and_numbers()

    elif see_car_brand_and_number == 'no':
        pass

# Adds the data of the cars to a dictionary.
def write_on_data_base(brand, model, year):
    my_car = Car(brand.title(), model.title(), year)
    my_cars.append(my_car.structure())

# Checks if the user wants to add more cars.     
def add_more_cars():
    while True:
        add_more_cars = input("Do you want to add more cars? (yes/no)\n")

        if add_more_cars == 'yes':
            return add_more_cars 

        elif add_more_cars == 'no':
            return add_more_cars

        else:
            print("Your answer must be 'yes' or 'no'.")
            continue

# Checks if the user wants to see the different brands and the number of cars of each brand he owns.
def see_brands_and_numbers():
    while True:
        brand_and_number = input("Do you want to see which brands do you have and how many cars of each brand you own? (yes/no)\n") 

        if brand_and_number == 'yes':
            return brand_and_number 

        elif brand_and_number == 'no':
            return brand_and_number 
        
        else:
            print("Your answer must be 'yes' or 'no'.")
            continue

# Gets the brands and adds them to a list, removing repetitions and counting the number of occurences of each brand.
def brands_and_numbers():
    brands = [brand.get('brand', None) for brand in my_cars]
    print(dict(Counter(brands))) 
    

main()




