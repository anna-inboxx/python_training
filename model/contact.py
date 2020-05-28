from sys import maxsize
import re


class Contact:

    def __init__(self, name=None, firstname=None, middlename=None, lastname=None, address=None, id=None,
                 email=None, email2=None, email3=None,all_emails_from_home_page=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None):
        self.name = name
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones = self.merge_phones_like_on_home_page()
        self.all_emails = self.merge_emails_like_on_home_page()
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.lastname == other.lastname

    # функция, кот опеределяет как будет выглядеть наш объект при выводе на консоль
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    #пишем правило (ключ для сравнения) если присвоено id, то берем его, если None, то maxsize
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_emails_like_on_home_page(self):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [self.email, self.email2, self.email3])))

    def merge_phones_like_on_home_page(self):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [self.homephone, self.mobilephone, self.workphone,
                                            self.secondaryphone]))))


