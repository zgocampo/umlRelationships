class Car:
    def start_engine(self):
        return "Engine started successfully."

class Driver:
    def drive(self, car):
        # Driver depends on Car temporarily within this method
        return car.start_engine()

# Example Usage
if __name__ == "__main__":
    my_car = Car()
    driver = Driver()
    print(f"[Dependency] Driver action: {driver.drive(my_car)}")