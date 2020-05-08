from datetime import datetime

class Account:
    def __init__(username,password,email):
        self._username=username
        self._password=password
        self._email=email
    
    def get_username():
        return self._username
    def set_username(username):
        self._username=username
    def get_password():
        return self._password
    def set_password(password):
        self._password=password
    def get_email():
        return self._email
    def set_email(email):
        self._email=email
        

class Organizer(Account):
    def __init__(fullname, organization):
        self._fullname=fullname
        self._organization=organization
    
    def get_fullname():
        return self._fullname
    def set_fullname(fullname):
        self._fullname=fullname
    def get_organization():
        return self._organization
    def set_organization(organization):
        self._organization=organization

class Admin(Account):
    pass

class Message:
    def __init__(recipient,author,text):
        self._recipient=recipient
        self._author=author
        self._text=text
        self._timestamp=datetime.now()

    def get_recipient():
        return self._recipient
    def set_recipient(recipient):
        self._recipient=recipient
    def get_author():
        return self._author
    def set_author(author):
        self._author=author
    def get_text():
        return self._text
    def set_text(text):
        self._text=text

        
class OrganizerList:
    def __init__(organizer_list):
        self._organizer_list=organizer_list

    def get_organizer_list():
        return self._organizer_list
    def set_organizer_list(organizer_list):
        self._organizer_list=organizer_list

## Thanos start
class Schedule:
    def __init__(event_list):
        self.__event_list=event_list
        self.__timestamp_created=datetime.now()
        self.__published=False

    def get_event_list():
        return self.__event_list
    def get_timestamp():
        return self.__timestamp_created
    def get_published():
        return self.__published
    def publish():
        self.__published=True
    def unpublish():
        self.__published=False

class Event:
    def __init__(name,duration):
        self.__name=name
        self.__duration=duration
        self.__organizer=None
        self.__tag_list= []
        self.__constraint_list= []
        self.__timestamp_created=datetime.now()

    def get_name():
        return self.__name
    def get_duration():
        return self.__duration
    def get_organizer():
        return self.__organizer
    def set_organizer(organizer):
        self.__organizer=organizer
    def add_tag(tag):
        self.__tag_list.append(tag)
        tag.add_event(self)
    def remove_tag(tag):
        self.__tag_list.remove(tag)
        tag.remove_event(self)
    def add_constraint(constraint):
        self.__constraint_list.append(constraint)
    def remove_constraint(constraint):
        self.__constraint_list.remove(constraint)
    def get_timestamp():
        return self.__timestamp_created


class Tag:
    def __init__(name):
        self.__name=name
        self.__event_list= []

    def get_name():
        return self.__name
    def get_event_list():
        return self.__event_list
    def add_event(event):
        self.__event_list.append(event)
    def remove_event(event):
        self.__event_list.remove(event)
## Thanos end
