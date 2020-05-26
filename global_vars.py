from data_classes import *

#global variables that imitate the existence of a database

account_list = AccountList([])
account_list.account_list.append(Admin('upatras','1','rectorate@upatras.gr'))
account_list.account_list.append(Organizer('makris','1','makri@ceid.upatras.gr', 'Christos Makris', 'upatras'))

session = None

building_list = None
room_list = None
schedule = None