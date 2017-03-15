import random


class Road:
    """The summary line for a class docstring should fit on one line.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    
    def __init__(self, **kwargs):
        defaults = {
            'name': 'Road ' + str(random.randint(1, 99999)),
            'length': '15',
            'speed_limit': '55'
        }
        
        for key, default in defaults.items():
            setattr(self, key, kwargs.get(key, default))

    def tell_road_name(self):
        return 'The name of this road is {}'.format(self.name)

    def tell_road_length(self):
        return 'The length of {} is {} miles'.format(self.name,
                                                     self.length)

    def tell_speed_limit(self):
        return 'The speed limit of {} is {} MPH'.format(self.name,
                                                        self.speed_limit)

    @staticmethod    
    def generate_random_road_data():
        data = {
            'name': 'Route ' + str(random.randint(10, 999)), 
            'length': random.randint(10, 100), 
            'speed_limit': random.randint(25, 85)
        }
        
        return data


if __name__ == "__main__":
    data = Road.generate_random_road_data()
    x = Road(**data)
    print(x.tell_road_name())
    print(x.tell_road_length())
    print(x.tell_speed_limit())
    y = Road()
    print(y.tell_road_name())
    print(y.tell_road_length())
    print(y.tell_speed_limit())
