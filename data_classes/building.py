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
        return self