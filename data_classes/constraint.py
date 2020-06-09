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

class TimeConstraint(Constraint):
    def __init__(self, organizer, startdatetime, enddatetime, repetition, weight):
        super().__init__(organizer)
        self._start_datetime = startdatetime
        self._end_datetime = enddatetime
        self._repetition = repetition
        self._weight = weight
    @property
    def start_datetime(self):
         return self._start_datetime
    @start_datetime.setter
    def start_datetime(self,start_datetime):
        self._start_datetime=start_datetime
    @property
    def end_datetime(self):
         return self._end_datetime
    @end_datetime.setter
    def end_datetime(self,end_datetime):
        self._end_datetime=end_datetime
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
    def getChanged(self):
        return self

class SpaceConstraint(Constraint):
    def __init__(self, organizer, space):
        super().__init__(organizer)
        self._space = space
    @property
    def space(self):
        return self._space
    @space.setter
    def space(self,space):
        self._space=space

class TagConstraint(Constraint):
    def __init__(self,organizer,tag,weight):
        super().__init__(organizer)
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
    def getChanged(self):
        return self
