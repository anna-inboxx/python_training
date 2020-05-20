from model.contact import Contact
import random
import string

constant = [
    Contact(name="name2020", lastname="lastname2020"),
    Contact(name="name2019", lastname="lastname2019")
]


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(name="", lastname="")] +[
    Contact(name=random_string("name", 10), lastname=random_string("lastname", 10))
    for i in range(2)
    ]
