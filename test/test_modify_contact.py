# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Tim", middlename="John",lastname= "Smuth", homephone="89337774448", email="djdjk@dljkk.ru"))
        app.contact.modify_first_contact(Contact(name="New name"))

def test_modify_contact_header(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Tim", middlename="John",lastname= "Smuth", homephone="89337774448", email="djdjk@dljkk.ru"))
        app.contact.modify_first_contact(Contact(middlename="New mid"))
