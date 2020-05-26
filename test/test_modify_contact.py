# -*- coding: utf-8 -*-
from model.contact import Contact
import random


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create_new_contact(Contact(name="Johna", lastname="Smuth"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(lastname="Dalton")
    #запоминаем идентификатор
#    contact.id = old_contacts[index].id
#    app.contact.modify_contact_by_index(index,contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(name="Johna", lastname="Smuth"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




