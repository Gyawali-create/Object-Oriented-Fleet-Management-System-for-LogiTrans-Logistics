
from abc import ABC, abstractmethod


# Task 1: Abstract Base Class
class Vehicle(ABC):

    def __init__(self, vehicle_id, model, daily_rate):
        self.vehicle_id = vehicle_id
        self.model = model

        # Use the setter to validate the daily rate
        self.daily_rate = daily_rate

    # Task 2: Encapsulation using property getter
    @property
    def daily_rate(self):
        return self.__daily_rate

    # Task 2: Encapsulation using property setter
    @daily_rate.setter
    def daily_rate(self, value):
        if value <= 0.0:
            raise ValueError("Daily rental rate must be greater than zero.")

        self.__daily_rate = value

    # Abstract method
    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    # Operator overloading: compare vehicles by daily rate
    def __lt__(self, other):
        return self.daily_rate < other.daily_rate


# Task 3: PassengerCar inherits from Vehicle
class PassengerCar(Vehicle):

    def __init__(self, vehicle_id, model, daily_rate, num_seats):
        super().__init__(vehicle_id, model, daily_rate)
        self.num_seats = num_seats

    # Task 4: Method overriding
    def calculate_rental_cost(self, days):
        return (self.daily_rate * days) + (15.0 * self.num_seats)

    # Operator overloading: vehicle description
    def __str__(self):
        return (
            f"Passenger Car | ID: {self.vehicle_id} | "
            f"Model: {self.model} | Seats: {self.num_seats} | "
            f"Daily Rate: ${self.daily_rate:.2f}"
        )


# Task 3: CargoTruck inherits from Vehicle
class CargoTruck(Vehicle):

    def __init__(self, vehicle_id, model, daily_rate, cargo_capacity_tons):
        super().__init__(vehicle_id, model, daily_rate)
        self.cargo_capacity_tons = cargo_capacity_tons

    # Task 4: Method overriding
    def calculate_rental_cost(self, days):
        return (self.daily_rate * days) + (50.0 * self.cargo_capacity_tons)

    # Operator overloading: vehicle description
    def __str__(self):
        return (
            f"Cargo Truck | ID: {self.vehicle_id} | "
            f"Model: {self.model} | Capacity: "
            f"{self.cargo_capacity_tons} tons | "
            f"Daily Rate: ${self.daily_rate:.2f}"
        )


# Polymorphism: Processes different vehicle types using common methods
def generate_fleet_manifest(fleet_list, days):

    print(f"\nFleet Rental Manifest for {days} days")
    print("=" * 65)

    for vehicle in fleet_list:
        print(vehicle)
        print(f"Total Rental Cost: ${vehicle.calculate_rental_cost(days):.2f}")
        print("-" * 65)


# Main program
if __name__ == "__main__":

    # Create passenger cars
    car1 = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)
    car2 = PassengerCar("CAR102", "Honda Civic", 60.0, 4)

    # Create cargo trucks
    truck1 = CargoTruck("TRK101", "Volvo FH", 150.0, 10.0)
    truck2 = CargoTruck("TRK102", "MAN TGX", 180.0, 15.0)

    # Store vehicles in one mixed fleet
    fleet = [car1, car2, truck1, truck2]

    # Generate fleet manifest for 3 days
    generate_fleet_manifest(fleet, 3)

    # Sort vehicles according to daily rental rate
    print("\nVehicles Sorted by Daily Rental Rate")
    print("=" * 65)

    sorted_fleet = sorted(fleet)

    for vehicle in sorted_fleet:
        print(f"{vehicle.model}: ${vehicle.daily_rate:.2f} per day")

    # Update rental rate
    print("\nUpdating Daily Rental Rate")
    print("=" * 65)

    car1.daily_rate = 85.0
    print(f"Updated rate for {car1.model}: ${car1.daily_rate:.2f}")

    # Test invalid rental rate
    print("\nTesting Invalid Rental Rate")
    print("=" * 65)

    try:
        car1.daily_rate = -20.0
    except ValueError as error:
        print(f"Validation Error: {error}")
