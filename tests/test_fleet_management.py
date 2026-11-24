
import unittest

from src.fleet_management import Vehicle, PassengerCar, CargoTruck, generate_fleet_manifest


class TestFleetManagement(unittest.TestCase):

    # TC01: Test passenger car creation
    def test_create_passenger_car(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)

        self.assertEqual(car.vehicle_id, "CAR101")
        self.assertEqual(car.model, "Toyota Corolla")
        self.assertEqual(car.daily_rate, 75.0)
        self.assertEqual(car.num_seats, 5)

    # TC02: Test cargo truck creation
    def test_create_cargo_truck(self):
        truck = CargoTruck("TRK101", "Volvo FH", 150.0, 10.0)

        self.assertEqual(truck.vehicle_id, "TRK101")
        self.assertEqual(truck.model, "Volvo FH")
        self.assertEqual(truck.daily_rate, 150.0)
        self.assertEqual(truck.cargo_capacity_tons, 10.0)

    # TC03: Test abstract Vehicle class
    def test_vehicle_is_abstract(self):
        with self.assertRaises(TypeError):
            Vehicle("V101", "Vehicle", 100.0)

    # TC04: Test passenger car rental calculation
    def test_passenger_car_rental_cost(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)

        cost = car.calculate_rental_cost(3)

        self.assertEqual(cost, 300.0)

    # TC05: Test cargo truck rental calculation
    def test_cargo_truck_rental_cost(self):
        truck = CargoTruck("TRK101", "Volvo FH", 150.0, 10.0)

        cost = truck.calculate_rental_cost(3)

        self.assertEqual(cost, 950.0)

    # TC06: Test daily rate update
    def test_update_daily_rate(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)

        car.daily_rate = 85.0

        self.assertEqual(car.daily_rate, 85.0)

    # TC07: Test zero daily rate
    def test_zero_daily_rate(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)

        with self.assertRaises(ValueError):
            car.daily_rate = 0.0

    # TC08: Test negative daily rate
    def test_negative_daily_rate(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)

        with self.assertRaises(ValueError):
            car.daily_rate = -20.0

    # TC09: Test vehicle sorting
    def test_sort_vehicles_by_daily_rate(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)
        car2 = PassengerCar("CAR102", "Honda Civic", 60.0, 4)
        truck = CargoTruck("TRK101", "Volvo FH", 150.0, 10.0)

        fleet = [truck, car, car2]

        sorted_fleet = sorted(fleet)

        self.assertEqual(
            [vehicle.daily_rate for vehicle in sorted_fleet],
            [60.0, 75.0, 150.0]
        )

    # TC10: Test polymorphic fleet manifest
    def test_generate_fleet_manifest(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)
        truck = CargoTruck("TRK101", "Volvo FH", 150.0, 10.0)

        fleet = [car, truck]

        # The function should run without errors
        generate_fleet_manifest(fleet, 3)

    # TC11: Test string representation of vehicles
    def test_vehicle_string(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)
        truck = CargoTruck("TRK101", "Volvo FH", 150.0, 10.0)

        self.assertIn("Toyota Corolla", str(car))
        self.assertIn("Volvo FH", str(truck))
        self.assertIn("Passenger Car", str(car))
        self.assertIn("Cargo Truck", str(truck))

    # TC12: Test valid positive rental rate
    def test_positive_daily_rate(self):
        car = PassengerCar("CAR101", "Toyota Corolla", 75.0, 5)

        car.daily_rate = 100.0

        self.assertEqual(car.daily_rate, 100.0)


if __name__ == "__main__":
    unittest.main()
