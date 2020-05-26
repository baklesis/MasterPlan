from gui_classes import *
from datetime import datetime

class AccountList:
    def __init__(self, account_list):
        self._account_list = account_list
    @property
    def account_list(self):
        return self._account_list
    @account_list.setter
    def account_list(self,account):
        self._account_list.append(account)
    def valOrganization(self,org):
        for acc in self.account_list:
            if (acc.getAccountType() == 'Admin') & (acc.username == org):
                return True
        return False
    def accountExists(self,username,password):
        for acc in self.account_list:
            if (acc.username==username) & (acc.password==password):
                return acc
        return False

class Account:
    def __init__(self, username, password, email):
        self._username=username
        self._password=password
        self._email=email
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        self._username=username
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        self._password=password
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email=email
    def getAccountType(self):
        return type(self).__name__

class Organizer(Account):
    def __init__(self, username, password, email, fullname, organization):
        super().__init__(username, password, email)
        self._fullname=fullname
        self._organization=organization
    @property
    def fullname(self):
        return self._fullname
    @fullname.setter
    def fullname(self,fullname):
        self._fullname=fullname
    @property
    def organization(self):
        return self._organization
    @organization.setter
    def organization(self,organization):
        self._organization=organization
    #def getName(): αντικαθηστατε από την username() που κληρονομεί απο την account
    def sendEmail(self):
        pass

class Admin(Account):
    pass

class Announcement:
    def __init__(self, text):
        self._text = text
        self._timestamp = datetime.now()
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, text):
        self._text = text

class Message:
    def __init__(self, recipient, author, text):
        self._recipient=recipient
        self._author=author
        self._text=text
        self._timestamp=datetime.now()
    @property
    def recipient(self):
        return self._recipient
    @recipient.setter
    def recipient(self,recipient):
        self._recipient=recipient
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        self._author=author
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self,text):
        self._text=text
    #def notifyOrganizers(self): καλύτερα να καλείται ο constructor που θα φτιαχνει μηνύματα προς καθε organizer

class OrganizerList:
    def __init__(self, organizer_list):
        self._organizer_list=organizer_list
    @property
    def organizer_list(self):
        return self._organizer_list
    @organizer_list.setter
    def organizer_list(self,organizer_list):
        self._organizer_list=organizer_list
    def addOrganizer(self):
        pass

class Session:
    def __init__(self, current_user):
        self._current_user = current_user
        self._selected_building = None
        self._selected_floor = 0
        self._selected_filters = []
    @property
    def current_user(self):
        return self._current_user
    @current_user.setter
    def current_user(self,user):
        self._current_user=user
    @property
    def selected_filters(self):
        return self._selected_filters
    @selected_filters.setter
    def selected_filters(self,filter):
        self._selected_filters.append(filter)
    @property
    def selected_building(self):
        return self._selected_building
    @selected_building.setter
    def selected_building(self,building):
        self._selected_building=building
    @property
    def selected_floor(self):
        return self._selected_floor
    @selected_floor.setter
    def selected_floor(self,floor):
        self._selected_floor=floor
    def getUserType(self):
        return self
    def convertToCSV(self):
        return self

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
    def __init__(self,building_list):
        self._building_list= building_list
    @property    
    def building_list(self):
        return self._building_list
    @building_list.setter
    def building_list(self,building):
        self._building_list.append(building)
    def createBuildingList(self,file):
        return self
    def convertToCSV(self):
        return self

class Room:
    def __init__(self, name, building, floor, capacity, group):
        self._name = name
        self._building = building
        self._floor = floor
        self._capacity = capacity
        self._group = group
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
    @property
    def group(self):
        return self._group
    @group.setter
    def group(self, group):
        self._group = group
    def getRoomInfo(self):
        return self

class RoomList:
    def __init__(self, room_list):
        self.room_list = room_list
    @property    
    def room_list(self):
        return self._room_list
    @room_list.setter
    def room_list(self,room):
        self._room_list.append(room)
    def createRoomList(self,file):
        return self
    def convertToCSV(self):
        return self

