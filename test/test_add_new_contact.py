# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
        app.contact.create_new_contact( Contact(name="Tim", middlename="John",lastname= "Smuth", homephone="89337774448", email="djdjk@dljkk.ru"))
        app.contact.return_to_edit_entry_page()



