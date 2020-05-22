from datetime import datetime

class Account:
    def __init__(self, username, password, email):
        self._username=username
        self._password=password
        self._email=email
    
    def get_username():
        return self._username
    def set_username(username):
        self._username=username
    def get_password():
        return self._password
    def set_password(password):
        self._password=password
    def get_email():
        return self._email
    def set_email(email):
        self._email=email
        

class Organizer(Account):
    def __init__(self, fullname, organization):
        self._fullname=fullname
        self._organization=organization
    
    def get_fullname():
        return self._fullname
    def set_fullname(fullname):
        self._fullname=fullname
    def get_organization():
        return self._organization
    def set_organization(organization):
        self._organization=organization

class Admin(Account):
    pass

class Message:
    def __init__(self, recipient, author, text):
        self._recipient=recipient
        self._author=author
        self._text=text
        self._timestamp=datetime.now()

    def get_recipient():
        return self._recipient
    def set_recipient(recipient):
        self._recipient=recipient
    def get_author():
        return self._author
    def set_author(author):
        self._author=author
    def get_text():
        return self._text
    def set_text(text):
        self._text=text

        
class OrganizerList:
    def __init__(self, organizer_list):
        self._organizer_list=organizer_list

    def get_organizer_list():
        return self._organizer_list
    def set_organizer_list(organizer_list):
        self._organizer_list=organizer_list

class Session:
    def __init__(self, user, building, floor, filters):
        self.user = user
        self.building = building
        self.floor = floor
        self.filters = filters
    
class Building:
    def __init__(self, name, organization, room_list):
        self.name = name
        self.organization = organization
        self.room_list = room_list

class BuildingList:
    def __init__(self):
        self._building_list= building_list
    
    @property    
    def building_list(self):
        return self._building_list
    
    @building_list.setter
    def building_list(self, ):
        self._building_list= building_list

    @building_list.deleter
    def building_list(self):
        del self._building_list

class Room:
    def __init__(self, name, building, floor, capacity, group):
        self.name = name
        self.building = building
        self.floor = floor
        self.capacity = capacity
        self.group = group
    


class RoomList:
    def __init__(self, room_list):
        self.room_list = room_list
    @property    
    def room_list(self):
        return self._room_list
    
    @room_list.setter
    def room_list(self, ):
        self._room_list=room_list

    @room_list.deleter
    def room_list(self):
        del self._room_list

class Schedule:
    def __init__(self,event_list):
        self.__event_list=event_list
        self.__timestamp_created=datetime.now()
        self.__published=False

    def get_event_list():
        return self.__event_list
    def get_timestamp():
        return self.__timestamp_created
    def get_published():
        return self.__published
    def publish():
        self.__published=True
    def unpublish():
        self.__published=False

class Event:
    def __init__(self,name,duration):
        self.__name=name
        self.__duration=duration
        self.__organizer=None
        self.__tag_list= []
        self.__constraint_list= []
        self.__timestamp_created=datetime.now()

    def get_name():
        return self.__name
    def get_duration():
        return self.__duration
    def get_organizer():
        return self.__organizer
    def set_organizer(organizer):
        self.__organizer=organizer
    def add_tag(tag):
        self.__tag_list.append(tag)
        tag.add_event(self)
    def remove_tag(tag):
        self.__tag_list.remove(tag)
        tag.remove_event(self)
    def add_constraint(constraint):
        self.__constraint_list.append(constraint)
    def remove_constraint(constraint):
        self.__constraint_list.remove(constraint)
    def get_timestamp():
        return self.__timestamp_created

class Tag:
    def __init__(self,name):
        self.__name=name
        self.__event_list= []

    def get_name():
        return self.__name
    def get_event_list():
        return self.__event_list
    def add_event(event):
        self.__event_list.append(event)
    def remove_event(event):
        self.__event_list.remove(event)

from  datetime import datetime
class Announcement:
    def __init__(self,text,timestamp,):
         self.text=text
         self.timestamp=datetime.now()
    def get_text(self):
         text= self.organizer 
            
class TimeConstraint:
    def __init__(self,datetime,repetition,weight):
         self.datetime=datetime
         self.repetition=repetition
         self.weight=weight
    def get_datetime(self):
         return self.datetime
    def get_repetition(self):
         return self.repetition
    def get_weight(self):
         return self.weight

class Constraint:
    def __init__(self,timestamp,organizer):
         self.timestamp=datetime.now()
         self.organizer=organizer
    def get_organizer(self):
         organizer= self.organizer
            
class SpaceConstraint:
    def __init__(self, space):
        self.space = space

    def get_space():
        return self.space
    
class TagConstraint:
    def __init__(self,tag,weight):
        self.tag=tag
        self.weight=weight
    def get_tag():
        return self.tag
    def get_weight():
        return self.weight

