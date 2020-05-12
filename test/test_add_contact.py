# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(name="", lastname="")] +[
    Contact(name=random_string("name", 10), lastname=random_string("lastname", 10))
    for i in range(4)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
