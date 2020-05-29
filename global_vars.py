from data_classes import *

#global variables that imitate the existence of a database

account_list = AccountList([])
account_list.account_list.append(Admin('upatras','1','rectorate@upatras.gr'))
account_list.account_list.append(Organizer('makris','1','makri@ceid.upatras.gr', 'Christos Makris', 'upatras'))

session = None

room_list = RoomList([Room("BA","Building A",0,200,"amphitheater"),Room("B4","Building A",0,100,"amphitheater"),Room("B3","Building A",0,50,"classroom")])

building_list = BuildingList([Building("Building A","upatras",[[]])])
building_list.building_list[0].room_list[0]=room_list

schedule = Schedule([])
schedule.addEvent(Event("AI Seminar",2),datetime(2020,5,20,5,0),"no","BA")
schedule.addEvent(Event("AT91 Workshop",2),datetime(2020,5,12,3,0),"no","BA")
schedule.addEvent(Event("Erasmus Presentation",2),datetime(2020,5,15,5,0),"no","BA")
schedule.addEvent(Event("IEEE Presentation",2),datetime(2020,5,15,7,0),"no","BA")
schedule.addEvent(Event("Robotics Seminar",2),datetime(2020,5,10,12,0),"no","BA")
schedule.addEvent(Event("Data Mining Seminar",2),datetime(2020,5,10,2,0),"no","BA")
schedule.addEvent(Event("Databases Seminar",2),datetime(2020,5,10,4,0),"no","B4")
schedule.addEvent(Event("Cyber Security Seminar",2),datetime(2020,5,10,8,0),"no","B4")

tag_AI = Tag("AI")
tag_Seminar = Tag("Seminar")
tag_list = TagList()
tag_list.tag_list.extend([tag_AI,tag_Seminar])
schedule.event_list[0]["object"].tag_list.append(tag_AI)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)
schedule.event_list[0]["object"].tag_list.append(tag_Seminar)


