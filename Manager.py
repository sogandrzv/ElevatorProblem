import threading
import time
from Elevator import Elevator
from Passenger import Passenger


class Manager:

    def __init__(self):
        self.num_of_floors = 15
        self.req_list = []
        self.elevator = Elevator(0)
        self.is_elevator_exec_last_list = True

    def create_passenger(self, passenger_destination, passenger_type):
        passenger = Passenger(passenger_destination, passenger_type)
        self.req_list.append(passenger)

    def run_elevator(self):
        # self.is_elevator_exec_last_list = False
        # for i in self.req_list:
        #     print(i)
        # print("req_list is: ", self.req_list)
        self.elevator.make_n_queue(self.req_list)


if __name__ == '__main__':
    manager = Manager()


    def get_input(req_queue):
        manager.req_list = req_queue
        while True:
            type_req = input("please choose type of your request (internal or external): ")
            if type_req == "internal":
                destination = int(input("Please select your destination: "))
                manager.create_passenger(destination, "none")
            elif type_req == "external":
                up_down = input("up or down request? ")
                destination = int(input("Please say where you are: "))
                manager.create_passenger(destination, up_down)


    # while 2:
    #     req_queue = []
    #     t = threading.Thread(target=get_input, args=(req_queue, ))
    #     t.start()
    #     time.sleep(30)
    #     # if manager.is_elevator_exec_last_list:
    #     manager.run_elevator()
    #     print("total time it takes: ", manager.elevator.total_time)

    # all request comes parallel
    manager.create_passenger(8, "internal")
    manager.create_passenger(5, "external")
    manager.create_passenger(10, "internal")
    manager.create_passenger(2, "internal")
    manager.create_passenger(11, "external")
    manager.create_passenger(4, "internal")
    manager.create_passenger(13, "internal")
    manager.create_passenger(5, "external")

    manager.run_elevator()

