# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    # сохраняем старый список
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test", header="test", footer="test"))
    # создаем новый список
    new_groups = app.group.get_group_list()
    #делаем проверку теста - тест работает если длина нового списка равна старый список +1
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


