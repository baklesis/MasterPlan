from data_classes.account import *
from data_classes.building import *
from data_classes.constraint import *
from data_classes.event import *
from data_classes.room import *
from data_classes.roomGroup import *
from data_classes.schedule import *
from data_classes.session import *
from data_classes.tag import *

#global variables that imitate the existence of a database

#Accounts
account_list = AccountList()
account_list.account_list = [
    Admin('upatras','1','rectorate@upatras.gr'),
    Organizer('makris','1','makri@ceid.upatras.gr', 'Christos Makris', 'upatras'),
    Organizer('alexiou','1','alexiou@ceid.upatras.gr', 'George Alexiou', 'upatras')
]

#Organizers
organizer_list = OrganizerList()
organizer_list.organizer_list = [
    account_list.account_list[1],
    account_list.account_list[2]
]

#Session
session = Session(None,None)

#Buildings
building_list = BuildingList([
    Building("Building B","upatras",[]),
    Building("Building A","upatras",[])
],"upatras")

#Rooms
room_list = RoomList([
    Room("BA",building_list.building_list[0],0,200),
    Room("B4",building_list.building_list[0],0,100),
    Room("B3",building_list.building_list[0],0,50),
    Room("Computer Lab",building_list.building_list[0],1,50),
    Room("AA",building_list.building_list[1],0,200)
],"upatras")

#Room Groups
room_group_list = RoomGroupList("upatras")
room_group_list.addRoomGroup("amphitheater",[room_list.room_list[0],room_list.room_list[1],room_list.room_list[4]])
room_group_list.addRoomGroup("classroom",room_list.room_list[2])
room_group_list.addRoomGroup("lab",room_list.room_list[3])

for room in room_list.room_list:
    for i,building in enumerate(building_list.building_list):
        if room.building.name == building.name:
            building_list.building_list[i].room_list.append(room)


#Schedule

schedule = Schedule([],"upatras")

schedule.addEvent("AI Seminar",120,"None")
schedule.event_list[0]["datetime"]=datetime.now() # test event που συμβαίνει πάντα αυτήν την στιγμή
schedule.event_list[0]["room"]=room_list.room_list[0]
schedule.event_list[0]["object"].organizer=organizer_list.organizer_list[0]
schedule.event_list[0]["object"].room_group = room_group_list.room_group_list[0]

schedule.addEvent("AT91 Workshop",180,"None")
schedule.event_list[1]["datetime"]=datetime(2020,5,12,3,0)
schedule.event_list[1]["room"]=room_list.room_list[0]
schedule.event_list[1]["object"].organizer=organizer_list.organizer_list[1]
schedule.event_list[1]["object"].room_group = room_group_list.room_group_list[1]

schedule.addEvent("Erasmus Presentation",120,"None")
schedule.event_list[2]["datetime"]=datetime(2020,5,15,5,0)
schedule.event_list[2]["room"]=room_list.room_list[0]
schedule.event_list[2]["object"].organizer=organizer_list.organizer_list[1]
schedule.event_list[2]["object"].room_group = room_group_list.room_group_list[0]

schedule.addEvent("IEEE Presentation",120,"None")
schedule.event_list[3]["datetime"]=datetime(2020,5,12,3,0)
schedule.event_list[3]["room"]=room_list.room_list[0]
schedule.event_list[3]["object"].organizer=organizer_list.organizer_list[0]
schedule.event_list[3]["object"].room_group = room_group_list.room_group_list[1]

schedule.addEvent("Robotics Seminar",120,"None")
schedule.event_list[4]["datetime"]=datetime.now() # test event που συμβαίνει πάντα αυτήν την στιγμή
schedule.event_list[4]["room"]=room_list.room_list[1]
schedule.event_list[4]["object"].organizer=organizer_list.organizer_list[1]

schedule.addEvent("Data Mining Seminar",120,"None")
schedule.event_list[5]["datetime"]=datetime(2020,5,10,2,0)
schedule.event_list[5]["room"]=room_list.room_list[1]
schedule.event_list[5]["object"].organizer=organizer_list.organizer_list[0]

schedule.addEvent("Databases Seminar",120,"None")
schedule.event_list[6]["datetime"]=datetime(2020,5,10,4,0)
schedule.event_list[6]["room"]=room_list.room_list[2]
schedule.event_list[6]["object"].organizer=organizer_list.organizer_list[0]

