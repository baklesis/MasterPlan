import secrets
import string

class Account:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

    def getAccountType(self):
        return type(self).__name__


class AccountList:
    def __init__(self):
        self._account_list = None

    @property
    def account_list(self):
        return self._account_list

    @account_list.setter
    def account_list(self,account_list):
        self._account_list = account_list

    def addAccount(self, username, password, email):
        self._account_list.append(Account(username, password, email))

    def valOrganization(self, org):
        for acc in self.account_list:
            if (acc.getAccountType() == 'Admin') & (acc.username == org):
                return True
        return False

    def accountExists(self, username, password):
        for acc in self.account_list:
            if (acc.username == username) & (acc.password == password):
                return acc
        return False


class Admin(Account):
    pass


class Organizer(Account):
    def __init__(self, username, password, email, fullname, organization):
        super().__init__(username, password, email)
        self._fullname = fullname
        self._organization = organization

    @property
    def fullname(self):
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        self._fullname = fullname

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, organization):
        self._organization = organization

    def sendEmail(self): #δεν έχει υλοποιηθεί
        return self


class OrganizerList:
    def __init__(self):
        self._organizer_list = None

    @property
    def organizer_list(self):
        return self._organizer_list

    @organizer_list.setter
    def organizer_list(self, organizer_list):
        self._organizer_list = organizer_list

    def getOrganizer(self, fullname):
        for organizer in self.organizer_list:
            if organizer.fullname == fullname:
                return organizer
        return None

    def addOrganizer(self, accountlist, organization, name, email):
        # generates temporary username
        generated_username = name.lower().replace(" ", "")
        while next((x for x in accountlist.account_list if x.username == generated_username), None) is not None:
            # if already in the account list it appends an ascending number at the end
            try:
                generated_username = generated_username[:-1] + str(int(generated_username[-1]) + 1)
            except:
                generated_username = generated_username + "1"
        # generates temporary password
        alphabet = string.ascii_lowercase + string.digits
        generated_password = "".join(secrets.choice(alphabet) for i in range(8))
        # creates a new Organizer
        newOrganizer = Organizer(generated_username, generated_password, email, name, organization)
        # adds it to the Organizer List
        self.organizer_list.append(newOrganizer)
        # adds it to the account list
        accountlist.account_list.append(newOrganizer)
        print("Account created with username: " + generated_username + " and password: " + generated_password)
