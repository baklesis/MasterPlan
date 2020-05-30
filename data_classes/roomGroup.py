class RoomGroup:
    def __init__(self, name, event_list, room_list):
        self._name = name
        self._event_list = event_list
        self._room_list = room_list
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def event_list(self):
        return self._event_list
    @event_list.setter
    def event_list(self, event):
        self._event_list.append(event)
    @property
    def room_list(self):
        return self._room_list
    @room_list.setter
    def room_list(self, room):
        self._room_list.append(room)

class RoomGroupList:
    def __init__(self, room_group_list, organization):
        self._room_group_list = room_group_list
        self._organization = organization
    @property
    def room_group_list(self):
        return self._room_group_list
    @room_group_list.setter
    def room_group_list(self, room_group_list):
        self._room_group_list = room_group_list
    def addRoomGroup(self,name,event_list,room_list):
        self._room_group_list.append(RoomGroup(name,event_list,room_list))