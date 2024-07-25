from abc import ABCMeta, abstractmethod
from enum import Enum

class SpotSize(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2

class Vehicle(metaclass=ABCMeta):
    def __init__(self, vehicle_type, licence_plate, spot_size):
        self.vehicle_type = vehicle_type
        self.licence_plate = licence_plate
        self.spot_size = spot_size
        self.spots_taken = list()

    def clear_spots(self):
        for spot in self.spots_taken:
            spot.remove(self)

    def take_spot(self, spot):
        self.spots_taken.append(spot)

    @abstractmethod
    def fits(self, spot):
        pass

class Motorcycle(Vehicle):
    def __init__(self, licence_plate):
        super(Motorcycle, self).__init__(SpotSize.SMALL, licence_plate, spot_size=1)

    def fits(self, spot):
        return True
    
def Car(Vehicle):
    def __init__(self, licence_plate):
        super(Car, self).__init__(SpotSize.MEDIUM, licence_plate, spot_size=1)

    def fits(self, spot):
        return True if spot.size == SpotSize.LARGE or spot.size == SpotSize.MEDIUM else False
    
def Bus(Vehicle):
    def __init__(self, licence_plate):
        super(Bus, self).__init__(SpotSize.LARGE, licence_plate, spot_size=5)

    def fits(self, spot):
        return True if spot.size == SpotSize.LARGE else False

class CarPark(object):
    def __init__(self, num_levels):
        self.num_levels = num_levels
        self.levels = list()

    def park(self, vehicle):
        for level in self.levels:
            if level.park(vehicle):
                return True
        return False
    
class Level(object):
    SPOTS_PER_ROW = 10

    def __init__(self, level_num, total_spots):
        self.level_num = level_num
        self.total_spots = total_spots
        self.available_spots = 0
        self.spots = list()

    def free_spot(self):
        self.available_spots += 1

    def park(self, vehicle):
        spot = self._find_available_spot(vehicle)
        if not spot:
            return None
        else:
            spot.park(vehicle)
            return spot

    def _find(self, vehicle):
        """Find an available spot where the vehicle can fit; else, return None"""

    def _park(self, spot, vehicle):
        """Take the spots starting at spot.spot_num to vehicle.spot_size"""

class Spot(object):
    def __init__(self, level_num, row, spot_num, spot_size, vehicle_size):
        self.level = level_num
        self.row = row
        self.spot_num = spot_num
        self.spot_size = spot_size
        self.vehicle_size = vehicle_size

    def available(self):
        return True if self.vehicle is None else False

    def fits(self, vehicle):
        if self.vehicle:
            return False
        return vehicle.fits(self)

    def park(self, vehicle):
        """Take this spot"""

    def remove(self, vehicle):
        """Free this spot"""
