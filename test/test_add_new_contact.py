# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.create_new_contact( Contact(name="Tom", middlename="John",lastname= "Smith", homephone="89337774448", email="djdjk@dljkk.ru"))
        app.return_to_edit_entry_page()
        app.logout()




