room_Dict = {}
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
        try:
            for i in room_Dict:
                print(i, room_Dict[i])
            roomNum = input("For what room do you want to change the rent amount?:")
            newRent = input("Enter the rent amount that you want to adjust to: $")
            room_Dict[roomNum] = newRent
        except:
            print("An unexpected error has occured. Try again.")

    @staticmethod
    def add_room():
        pass

    @staticmethod
    def remove_room():
        pass

    @staticmethod
    def read_from_database(room_filename):
        pass
