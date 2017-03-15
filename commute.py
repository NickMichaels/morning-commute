import datetime
import random

from road import Road
from vehicle import Vehicle
from signal import Signal

class Commute:
    """The summary line for a class docstring should fit on one line.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def create_scenario(self):
        road_data = Road.generate_random_road_data()
        self.road = Road(**road_data)
        # determine number of signals to create
        num_signals = int( self.road.length / 4 )
        
        self.signals = []
        
        for x in range(1, num_signals):
            signal_data = Signal.generate_random_signal_data(x, self.road.length )
            signal = Signal(**signal_data)
            self.signals.append(signal)
        
        vehicle_data = Vehicle.generate_random_vehicle_data();
        self.vehicle = Vehicle(**vehicle_data)
        

    def tell_road_data(self):
        str = 'The road data is as follows:'
        road_attrs = [a for a in dir(self.road) if not a.startswith('__') and not callable(getattr(self.road,a))]
        print(road_attrs)
        
        return str
          
    
    
if __name__ == "__main__":
    c = Commute()
    c.create_scenario()
    print(c.road.tell_road_name())
    print(c.road.tell_road_length())
    print(c.road.tell_speed_limit())
    for s in c.signals:
        print(s.tell_location())
        print(s.tell_r_cycle())
        print(s.tell_g_cycle())
        print(s.tell_offset())
    print(c.vehicle.tell_make())
    print(c.vehicle.tell_model())
    print(c.vehicle.tell_fuel_efficiency())
    print(c.vehicle.tell_fuel())



