class Room:
    def __init__(self, room_type):
        self.room_type = room_type

class House:
    def __init__(self):
        # Composition: Rooms are instantiated inside the House
        self.rooms = [Room("Living Room"), Room("Kitchen"), Room("Bedroom")]

# Example Usage
if __name__ == "__main__":
    my_house = House()
    print("[Composition] House contains the following rooms:")
    for room in my_house.rooms:
        print(f" - {room.room_type}")