"""Prompts the user to insert its car info"""

from Car_structure import Car 
from collections import Counter

my_cars = []

# Adds the data of the cars to a dictionary.
def write_on_data_base(brand, model, year):
    my_car = Car(brand.title(), model.title(), year)
    my_cars.append(my_car.structure())

# Prompts the user.
def prompt_the_user(prompt):
    while True:
        answer = input(f"{prompt} (yes/no)\n")

        if answer == 'yes' or answer == 'no':
            return answer 
               
        else:
            print("Your answer must be 'yes' or 'no'.")
            continue

# Gets the brands and adds them to a list, removing repetitions and counting the number of occurences of each brand.
def brands_and_numbers():
    brands = [brand.get('brand', None) for brand in my_cars]
    print(dict(Counter(brands))) 

# This is the main function.
def main():
    print("Hello, this program will store the information about your cars.")

    while True:
        brand = input("What is the car brand?\n")
        model = input("What is the model of the car?\n")
        year = int(input("From which year is the car?\n"))

        write_on_data_base(brand, model, year)
        
        add_more_cars = prompt_the_user("Do you want to add more cars to the list?")

        if add_more_cars == 'yes':
            continue 

        elif add_more_cars == 'no':
            break
    
    see_car_brand_and_number = prompt_the_user("Do you want to see which brands do you have and how many cars of each brand you own?")

    if see_car_brand_and_number == 'yes':
        brands_and_numbers()

    elif see_car_brand_and_number == 'no':
        pass

    final_results = prompt_the_user("Do you want to visualise all the data?")

    if final_results == 'yes':
        print(my_cars)
    
if __name__ == "__main__":
    main()




