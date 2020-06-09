from datetime import datetime
class Event:
    def __init__(self, name, duration, room_group):
        self._name = name
        self._duration = duration
        self._organizer = None
        self._room_group = room_group
        self._tag_list = []
        self._constraint_list = []
        self._timestamp_created = datetime.now()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

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
    def constraint_list(self, constraint):
        self._constraint_list.append(constraint)

    @property
    def timestamp_created(self):
        return self._timestamp_created

    @property
    def room_group(self):
        return self._room_group

    @room_group.setter
    def room_group(self, room_group):
        self._room_group = room_group

    def addTag(self, name, tag_list):
        for i in self.tag_list:
            if i.name == name:
                return self
        tag = tag_list.addTag(name)
        self._tag_list.append(tag)
        return self

    def removeTag(self, name, tag_list, schedule):
        found=False
        for tag in self.tag_list:
            if tag.name == name:
                found=True
                break
        if found:
            self.tag_list.remove(tag)
            tag_list.removeTag(name, schedule)

    def addConstraint(self, constraint):
        if type(constraint).__name__ == "SpaceConstraint":
            for const in self.constraint_list:
                if type(const).__name__ == "SpaceConstraint":
                    self.constraint_list.remove(const)
        self.constraint_list.append(constraint)
        return self

