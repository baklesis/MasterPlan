from datetime import datetime

class Constraint:
    def __init__(self,organizer):
        self.__organizer = organizer
        self.__timestamp=datetime.now()
    @property
    def organizer(self):
         return self.__organizer
    @organizer.setter
    def organizer(self,organizer):
        self.__organizer=organizer

class TimeConstraint:
    def __init__(self,eventdatetime,repetition,weight):
         self._datetime=eventdatetime
         self._repetition=repetition
         self._weight=weight
    @property
    def datetime(self):
         return self._datetime
    @datetime.setter
    def datetime(self,eventdatetime):
        self._datetime=eventdatetime
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
