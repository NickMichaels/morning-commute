import random


class Signal:
    """The summary line for a class docstring should fit on one line.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, **kwargs):
        defaults = {
            'location': '2', #  just in miles, none of that fancy GPS stuff here
            'r_cycle': '10',
            'g_cycle': '40',
            'offset': '0', # offset from an external decided time for the cycles to start
        }
        
        for key, default in defaults.items():
            setattr(self, key, kwargs.get(key, default))

    def tell_location(self):
        return 'This signal is located at mile marker {}.'.format(self.location)
        
    def tell_r_cycle(self):
        return 'The red light cycle for this signal {} seconds.'.format(self.r_cycle)
        
    def tell_g_cycle(self):
        return 'The green light cycle for this signal is {} seconds.'.format(self.g_cycle)
    
    def tell_offset(self):
        return 'The time offset for this signal is {} seconds.'.format(self.offset)
        
    @staticmethod    
    def generate_random_signal_data(min_location = 1, max_location = 10):
        data = {
            'location': random.randint(min_location, max_location), 
            'r_cycle': random.randint(10, 30), 
            'g_cycle': random.randint(25, 95),
            'offset': random.randint(0, 30),
        }
        
        return data


if __name__ == "__main__":
    data = Signal.generate_random_signal_data(1, 15)
    x = Signal(**data)
    print(x.tell_location())
    print(x.tell_r_cycle())
    print(x.tell_g_cycle())
    print(x.tell_offset())
    y = Signal()
    print(y.tell_location())
    print(y.tell_r_cycle())
    print(y.tell_g_cycle())
    print(y.tell_offset())
    