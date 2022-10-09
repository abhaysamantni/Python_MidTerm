# The DroneSet defines a class that stores attributes and methods pertaining to various drone sets
import math


class HWSet:

    def __init__(self, qty):
        self.__capacity = qty
        self.__availability = self.__capacity
        self.__checkedout = 0

    def check_out(self, qty):
        if (qty < self.__availability):
            self.__availability = self.__availability - qty
            self.__checkedout += qty
            return 0
        else:
            self.__checkedout += self.__availability
            self.__availability = 0
            return -1

    def check_in(self, qty):
        if ((qty >= 0) and (qty < self.__checkedout)):
            self.__availability += qty
            return 0
        else:
            return -1

    def get_availability(self):
        return self.__availability

    def get_capacity(self):
        return self.__capacity

    def get_checkedout_qty(self):
        return self.__checkedout


class DroneSet(HWSet):

    def __init__(self, qty, payload):
        HWSet.__init__(self, qty)
        self.__payload = payload

    def get_payload(self):
        return self.__payload

    def set_payload(self, payload):
        self.__payload = payload