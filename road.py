import random


class Road:
    """ Class to create a "road" that will have "signals" and "vehicles"

    Attributes:
        name (str): Name of the road.
        length (int): Length of the road in miles
        speed_limit (int): Speed limit of road in MPH.
    """

    def __init__(self, **kwargs):
        defaults = {
            'name': 'Road ' + str(random.randint(1, 99999)),
            'length': '15',
            'speed_limit': '55'
        }

        for key, default in defaults.items():
            setattr(self, key, kwargs.get(key, default))

    def state_road_name(self):
        """
        Returns a formatted string stating the name of the road
        """
        return 'The name of this road is {}'.format(self.name)

    def state_road_length(self):
        """
        Returns a formatted string stating the length of the road in miles.
        """
        return 'The length of {} is {} miles'.format(self.name,
                                                     self.length)

    def state_speed_limit(self):
        """
        Returns a formatted string stating the speed limit in MPH.
        """
        return 'The speed limit of {} is {} MPH'.format(self.name,
                                                        self.speed_limit)

    @staticmethod
    def generate_random_road_data():
        """
        Generate random signal data to pass to a new road object

        Returns:
            A dict of data to pass to a new road object
        """
        data = {
            'name': 'Route ' + str(random.randint(10, 999)),
            'length': random.randint(10, 100),
            'speed_limit': random.randint(25, 85)
        }

        return data

if __name__ == "__main__":
    data = Road.generate_random_road_data()
    x = Road(**data)
    print(x.state_road_name())
    print(x.state_road_length())
    print(x.state_speed_limit())
    y = Road()
    print(y.state_road_name())
    print(y.state_road_length())
    print(y.state_speed_limit())
