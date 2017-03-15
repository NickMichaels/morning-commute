import random


class Vehicle:
    """The summary line for a class docstring should fit on one line.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    
    def __init__(self, **kwargs):
        defaults = {
            'name': 'Car ' + str(random.randint(1, 99999)),
            'make': 'Nissan',
            'model': 'Leaf',
            'year': '2015',
            'max_speed': '57',
            'fuel_efficiency': '4',
            'fuel': '24'
        }
        
        for key, default in defaults.items():
            setattr(self, key, kwargs.get(key, default))

    def tell_make(self):
        return 'The make of this vehicle is {}.'.format(self.make)
        
    def tell_model(self):
        return 'The model of this vehicle is {}.'.format(self.model)
    
    def tell_fuel_efficiency(self):
        return 'The fuel effiency of this vehicle is {} mpkWH (miles per kiloWatt Hour).'.format(self.fuel_efficiency)

    def tell_fuel(self):
        return 'There are {} kW (kiloWatt hours) left in the battery for this vehicle.'.format(self.fuel)
    
    @staticmethod    
    def get_random_model(make):
        models = {
            'Tesla': ('Model S', 'Roadster', 'Model X', 'Model 3'),
            'Nissan': ('Leaf'),
            'Hyundai': ('Ioniq'),
            'Chevrolet': ('Spark EV', 'Bolt', 'Volt'),
            'Toyota': ('RAV 4 EV', 'Prius Prime'),
            'BMW': ('i3', 'i8')
        }
        
        return random.choice(models[make])

    @staticmethod    
    def generate_random_vehicle_data():
        data = {
            'name': 'Car ' + str(random.randint(1, 99999)), 
            'make': random.choice(['Nissan', 'Tesla', 'Hyundai' , 'BMW', 'Chevrolet', 'Toyota']),
            'year': random.randint(2000, 2016),
            'max_speed': random.randint(55, 75),
            'fuel_efficiency': round(random.uniform(2.5, 6.3),2),
            'fuel': random.randint(18, 80)
        }
        # Generate model down here
        data['model'] = Vehicle.get_random_model(data['make'])
        
        return data


if __name__ == "__main__":
    data = Vehicle.generate_random_vehicle_data();
    x = Vehicle(**data)
    print(x.tell_make())
    print(x.tell_model())
    print(x.tell_fuel_efficiency())
    print(x.tell_fuel())
    y = Vehicle()
    print(y.tell_make())
    print(y.tell_model())
    print(y.tell_fuel_efficiency())
    print(y.tell_fuel())
    