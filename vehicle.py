import random


class Vehicle:
    """ Class to create a "vehicle" that travels on a "road"

    Attributes:
        name (str): Name of the vehicle - "nickname" if you will.
        make (str): Make of the vehicle.
        model (str): Model of the vehicle.
        year (int): Model year of the vehicle.
        max_speed (int): Max speed of the vehicle.
        fuel_efficiency (int): Fuel efficiency (in mpkWh) of the vehicle
        fuel (int): Battery charge (in kWh) left in the vehicle.
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

    def state_make(self):
        """
        Returns a formatted string stating the make of the vehicle
        """
        return 'The make of this vehicle is {}.'.format(self.make)

    def state_model(self):
        """
        Returns a formatted string stating the model of the vehicle
        """
        return 'The model of this vehicle is {}.'.format(self.model)

    def state_fuel_efficiency(self):
        """
        Returns a formatted string stating the fuel efficiency of the vehicle
        """
        line = """
The fuel effiency of this vehicle is {} mpkWH (miles per kiloWatt Hour).
"""
        return line.replace('\n', '').format(self.fuel_efficiency)

    def state_fuel(self):
        """
        Returns a formatted string stating the fuel of the vehicle
        """
        line = """
There are {} kW (kiloWatt hours) left in the battery for this vehicle.
"""
        return line.replace('\n', '').format(self.fuel)

    @staticmethod
    def get_random_model(make):
        """
        Generate a random model from a passed make, Nissan Roadster is wrong

        Args:
            max: The make of the vehicle

        Returns:
            A string representation of random model
        """
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
        """
        Generate random vehicle data to pass to a new vehicle object

        Returns:
            A dict of data to pass to a new vehicle object
        """
        data = {
            'name': 'Car ' + str(random.randint(1, 99999)),
            'make': random.choice(['Nissan', 'Tesla', 'Hyundai', 'BMW',
                                   'Chevrolet', 'Toyota']),
            'year': random.randint(2000, 2016),
            'max_speed': random.randint(55, 75),
            'fuel_efficiency': round(random.uniform(2.5, 6.3), 2),
            'fuel': random.randint(18, 80)
        }
        # Generate model down here
        data['model'] = Vehicle.get_random_model(data['make'])

        return data


if __name__ == "__main__":
    data = Vehicle.generate_random_vehicle_data()
    x = Vehicle(**data)
    print(x.state_make())
    print(x.state_model())
    print(x.state_fuel_efficiency())
    print(x.state_fuel())
    y = Vehicle()
    print(y.state_make())
    print(y.state_model())
    print(y.state_fuel_efficiency())
    print(y.state_fuel())
