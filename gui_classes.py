import data_classes as dc #εισαγωγή data classes
import typing #να σκεφτουμε μήπως για δικη μας ευκολια χρειαστεί για runtime support για τυπους δεδομένων παραμέτρων συναρτησεων

class HomePage:
    def enterOrganization(self,org):

class ErrorPage:
    def showPage(self):

class UserPage:
    def showPage(self):
        pass

class GuestPage(UserPage):
    def showPage(self):
    def logIn(self,user,pass):


class LoggedUserPage(UserPage):
    def showPage(self):
        pass

class OrganizerPage(LoggedUserPage):
    def showPage(self):

class AdminPage(LoggedUserPage):
    def showPage(self):

class MainView:
    def showView(self):
        pass
    def openFilterMenu(self):
    def selectFilter(self,tag):
    def filter(self):
    def fillEvents(self): #abstract γιατι υλοποιείται διαφορετικά σε grid/cal
        pass
    def selectSearch(self):
    def refreshViews(self): # θα μπορουσε να συγχωνευθει με την fillevents()
    def publish(self):
    def reset(self): # resetSchedule καλυτερα?

class GridView(MainView):
    def showView(self):
    def selectRoom(self,room):
    def fillEvents(self,event_list): # new
    def returnToBuildings(self):

class CalendarView(MainView):
    def showView(self):
    def selectEvent(self,event):
    def showView(self):
    def fillEvents(self,event_list):  # new

class SearchWindow:
    def showWindow(self):
    def enter(self):
    def selectSuggestion(self):
    def search(self):
    def show(self,message):
    def autocomplete(self):
    def sort(self):
    def selectResult(self):

class RangeWindow:
    def showWindow(self):
    def selectRange(self,start,end):

class InitWindow:
    def showWindow(self):
    def checkForFiles(self): #checkExistFiles()?
    def importFile(file):
    def validateFiles(self):
    def save(self): #saveFiles()?

class EventInfoWindow:
    def showWindow(self):

class EventListWindow:
    def showWindow(self):
    def selectEvent(self):
    def selectFilter(self):
    def filter(self):
    def selectSorting(self):
    def sort(type,order):

class EventEditWindow:
    def showWindow(self):
    def addTag(self):
    def createTag(self):
    def saveSpaceConstraint(self,space):
    def checkSpaceConstraint(self):
    def cancelSpaceConstraint(self):
    def addTagConstraint(self):
    def selectConstraint(self):
    def decrease(self): #decreaseWeight()?
    def reset(self): # τι ειναι αυτο?
    def showField(self): # τι ειναι αυτο?

class EventCreateWindow:
    def showWindow(self):
    def selectName(self):
    def selectDuration(self):
    def setTags(self):
    def addTag(self):
    def showRoomGroups(self):
    def selectGroup(self):
    def selectOrganizer(self):
    def saveEvent(self):

class OrganizerCreateWindow:
    def showWindow(self):
    def fillIn(self): #μαλλον αχρηστο
    def save(self):
    def cancel(self):

class OrganizerListWindow:
    def selectOrganizer(self,org):

class ConstraintWindow:
    def showWindow(self):        
    def selectTag(self,tag):
    def selectTime(self,datetime):
    def selectRepetition(self,rep):
    def selectWeight(self,weight):
    def saveTagConstraint(self):
    def saveTimeConstraint(self):
    def checkData(self):

class MessageWindow:
    def showWindow(self,message):
    def validate(self,choice):
    def createFile(self):
    def executeScheduling(self):
    def checkfields(self):

class SearchWindow()
    def showWindow(self):
    def enter(self):
    def selectSuggestion(self):
    def search(self,):
    def show(self):
    def autocomplete(self):
    def sort(self):
    def selectResult(self)    
