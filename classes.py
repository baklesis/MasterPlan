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
