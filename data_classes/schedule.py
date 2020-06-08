from data_classes.event import *
from datetime import datetime, timedelta, date, time

class Schedule:
    def __init__(self, event_list, organization):
        self.event_list = []
        for event in event_list:
            self.addEvent(event.name, event.duration, event.room_group)
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

    def addEvent(self, name, duration, room_group):  # event list ειναι list of dictionaries
        newEvent = Event(name, duration, room_group)
        self._event_list.append(
            {
                "object": newEvent,
                "datetime": None,
                "repetition": None,
                "room": None
            }
        )
        return newEvent

    # coming soon implement test functions for set datetime
    def deleteSchedule(self):  # destructor καλυτερα
        return self

    def getSchedule(self,building,room,organizer,event):
        if building is not None:
            building_event_list = []
            for event in self._event_list:
                if event["room"].building.name == building.name:  # αν το event διεξαγεται στο επιλεγμένο κτιριο
                    building_event_list.append(event)
            return building_event_list
        if event is not None:
            return 0

    def getEvent(self, name):
        for event in self.event_list:
            if event.name == name:
                return event
        return None

    def publishSchedule(self):
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

    #Scheduling Algorithm
    def executeScheduling(self,room_list):

        new_schedule = Schedule([event['object'] for event in self.event_list], self.organization)  # create a copy of the old schedule with empty scheduled dates and rooms
        weight = {'low': 1 / 3, 'medium': 2 / 3, 'high': 1}  # weight dictionary

        for i,event in enumerate(new_schedule.event_list):

            solution_list = []  # all solutions will go here and they will be sorted to find the best
            available_datetimes= []

            # create scheduling period (generates available datetimes in 30 minute intervals for the next week starting monday)
            today_datetime = datetime.combine(date.today(), time())
            start_datetime = today_datetime + timedelta(days= 7 - today_datetime.weekday())
            end_datetime = start_datetime + timedelta(days=7)
            temp_datetime = start_datetime
            while temp_datetime < end_datetime:
                available_datetimes.append(temp_datetime)
                temp_datetime += timedelta(minutes=30)

            # save constraints
            space_constraint = None
            time_constraints = []
            tag_constraints = []
            for constraint in event["object"].constraint_list:
                if type(constraint).__name__ == 'SpaceConstraint':
                    space_constraint = constraint.space
                if type(constraint).__name__ == 'TimeConstraint':
                    time_constraints.append(constraint)
                if type(constraint).__name__ == 'TagConstraint':
                    tag_constraints.append(constraint)

            # begin algorithm
            available_rooms = room_list.room_list
            if event['object'].room_group is not None:
                available_rooms = event['object'].room_group.room_list
            for possible_datetime in available_datetimes:
                for room in available_rooms:

                    # check if other event is already scheduled in this room at the same time
                    check_next = 0  # flag to continue to next datetime
                    for other_event in new_schedule.event_list:
                        other_room_name = None
                        if other_event['room'] is not None:
                            other_room_name = other_event['room'].name
                        if other_room_name == room.name:  # if the other event is in the same room

                            # create event period
                            event_period = set()  # contains all 30 minute interval datetimes in the event period
                            temp_datetime = possible_datetime
                            while temp_datetime < possible_datetime + timedelta(minutes=event['object'].duration):
                                event_period.add(temp_datetime)
                                temp_datetime += timedelta(minutes=30)

                            # create other event period
                            other_event_period = set() # contains all 30 minute interval datetimes in the other event period
                            temp_datetime = other_event['datetime']
                            while temp_datetime < other_event['datetime'] + timedelta(minutes=other_event['object'].duration):
                                other_event_period.add(temp_datetime)
                                temp_datetime += timedelta(minutes=30)

                            if len(event_period.intersection(other_event_period)) > 0:  # if the other event is scheduled at the same time
                                check_next = 1 # check next possible solution
                                break  # stop checking if other rooms are scheduled in that datetime

                    if check_next: # if another event is scheduled at the same time
                        check_next = 0
                        continue  # check another possible solution

                    # apply space constraint
                    if space_constraint:
                        if space_constraint < room.capacity:
                            score = 3
                        else:
                            score = 3 - (space_constraint - room.capacity) / space_constraint
                    else:
                        score = 3

                    # apply time constraints
                    for time_constraint in time_constraints:

                        # create unwanted period
                        unwanted_period = set()  # contains all 30 minute interval datetimes in the time cosntraint period
                        temp_datetime = time_constraint.start_datetime
                        while temp_datetime < time_constraint.end_datetime:
                            unwanted_period.add(temp_datetime)
                            temp_datetime += timedelta(minutes=30)

                        if len(event_period.intersection(unwanted_period)) > 0:  # if the event is scheduled during the unwanted period
                            score = score - 0.1 * weight[time_constraint.weight]  # apply small penalty for each time constraint broken

                    # apply tag constraints
                    for tag_constraint in tag_constraints:
                        for same_tag_event in tag_constraint.tag.event_list:  # for every event with the same tag as in the tag constraint

                            #create same tag event period
                            same_tag_event_period = set()  # contains all 30 minute interval datetimes in the time cosntraint period
                            temp_datetime = same_tag_event['datetime']
                            while temp_datetime < same_tag_event['datetime'] + timedelta(minutes=same_tag_event['object'].duration):
                                same_tag_event_period.add(temp_datetime)
                                temp_datetime += timedelta(minutes=30)

                            if len(event_period.intersection(other_event_period)) > 0:  # if the same tag event is scheduled at the same time
                                score = score - 0.1 * weight[tag_constraint.weight]  # apply small penalty for each tag constraint broken
                                break

                    solution_list.append([room, possible_datetime, score])
            solution_list.sort(key = lambda x: x[2], reverse = True )
            best_solution = solution_list[0]
            new_schedule.event_list[i]["room"] = best_solution[0]
            new_schedule.event_list[i]["datetime"] = best_solution[1]

        return new_schedule
