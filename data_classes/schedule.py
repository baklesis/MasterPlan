from datetime import datetime

import ui_classes
from data_classes.event import *
from ui_classes.EventListWindow import EventListWindow


class Schedule:
    def __init__(self, event_list, organization):
        self._event_list = event_list
        self._organization = organization
        self._timestamp_created = datetime.now()
        self._published = False

    @property
    def event_list(self):
        return self._event_list

    @event_list.setter
    def event_list(self, event_list):
        self._event_list = event_list

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, organization):
        self._organization = organization

    @property
    def timestamp_created(self):
        return self._timestamp_created

    # δεν εβαλα την get γιατί παίρνει αυτόματα τιμή
    @property
    def published(self):
        return self._published

    @published.setter
    def published(self, published):
        self._published = published

    def addEvent(self, name, duration, repetition):  # event list ειναι list of dictionaries
        newEvent = Event(name, duration)
        self._event_list.append(
            {
                "object": newEvent,
                "datetime": None,
                "repetition": repetition,
                "room": None
            }
        )
        return newEvent

    # coming soon implement test functions for set datetime
    def deleteSchedule(self):  # desctructor καλυτερα
        return self

    def getSchedule(self,building=None, room=None,organizer=None,event=None):
       if building != None:
        building_event_list = []
        for event in self._event_list:
            if event["room"].building.name == building.name:  # αν το event διεξαγεται στο επιλεγμένο κτιριο
                building_event_list.append(event)
        return building_event_list
       if event != None:
        for event in ui_classes.EventListWindow:

    def getEvent(self, name):
        for event in self.event_list:
            if event.name == name:
                return event
        return None



    #def getSchedule(self, event, room, organizer, str):  # special συναρτηση get
    #    return self

    def publishSchedule(self):
        return self

    def createSchedule(self, file):  # μήπως στο initialization func?
        return self

    def convertToCSV(self):
        f = open("schedule.csv", "w")
        for x in range(len()):
            for y in range(len()):
                line = str(x + 1) + ',' + str(id_movies[y]) + ',' + str(ratings[x][y]) + '\n'
                f.write(line)
        f.close()
        return self

    def getEvent(self,name):
        for event in self.event_list:
            if event["object"].name == name:
                return event
        return None