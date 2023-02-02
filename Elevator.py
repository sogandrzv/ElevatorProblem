import math
import random
import time


class Elevator:

    def __init__(self, floor):
        self.on_floor = floor
        self.direction = 0
        self.is_running = False
        self.is_up_or_dwn_request = "up"
        self.all_request_list = []
        self.total_time = 0
        self.size_of_each_buffer = 0  # n is changeable
        self.door_status = False  # True: door is open, False: door is close

    def calculate_in_dir_req(self, req_list):
        req_list.sort(key=lambda x: x.destination, reverse=False)
        request_in_up_dir = []
        request_in_down_dir = []

        for passenger in req_list:
            if passenger.destination > self.on_floor:
                request_in_up_dir.append(passenger)
            elif passenger.destination < self.on_floor:
                request_in_down_dir.append(passenger)

        request_in_up_dir.sort(key=lambda x: x.destination, reverse=False)
        request_in_down_dir.sort(key=lambda x: x.destination, reverse=True)

        return request_in_up_dir, request_in_down_dir

    # chose which in direction goes first for lower cost
    def select_direction(self, req_list):
        # print("req ", req_list)
        down_dis = abs(self.on_floor - req_list[0].destination)
        up_dis = abs(self.on_floor - req_list[len(req_list) - 1].destination)
        # print(f"down {down_dis}, up{up_dis}")
        direction = -1 if down_dis < up_dis else 1
        # print("return dir is : ", direction)
        return direction

    def look_algo(self, req_list):
        req_in_up_dir, req_in_down_dir = self.calculate_in_dir_req(req_list)
        direction = self.select_direction(req_list)
        run = 2
        num_of_change_dir = 0
        # print("number of change dir is : ", direction)
        #
        while run:
            if direction == 1:
                for passenger in req_in_up_dir:
                    dist = abs(passenger.destination - self.on_floor)

                    self.close_door(self.on_floor)
                    time.sleep(0.1)
                    print(f"is running: {self.is_running}")
                    while self.on_floor < passenger.destination:
                        self.on_floor += 1

                    self.open_door(self.on_floor)

                    if passenger.type_of_req == "external":
                        self.all_request_list.remove(passenger)

                        passenger.type_of_req = "internal"
                        x = random.randint(0, 14)
                        # if random generate a number that is eq to current floor -> generate new number
                        while x == passenger.destination:
                            x = random.randint(0, 14)

                        # x = int(input("please choose your destination: "))

                        passenger.destination = x
                        self.all_request_list.append(passenger)

                    elif passenger.type_of_req == "internal":
                        self.all_request_list.remove(passenger)

                    print(f"is running: {self.is_running}")
                    # req_in_up_dir.remove(passenger)

                    self.total_time += dist
                    # req_in_up_dir.remove(passenger)
                    # print(req_in_up_dir)

                    print("on floor : ", self.on_floor)

                num_of_change_dir += 1
                direction = -1

            elif direction == -1:
                for passenger in req_in_down_dir:
                    dist = abs(passenger.destination - self.on_floor)

                    self.close_door(self.on_floor)
                    time.sleep(0.1)
                    print(f"is running: {self.is_running}")
                    while self.on_floor > passenger.destination:
                        self.on_floor -= 1

                    self.open_door(self.on_floor)

                    if passenger.type_of_req == "external":
                        self.all_request_list.remove(passenger)

                        passenger.type_of_req = "internal"
                        x = random.randint(0, 14)
                        # if random generate a number that is eq to current floor -> generate new number
                        while x == passenger.destination:
                            x = random.randint(0, 14)

                        # x = int(input("please choose your destination: "))

                        passenger.destination = x
                        self.all_request_list.append(passenger)

                    elif passenger.type_of_req == "internal":
                        self.all_request_list.remove(passenger)

                    print(f"is running: {self.is_running}")
                    # self.all_request_list.remove(passenger)

                    # req_in_down_dir.remove(passenger)

                    self.total_time += dist

                    # req_in_down_dir.remove(passenger)

                    print("on floor : ", self.on_floor)

                num_of_change_dir += 1
                direction = 1
            run -= 1

            # print("number of change dir is : ", direction)

    # make n queue for N-step-look
    def make_n_queue(self, req_list):

        self.size_of_each_buffer = math.ceil(len(req_list) / 2)
        print("N = ", self.size_of_each_buffer)

        for passenger in req_list:
            self.all_request_list.append(passenger)
        # self.all_request_list = req_list

        for i in self.all_request_list:
            if self.on_floor == i.destination:
                self.open_door(self.on_floor)
                self.all_request_list.remove(self.on_floor)
        # print("req list =", self.all_request_list)

        # if head is in req_list -> open the door

        while len(self.all_request_list) != 0:
            n = self.size_of_each_buffer
            n_buffer = [self.all_request_list[i:i + n] for i in range(0, len(self.all_request_list), n)]

            if len(n_buffer) == 1:
                buffer0 = n_buffer[0]
                self.look_algo(buffer0)

            if len(n_buffer) == 2:
                buffer0 = n_buffer[0]
                buffer1 = n_buffer[1]
                self.look_algo(buffer0)
                self.look_algo(buffer1)

            if len(n_buffer) == 3:
                buffer0 = n_buffer[0]
                buffer1 = n_buffer[1]
                buffer2 = n_buffer[2]
                self.look_algo(buffer0)
                self.look_algo(buffer1)
                self.look_algo(buffer2)

            if len(n_buffer) == 4:
                buffer0 = n_buffer[0]
                buffer1 = n_buffer[1]
                buffer2 = n_buffer[2]
                buffer3 = n_buffer[3]
                self.look_algo(buffer0)
                self.look_algo(buffer1)
                self.look_algo(buffer2)
                self.look_algo(buffer3)

        return True

    def open_door(self, floor):
        self.is_running = False
        print(f"in floor {floor} opening the door")
        self.door_status = True

    def close_door(self, floor):
        print(f"in floor {floor} closing the door ")
        self.door_status = False
        self.is_running = True

    def reset_params(self):
        self.all_request_list = []
        self.is_running = False
        # for req in req_list:
        # count += 1
        # if count != self.size_of_each_buffer:
        #     buffer = []
        #     buffer.append(req)

    # def add_passenger_to_buffers(self, passenger):
    #     if len(self.buffer) != self.size_of_each_buffer:
    #         self.buffer.append(passenger.floor)
    #     elif len(self.buffer1) != self.size_of_each_buffer:
    #         self.buffer1.append(passenger.floor)
