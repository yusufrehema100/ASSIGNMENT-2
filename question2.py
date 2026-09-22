from abc import ABC, abstractmethod

# Parent abstract class
class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

# Subclasses with their fare rules
class Taxi(Transport):
    def calculate_fare(self, distance):
        return 5000 + (2000 * distance)

class Bus(Transport):
    def calculate_fare(self, distance):
        return 1000 * distance

class Motorcycle(Transport):
    def calculate_fare(self, distance):
        return 2000 + (1500 * distance)

# Creating the objects
taxi_obj = Taxi()
bus_obj = Bus()
bike_obj = Motorcycle()

# Store in a list and set distance to 10
my_trips = [taxi_obj, bus_obj, bike_obj]
km = 10

print("--- System Fare Rates ---")

# Polymorphism loop
for vehicle in my_trips:
    total_fare = vehicle.calculate_fare(km)
    name = vehicle.__class__.__name__
    
    print("Vehicle Type:", name)
    print("Distance:", km, "km")
    print("Fare: UGX", total_fare)
    print("--------------------")