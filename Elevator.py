import math
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
        self.door_status = False        # True: door is open, False: door is close

        # self.buffer0 = []
        # self.buffer1 = []
        # self.buffer2 = []
        # self.buffer3 = []
    def add_passenger_to_elevator(self):
        pass

    def calculate_in_dir_req(self, req_list):
        req_list.sort()
        request_in_up_dir = []
        request_in_down_dir = []

        for floor in req_list:
            if floor > self.on_floor:
                request_in_up_dir.append(floor)
            elif floor < self.on_floor:
                request_in_down_dir.append(floor)

        request_in_up_dir.sort()
        request_in_down_dir.sort(reverse=True)

        return request_in_up_dir, request_in_down_dir

    # chose which in direction goes first for lower cost
    def select_direction(self, req_list):
        # print("req ", req_list)
        down_dis = abs(self.on_floor - req_list[0])
        up_dis = abs(self.on_floor - req_list[len(req_list) - 1])
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

        while run:
            if direction == 1:
                for floor in req_in_up_dir:
                    dist = abs(floor - self.on_floor)

                    self.close_door(self.on_floor)
                    time.sleep(0.1)
                    print(f"is running: {self.is_running}")

                    self.on_floor += dist

                    self.open_door(self.on_floor)
                    print(f"is running: {self.is_running}")

                    self.total_time += dist
                    # req_in_up_dir.remove(floor)
                    # print(req_in_up_dir)

                    print("on floor : ", self.on_floor)

                num_of_change_dir += 1
                direction = -1

            elif direction == -1:
                for floor in req_in_down_dir:
                    dist = abs(floor - self.on_floor)

                    self.close_door(self.on_floor)
                    time.sleep(0.1)
                    print(f"is running: {self.is_running}")

                    self.on_floor -= dist

                    self.open_door(self.on_floor)
                    print(f"is running: {self.is_running}")

                    self.total_time += dist

                    # req_in_down_dir.remove(floor)

                    print("on floor : ", self.on_floor)

                num_of_change_dir += 1
                direction = 1
            run -= 1
            # print("number of change dir is : ", direction)

    # make n queue for N-step-look
    def make_n_queue(self, req_list):

        self.size_of_each_buffer = math.ceil(len(req_list) / 2)
        print("N = ", self.size_of_each_buffer)
        self.all_request_list = req_list

        # if head is in req_list -> open the door
        if self.on_floor in self.all_request_list:
            self.open_door(self.on_floor)
            self.all_request_list.remove(self.on_floor)

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
        print(f"in floor {floor} opening the door")
        self.door_status = True
        self.is_running = False

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
