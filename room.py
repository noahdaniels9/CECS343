
class Room:
    number: int = 0
    rent: float = 0

    def __init__(self, number, rent):
        self.number = number
        self.rent = rent

    def display(self):
        """Display this room's information"""
        print(f'Room number: {self.number}\n'
              f'Rent: ${self.rent}')

    def adjust_rent(self):
        pass

    @staticmethod
    def add_room():
        pass

    @staticmethod
    def remove_room():
        pass

    @staticmethod
    def read_from_database(room_filename):
        pass