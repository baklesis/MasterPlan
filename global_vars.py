from data_classes import *

# global variables that imitate the existence of a database

account_list = AccountList([])
account_list.account_list.append(Admin('upatras','1','rectorate@upatras.gr'))
account_list.account_list.append(Organizer('makris','1','makri@ceid.upatras.gr', 'Christos Makris', 'upatras'))

session = None

room_list = RoomList([Room("BA","Building A",0,200,"amphitheater"),Room("B4","Building A",0,100,"amphitheater"),Room("B3","Building A",0,50,"classroom")],"upatras")

building_list = BuildingList([Building("Building A","upatras",[[]])])
building_list.building_list[0].room_list[0]=room_list

schedule = Schedule([])
schedule.addEvent("AI Seminar",60,"no")
schedule.addEvent("AT91 Workshop",80,"no")
schedule.addEvent("Erasmus Presentation",60,"no")
schedule.addEvent("IEEE Presentation",30,"no")
schedule.addEvent("Robotics Seminar",120,"no")
schedule.addEvent("Data Mining Seminar",120,"no")
schedule.addEvent("Databases Seminar",120,"no")
schedule.addEvent("Cyber Security Seminar",90,"no")

tag_AI = Tag("AI")
tag_Seminar = Tag("Seminar")
tag_list = TagList("upatras")
tag_list.tag_list.extend([tag_AI,tag_Seminar])
schedule.event_list[0]["object"].tag_list.append(tag_AI)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)


