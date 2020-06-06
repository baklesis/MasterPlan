import csv

class Building:
    def __init__(self, name, organization, room_list):
        self._name = name
        self._organization = organization
        self._room_list = room_list
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def organization(self):
        return self._organization
    @organization.setter
    def organization(self, organization):
        self._organization = organization
    @property
    def room_list(self):
        return self._room_list
    @room_list.setter
    def room_list(self, room):
        self._room_list.append(room)

class BuildingList:
    def __init__(self,building_list, organization):
        self._building_list = building_list
        self._organization = organization
    @property
    def building_list(self):
        return self._building_list
    @building_list.setter
    def building_list(self,building_list):
        self._building_list = building_list
    @property
    def organization(self):
        return self._organization
    @organization.setter
    def organization(self, organization):
        self._organization = organization
    def createBuildingList(self,file):
        return self
    def convertToCSV(self):
        # convert data to csv
        f = open("building.csv", "w")
        for x in range(len(self.building_list)):
            for y in range(len(self.building)):
                line = str(x + 1) + ',' + str(self.building.name) + ',' + str(self.building._organization) + '\n'
                f.write(line)
        f.close()
        return self

    def createRoomList(self, file):
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.building_list.append()
        return self.building_list

    def validateFile(self):
        csv_file = open(self.listFile, 'rb')
        try:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
        except csv.Error:
            return self