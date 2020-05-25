import data_classes as dc #εισαγωγή data classes
import typing #να σκεφτουμε μήπως για δικη μας ευκολια χρειαστεί για runtime support για τυπους δεδομένων παραμέτρων συναρτησεων

class HomePage:
    def enterOrganization(self,org):
        return self
        #dc.AccountList.valOrganization

class ErrorPage:
    def showPage(self):
        return self

class UserPage:
    def showPage(self):
        pass

class GuestPage(UserPage):
    def showPage(self):
        return self
    def logIn(self, username, password):
        acc = dc.AccountList.accountExists(username, password)
        if acc != false:
            type = dc.acc.getAccountType
            if type == "Organizer":
                return self
                # OrganizerPage.showPage()

            elif type == "Admin":
                return self
                # AdminPage.showPage()
        else:
            return self
            # MessageWindow.showWindow("Account not found.")

class LoggedUserPage(UserPage):
    def showPage(self):
        pass

class OrganizerPage(LoggedUserPage):
    def showPage(self):
        return self
        # global session = dc.Session(acc)
        # global building
        # global room

class AdminPage(LoggedUserPage):
    def showPage(self):
        return self
        # session = dc.Session(acc)
        # global building
        # global room

class MainView:
    def showView(self):
        pass
    def openFilterMenu(self):
        return self
    def selectFilter(self,tag):
        return self
    def filter(self):
        return self
    def fillEvents(self,event_list): #abstract γιατι υλοποιείται διαφορετικά σε grid/cal
        pass
    def selectSearch(self):
        return self
    def refreshViews(self): # θα μπορουσε να συγχωνευθει με την fillevents()
        return self
    def publish(self):
        return self
    def reset(self): # resetSchedule καλυτερα?
        return self

class GridView(MainView):
    def showView(self):
        return self
    def selectRoom(self,room):
        return self
    def fillEvents(self,event_list): # new
        return self
    def returnToBuildings(self):
        return self

class CalendarView(MainView):
    def showView(self):
        return self
    def selectEvent(self,event):
        return self
    def showView(self):
        return self
    def fillEvents(self,event_list):  # new
        return self

class SearchWindow:
    def showWindow(self):
        return self
    def enter(self):
        return self
    def selectSuggestion(self):
        return self
    def search(self):
        return self
    def show(self,message):
        return self
    def autocomplete(self):
        return self
    def sort(self):
        return self
    def selectResult(self):
        return self

class RangeWindow:
    def showWindow(self):
        return self
    def selectRange(self,start,end):
        return self

class InitWindow:
    def showWindow(self):
        return self
    def checkForFiles(self): #checkExistFiles()?
        return self
    def importFile(file):
        return self
    def validateFiles(self):
        return self
    def save(self): #saveFiles()?
        return self

class EventInfoWindow:
    def showWindow(self):
        return self

class EventListWindow:
    def showWindow(self):
        return self
    def selectEvent(self):
        return self
    def selectFilter(self):
        return self
    def filter(self):
        return self
    def selectSorting(self):
        return self
    def sort(type,order):
        return self

class EventEditWindow:
    def showWindow(self):
        return self
    def addTag(self):
        return self
    def createTag(self):
        return self
    def saveSpaceConstraint(self,space):
        return self
    def checkSpaceConstraint(self):
        return self
    def cancelSpaceConstraint(self):
        return self
    def addTagConstraint(self):
        return self
    def selectConstraint(self):
        return self
    def decrease(self):
        return self
    def reset(self):
        return self
    def showField(self):
        return self

class EventCreateWindow:
    def showWindow(self):
        # gets room group list
        # shows all elements
    def setTags(self): #καλύτερα μετονομασία σε addTag, λόγω λειτουργικότητας
    def selectOrganizer(self): #ζήτημα, χρειάζεται αλλαγή ροής
    def saveEvent(self):
        # checks if all complete
        # gets Name
        # gets Duration
        # gets selected Room Group
        # gets Tag list
        # creates new event with selected attributes
        # creates tags if needed (discussion needed)
        # if not complete shows message

class OrganizerCreateWindow:
    def showWindow(self):
        return self
    def fillIn(self): #μαλλον αχρηστο
        return self
    def save(self):
        return self
    def cancel(self):
        return self

class OrganizerListWindow:
    def selectOrganizer(self,org):
        return self

class ConstraintWindow:
    def showWindow(self):
        return self
    def selectTag(self,tag):
        return self
    def selectTime(self,datetime):
        return self
    def selectRepetition(self,rep):
        return self
    def selectWeight(self,weight):
        return self
    def saveTagConstraint(self):
        return self
    def saveTimeConstraint(self):
        return self
    def checkData(self):
        return self

class MessageWindow:
    def showWindow(self,message):
        return self
    def validate(self,choice):
        return self
    def createFile(self):
        return self
    def executeScheduling(self):
        return self
    def checkFields(self):
        return self