class Schedule:
    def __init__(self,event_list):
        self._event_list=event_list
        self._timestamp_created=datetime.now()
        self._published=False
    @property
    def event_list(self):
        return self._event_list
    @event_list.setter
    def event_list(self,event,datetime,repetition,room): #event list ειναι list of dictionaries
        self._event_list.append(
            {
            "event" : event,
            "datetime" : datetime,
            "repetition" : repetition,
            "room" : room
            }
        )
    @property
    def timestamp_created(self):
        return self._timestamp_created
    # δεν εβαλα την get γιατί παίρνει αυτόματα τιμή
    @property
    def published(self):
        return self._published
    @published.setter
    def published(self,published):
        self._published=published
    def deleteSchedule(self): #desctructor καλυτερα
        return self
    def getSchedule(self,event,room,organizer,str): #να δουμε πως θα μπορουσαμε το κάνουμε μέσω του constructor
        return self
    def publishSchedule(self):
        return self
    def createSchedule(self,file): #μήπως στο initialization?
        return self
    def convertToCSV(self):
        return self
        

class Event:
    def __init__(self,name,duration):
        self._name=name
        self._duration=duration
        self._organizer=None
        self._tag_list= []
        self._constraint_list= []
        self._timestamp_created=datetime.now()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    @property
    def organizer(self):
        return self._organizer
    @organizer.setter
    def organizer(self, organizer):
        self._organizer = organizer
    @property
    def tag_list(self):
        return self._tag_list
    @tag_list.setter
    def tag_list(self, tag_list):
        self._tag_list = tag_list
    @property
    def constraint_list(self):
        return self._constraint_list
    @constraint_list.setter
    def constraint_list(self,constraint):
        self._constraint_list.append(constraint)
    @property
    def timestamp_created(self):
        return self._timestamp_created
    def getEventInfo(self):
        return self
    #def addTag(self):  μπορεί να αντικατασταθεί από την tag_list.setter
    #def addConstraint(self): # μπορεί να αντικατασταθεί από την constraint_list.setter

class Tag:
    def __init__(self,name):
        self._name=name
        self._event_list= []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    @property
    def event_list(self):
        return self._event_list
    @event_list.setter
    def event_list(self, event):
        self._event_list.append(event)

class TagList:
    def __init__(self):
        self._tag_list = []
    @property
    def tag_list(self):
        return self._tag_list
    def addTag(self, name):
        self._tag_list.append(Tag(name))

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
    def __init__(self, room_group_list):
        self._room_group_list = room_group_list
    @property
    def room_group_list(self):
        return self._room_group_list
    def addRoomGroup(self,name,event_list,room_list):
        self._room_group_list.append(RoomGroup(name,event_list,room_list))

class Constraint:
    def __init__(self,organizer):
        self._organizer = organizer
        self._timestamp=datetime.now()
    @property
    def organizer(self):
         return self._organizer
    @organizer.setter
    def organizer(self,organizer):
        self._organizer=organizer

class TimeConstraint:
    def __init__(self,datetime,repetition,weight):
         self._datetime=datetime
         self._repetition=repetition
         self._weight=weight
    @property
    def datetime(self):
         return self._datetime
    @datetime.setter
    def datetime(self):
        self._datetime=datetime
    @property
    def repetition(self):
         return self._repetition
    @repetition.setter
    def repetition(self,repetition):
        self._repetition=repetition
    @property
    def weight(self):
         return self._weight
    @weight.setter
    def weight(self,weight):
        self._weight=weight
    def getConstraintInfo(self):
        return self
    def getChanged(self):
        return self

class SpaceConstraint:
    def __init__(self, space):
        self._space = space
    @property
    def space(self):
        return self._space
    @space.setter
    def space(self,space):
        self._space=space
    def getConstraintInfo(self):
        return self

class TagConstraint:
    def __init__(self,tag,weight):
        self._tag=tag
        self._weight=weight
    @property
    def tag(self):
        return self._tag
    @tag.setter
    def tag(self,tag):
        self._tag=tag
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self,weight):
        self._weight=weight
    def getConstraintInfo(self):
        return self
    def getChanged(self):
        return self
