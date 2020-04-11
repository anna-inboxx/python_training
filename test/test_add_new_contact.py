# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.contact.create_new_contact( Contact(name="Tom", middlename="John",lastname= "Smith", homephone="89337774448", email="djdjk@dljkk.ru"))
        app.contact.return_to_edit_entry_page()
        app.session.logout()




