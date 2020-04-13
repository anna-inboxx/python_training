# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New name"))
    app.session.logout()

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()