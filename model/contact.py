from sys import maxsize


class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, address=None, homephone=None, mobilephone=None, secondaryphone=None, workphone=None, email=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name is None or other.name is None or self.name == other.name) and self.lastname == other.lastname

    # функция, кот опеределяет как будет выглядеть наш объект при выводе на консоль
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    #пишем правило (ключ для сравнения) если присвоено id, то берем его, если None, то maxsize
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize