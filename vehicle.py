class Vehicle:
    def __init__(self, weight, color, owner):

        if not isinstance(weight, float):
            raise ValueError("Weight must be a number.")

        if not isinstance(color, str):
            raise ValueError("Color must be a string.")

        if not isinstance(owner, str):
            raise ValueError("Owner must be a string.")

        self.weight = weight
        self.color = color
        self.owner = owner

class Car(Vehicle):
    def __init__(self, weight, color, owner, registration_nr, horse_power):
        Vehicle.__init__(self, weight, color, owner)

        if not isinstance(registration_nr, str):
            raise ValueError("Registration number must be a string.")

        if not isinstance(horse_power, int):
            raise ValueError("Horse power must be a integer.")

        self.reg_nr = registration_nr
        self.hp = horse_power

class Truck(Car):
    def __init__(self, weight, color, owner, registration_nr, horse_power):
        Car.__init__(self, weight, color, owner, registration_nr, horse_power)



truck = Truck(10000.0, "green", "George Obama", "abc-123", 9001)

print truck.owner








