"""Attempts to create a simple model for a car"""

class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model 
        self.year = year 

#Creates a dictionary where the info is going to be stored.
    def structure(self):
        car ={
            'brand': self.brand,
            'model': self.model,
            'year': self.year
            }
        
        return car 
    

