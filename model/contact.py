from sys import maxsize


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
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name is None or other.name is None or self.name == other.name) and self.lastname == other.lastname

    # функция, кот опеределяет как будет выглядеть наш объект при выводе на консоль
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    #пишем правило (ключ для сравнения) если присвоено id, то берем его, если None, то maxsize
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize