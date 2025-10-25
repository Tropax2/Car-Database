"""A small car database that acquires info by prompting the user."""

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

# Gets the brands and adds them to a list.
def brands_and_amount():
    brands = [brand.get('brand', None) for brand in my_cars]
    return brands

# gets the brands and the number of vehicles of each brand.
def get_brand_counts():
    counts = Counter(brands_and_amount())
    brands = list(counts.keys())
    amounts = list(counts.values())
    return brands, amounts

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
    
    see_car_brands_and_amounts = prompt_the_user("Do you want to see which brands do you have and how many cars of each brand you own?")

    if see_car_brands_and_amounts == 'yes':
        print(dict(Counter(brands_and_amount())))

    elif see_car_brands_and_amounts == 'no':
        pass

    final_results = prompt_the_user("Do you want to visualise all the data?")

    if final_results == 'yes':
        print(my_cars)   
    
if __name__ == "__main__":
    main()



