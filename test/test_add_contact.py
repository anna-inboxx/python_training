# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(Contact(name="Tim", middlename="John",lastname= "Smuth"))
    new_contacts = app.contact.get_contact_list()
    #проверка в тесте
    assert len(old_contacts) + 1 == len(new_contacts)