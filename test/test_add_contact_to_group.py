from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
from random import randrange


def test_add_contact_to_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    #Проверяем наличие групп и контактов (что в приложении есть хотя бы одна группа и один контакт).
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name="For adding contact"))
        group_list = db.get_group_list()

    group = group_list[randrange(len(group_list))]

    #проверить, что существуют контакты, которые можно добавить в группу (и предварительно создавать новый контакт или группу, если все контакты добавлены во все группы).
    contact_list = db.get_contacts_not_in_group(group)
    if len(contact_list) == 0:
        app.contact.create_new_contact(Contact(name="Add to group", lastname="Smuth"))
        contact_list = db.get_contacts_not_in_group(group)

    #Для всех тестов надо вместо первой попавшейся группы и контакта выбирать именно такой контакт, который можно добавить в группу или удалить из группы.
    contact = contact_list[randrange(len(contact_list))]
    old_contacts_in_group = db.get_contacts_in_group(group)

    app.contact.add_contact_to_group_by_id(contact.id, group.id)

    old_contacts_in_group.append(contact)
    #Сравнивать надо изменившиеся списки групп контакта (который добавляем или удаляем из группы), или списки контактов, состоящих в той группе, которую добавляли или удаляли контакт.
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)







