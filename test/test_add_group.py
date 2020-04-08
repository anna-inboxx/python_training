# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
            app.open_home_page()
            app.login(username="admin", password="secret")
            app.open_groups_page()
            app.create_group( Group(name="test", header="test", footer="test"))
            app.return_to_group_page()
            app.logout()


def test_add_empty_group(app):
            app.open_home_page()
            app.login(username="admin", password="secret")
            app.open_groups_page()
            app.create_group(Group(name="", header="", footer=""))
            app.return_to_group_page()
            app.logout()