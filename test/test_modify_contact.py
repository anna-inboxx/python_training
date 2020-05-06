# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Modify",lastname="Smuth"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="Last name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_header(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Modify",lastname="Smuth"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

