# -*- coding: utf-8 -*-
from model.group import Group
import random


#def test_modify_group_name(app, db):
#    if len(db.get_group_list()) == 0:
#        app.group.create(Group(name="testdel", header="test", footer="test"))
#    old_groups = db.get_group_list()
#    index = randrange(len(old_groups))
#    group = Group(name="NEW test_modify")
    # запоминаем индентификатор
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(index,group)
#    new_groups = db.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="testdel", header="test", footer="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


# сравнение в БД и опционно UI

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Testcheck", header="test", footer="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),key=Group.id_or_max)







