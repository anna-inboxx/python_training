from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testdel", header="test", footer="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    #из старого списка удаляем первую группу. Удаляем все элементы с 0 по 1, т.е. только с индексом 0
    old_groups[0:1] = []
    #сравниваем списки
    assert old_groups == new_groups