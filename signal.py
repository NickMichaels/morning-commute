import random


class Signal:
    """ Class to create a "signal" that will be placed on a road

    Attributes:
        location (str): Location of the signal, should correspond to a mile
                        marker within the confines of a road.
        r_cycle (int): Amount of time in seconds that the signal is red.
        g_cycle (int): Amount of time in seconds that the signal is green.
        offset (int): Amount of time in seconds that the lights start time
                      is offset from a standard start time
    """

    def __init__(self, **kwargs):
        defaults = {
            'location': '2',
            'r_cycle': '10',
            'g_cycle': '40',
            'offset': '0',
        }

        for key, default in defaults.items():
            setattr(self, key, kwargs.get(key, default))

    def state_location(self):
        """
        Returns a formatted string stating the location of the signal on a road
        """
        line = 'This signal is located at mile marker {}.'
        return line.format(self.location)

    def state_r_cycle(self):
        """
        Returns a formatted string stating the red light cycle in seconds
        """
        line = 'The red light cycle for this signal {} seconds.'
        return line.format(self.r_cycle)

    def state_g_cycle(self):
        """
        Returns a formatted string stating the green light cycle in seconds
        """
        line = 'The green light cycle for this signal is {} seconds.'
        return line.format(self.g_cycle)

    def state_offset(self):
        """
        Returns a formatted string stating the offset in seconds
        """
        line = 'The time offset for this signal is {} seconds.'
        return line.format(self.offset)

    @staticmethod
    def generate_random_signal_data(min_location=1, max_location=10):
        """
        Generate random signal data to pass to a new signal object

        Args:
            min_location: Minimum mile marker for signal placement
            max_location: Maximum mile amrker for signal placement

        Returns:
            A dict of data to pass to a new signal object
        """
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
    print(x.state_location())
    print(x.state_r_cycle())
    print(x.state_g_cycle())
    print(x.state_offset())
    y = Signal()
    print(y.state_location())
    print(y.state_r_cycle())
    print(y.state_g_cycle())
    print(y.state_offset())
