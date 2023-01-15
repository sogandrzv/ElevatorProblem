from Elevator import Elevator
from Passenger import Passenger


class Manager:

    def __init__(self):
        self.num_of_floors = 15
        self.req_list = []
        self.elevator = Elevator(9)

    def create_passenger(self, passenger_name, passenger_destination):
        passenger = Passenger(passenger_name, passenger_destination)
        self.req_list.append(passenger.destination)

    def run_elevator(self):
        print("req_list is: ", self.req_list)
        self.elevator.make_n_queue(self.req_list)


if __name__ == '__main__':
    manager = Manager()

    # all request comes parallel
    manager.create_passenger("a", 8)
    manager.create_passenger("b", 10)
    manager.create_passenger("c", 2)
    manager.create_passenger("d", 11)
    manager.create_passenger("e", 4)
    manager.create_passenger("f", 13)
    manager.create_passenger("g", 5)
    manager.create_passenger("h", 15)
    manager.create_passenger("i", 6)
    manager.create_passenger("j", 14)
    manager.create_passenger("k", 7)
    manager.create_passenger("l", 1)
    manager.create_passenger("n", 9)
    manager.create_passenger("m", 12)
    manager.create_passenger("o", 3)

    manager.run_elevator()

    print("total time it takes: ", manager.elevator.total_time)
    # print(manager.req_list)
#     # passenger = Passenger(f"x {1}", 1)
#     # passenger1 = Passenger(f"x {2}", 10)
#     # passenger2 = Passenger(f"x {3}", 2)
#     # passenger3 = Passenger(f"x {4}", 20)
#     # passenger4 = Passenger(f"x {5}", 4)
#     # passenger5 = Passenger(f"x {5}", 17)
#     # passenger6 = Passenger(f"x {5}", 5)
#     # passenger7 = Passenger(f"x {5}", 19)
#
#     req_list = [passenger.destination, passenger1.destination, passenger2.destination,
#                 passenger3.destination, passenger4.destination, passenger5.destination,
#                 passenger6.destination, passenger7.destination]
#     # arr = [9, 4, 6, 7, 10]
#     # arr1 = [4, 6, 1, 8, 9]
#     on_floor = 5
#     el = Elevator(on_floor)
#     el.add_static_req_list(req_list)
#     # el.add_passenger_to_buffers(passenger)
#     # el.add_passenger_to_buffers(passenger1)
#     # el.add_passenger_to_buffers(passenger2)
#     # el.add_passenger_to_buffers(passenger3)
#     # el.add_passenger_to_buffers(passenger4)
#
#     el.look_algo(on_floor)
#
#     # def new_buffer_create(self, buffer):
#     #     while len(buffer) != self.size_of_each_buffer:
#     #         return buffer
#     #     buffer1 = []
#     #     return buffer1
