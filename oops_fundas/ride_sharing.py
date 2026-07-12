"""
Exercise 2: The Ride-Sharing App (Uber/Lyft Style)
 Your Task
       Create a base class Vehicle:
          Attributes: driver_name, license_plate, and base_fare (default to $5.00).
          Method: calculate_fare(distance) — Formula: base_fare + (distance * 1.5).
       Create a child class LuxuryRide (inherits from Vehicle):
          Change the base_fare to $15.00.
          Override calculate_fare(distance) — Formula: base_fare + (distance * 3.0).
       Create a child class SharedRide (inherits from Vehicle):
          Override calculate_fare(distance) — Calculate the normal vehicle fare, but apply a 20% discount because the ride is shared.
"""


class Vehicle:

    def __init__(self, name, licenseplate, fare=5.00):
        self.driver_name = name
        self.license_plate = licenseplate
        self.base_fare = fare

    def calculate_fare(self, distance):
        return self.base_fare + (distance * 1.5)


class LuxuryRide(Vehicle):

    def __init__(self, name, licenseplate, fare=15.00):
        super().__init__(name, licenseplate, fare)

    def calculate_fare(self, distance):
        return self.base_fare + (distance * 3.0)


class SharedRide(Vehicle):

    def __init__(self, name, licenseplate, fare=1.5):
        super().__init__(name, licenseplate, fare)

    def calculate_fare(self, distance):
        return self.base_fare + (distance * 1.5) * 0.8


bike = Vehicle("Varun", "PB027856", 5.00)
print(bike.calculate_fare(20))

car = LuxuryRide("Pranav", "PB014582", 10.00)
print(car.calculate_fare(40))

shared_car = SharedRide("Amit", "PB456522", 1.5)
print(shared_car.calculate_fare(40))
