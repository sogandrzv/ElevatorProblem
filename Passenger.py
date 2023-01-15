import random


class Passenger:
    def __init__(self, name, floor):
        self.destination = floor
        # list_floors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # self.requested_floor = random.choice(list(filter(lambda ele: ele != floor, list_floors)))
        self.name = name
        self.status = 'waiting'

# if __name__ == '__main__':
#     e = Passenger(4)
#     print(e.requested_floor)
