from global_vars import *
import csv
class Room:
    def __init__(self, name, building, floor, capacity):
        self._name = name
        self._building = building
        self._floor = floor
        self._capacity = capacity
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def building(self):
        return self._building
    @building.setter
    def building(self,building):
        self._building=building
    @property
    def floor(self):
        return self._floor
    @floor.setter
    def floor(self,floor):
        self._floor=floor
    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

class RoomList:
    def __init__(self, room_list):
        self._room_list = room_list
    def __init__(self, room_list,organization):
        self.room_list = room_list
        self.__organization=organization
    @property
    def room_list(self):
        return self._room_list
    @room_list.setter
    def room_list(self,room_list):
        self._room_list = room_list

    def convertToCSV(self):
        # convert data to csv
        f = open("room.csv", "w")
        for x in range(len(self._room_list)):
            for y in range(len(self.room)):
                line = str(x + 1) + ',' + str(self.room.name) + ',' + str(self.room.building) + ',' + str(self.room.floor) + ',' + str(self.room.capacity) + '\n'
                f.write(line)
        f.close()
        return self

    def createRoomList(self,file):
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.room_list.append()
        return self.room.list

    def validateFile(self):
        csv_file = open(self.listFile, 'rb')
        try:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
        except csv.Error:
            return self

