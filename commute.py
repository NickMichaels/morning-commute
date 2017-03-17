import datetime
import random

from road import Road
from vehicle import Vehicle
from signal import Signal


class Commute:
    """
    Class to create a scenario of a morning commute
    """

    def create_scenario(self):
        """
        Create the scenrario here, some of this could be moved to an __init__
        """
        road_data = Road.generate_random_road_data()
        self.road = Road(**road_data)
        # determine number of signals to create
        num_signals = int(self.road.length / 4)

        self.signals = []

        for x in range(1, num_signals):
            data = Signal.generate_random_signal_data(x, self.road.length)
            signal = Signal(**data)
            self.signals.append(signal)

        vehicle_data = Vehicle.generate_random_vehicle_data()
        self.vehicle = Vehicle(**vehicle_data)

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
