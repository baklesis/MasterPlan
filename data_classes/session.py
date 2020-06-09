from datetime import datetime

class Session:
    def __init__(self, current_user,current_org):
        self._current_user = current_user
        self._current_org = current_org
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
    def current_org(self):
        return self._current_org
    @current_org.setter
    def current_org(self, org):
        self._current_org = org
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
        if self._current_user==None:
            return "Guest"
        else:
            return self._current_user.getAccountType()

    def convertToCSV(self): # δεν έχει υλοποιηθεί
        return self

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