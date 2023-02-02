

class Passenger:
    def __init__(self, floor, type_of_req):
        self.destination = floor
        self.status = False
        self.type_of_req = type_of_req

    def __str__(self):
        return f"dest = {self.destination}, type = {self.type_of_req}"


