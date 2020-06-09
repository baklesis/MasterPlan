from datetime import datetime

class Message:
    def __init__(self, recipient, author, text):
        self._recipient=recipient
        self._author=author
        self._text=text
        self._timestamp=datetime.now()
    @property
    def recipient(self):
        return self._recipient
    @recipient.setter
    def recipient(self,recipient):
        self._recipient=recipient
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        self._author=author
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self,text):
        self._text=text
    def notifyOrganizers(self): #δεν έχει υλοποιηθεί
        return self