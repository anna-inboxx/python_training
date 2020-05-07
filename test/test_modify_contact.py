# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Johna", lastname="Smuth"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="NEWlastname")
    #запоминаем идентификатор
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