schedule.addEvent("Cyber Security Seminar",120,"None")
schedule.event_list[7]["datetime"]=datetime(2020,5,10,8,0)
schedule.event_list[7]["room"]=room_list.room_list[2]
schedule.event_list[7]["object"].organizer=organizer_list.organizer_list[0]

schedule.addEvent("AI Workshop",120,"None")
schedule.event_list[8]["datetime"]=datetime.now() # test event που συμβαίνει πάντα αυτήν την στιγμή
schedule.event_list[8]["room"]=room_list.room_list[3]
schedule.event_list[8]["object"].organizer=organizer_list.organizer_list[0]

schedule.addEvent("Networks Seminar",180,"None")
schedule.event_list[9]["datetime"]=datetime(2020,5,20,12,0)
schedule.event_list[9]["room"]=room_list.room_list[4]
schedule.event_list[9]["object"].organizer=organizer_list.organizer_list[1]

schedule.addEvent("Architecture Workshop",120,"None")
schedule.event_list[10]["datetime"]=datetime(2020,5,9,3,0)
schedule.event_list[10]["room"]=room_list.room_list[4]
schedule.event_list[10]["object"].organizer=organizer_list.organizer_list[1]

schedule.addEvent("Internship Presentation",120,"None")
schedule.event_list[11]["datetime"]=datetime.now() # test event που συμβαίνει πάντα αυτήν την στιγμή
schedule.event_list[11]["room"]=room_list.room_list[4]
schedule.event_list[11]["object"].organizer=organizer_list.organizer_list[1]


# Tags
tag_list = TagList("upatras")
tag_list.addTag("AI")
tag_list.addTag("Seminar")
tag_list.addTag("Workshop")
tag_list.addTag("Presentation")
schedule.event_list[0]["object"].tag_list.append(tag_list.tag_list[0])
schedule.event_list[0]["object"].tag_list.append(tag_list.tag_list[1])
schedule.event_list[1]["object"].tag_list.append(tag_list.tag_list[2])
schedule.event_list[2]["object"].tag_list.append(tag_list.tag_list[3])
schedule.event_list[3]["object"].tag_list.append(tag_list.tag_list[3])
schedule.event_list[4]["object"].tag_list.append(tag_list.tag_list[1])
schedule.event_list[5]["object"].tag_list.append(tag_list.tag_list[1])
schedule.event_list[6]["object"].tag_list.append(tag_list.tag_list[1])
schedule.event_list[7]["object"].tag_list.append(tag_list.tag_list[1])
schedule.event_list[8]["object"].tag_list.append(tag_list.tag_list[0])
schedule.event_list[8]["object"].tag_list.append(tag_list.tag_list[2])
schedule.event_list[9]["object"].tag_list.append(tag_list.tag_list[1])
schedule.event_list[10]["object"].tag_list.append(tag_list.tag_list[2])
schedule.event_list[11]["object"].tag_list.append(tag_list.tag_list[3])

#Constraints

schedule.event_list[0]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[0], datetime(2020,6,20,15),
                                                              datetime(2020,6,20,18),"none","high"))
schedule.event_list[0]["object"].addConstraint(TagConstraint(organizer_list.organizer_list[0],tag_list.getTag("Seminar"), "medium"))
schedule.event_list[1]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[1], datetime(2020,6,10,16),
                                                              datetime(2020,6,20,17),"none","high"))
#schedule.event_list[2]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[0]))
schedule.event_list[3]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[1], datetime(2020,6,12,8),
                                                              datetime(2020,6,12,9),"none","high"))
schedule.event_list[4]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[1], datetime(2020,6,5,15),
                                                              datetime(2020,6,5,18),"none","high"))
#schedule.event_list[5]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[0]))
#schedule.event_list[6]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[0]))
#schedule.event_list[7]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[0]))
#schedule.event_list[8]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[0]))
#schedule.event_list[8]["object"].addConstraint(TagConstraint(organizer_list.organizer_list[0]))
schedule.event_list[9]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[1], datetime(2020,6,20,15),
                                                              datetime(2020,6,20,18),"none","high"))
#schedule.event_list[10]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[1]))
#schedule.event_list[11]["object"].addConstraint(TimeConstraint(organizer_list.organizer_list[1]))