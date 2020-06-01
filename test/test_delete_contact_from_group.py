from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
from random import randrange


def test_delete_contact_from_group(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    #Проверяем наличие групп и контактов (что в приложении есть хотя бы одна группа и один контакт)
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name="For adding contact"))
        group_list = db.get_group_list()

    group = group_list[randrange(len(group_list))]

    # Проверяем, что существуют контакты, которые можно удалить из группы (и предварительно создавать новый контакт или группу, если все контакты добавлены во все группы).
    contact_in_group = db.get_contacts_in_group(group)
    if len(contact_in_group) == 0:
        contacts_not_in_group = db.get_contacts_not_in_group(group)
        if len(contacts_not_in_group) == 0:
            app.contact.create(Contact(name="TEST123456789"))
            contacts_not_in_group = db.get_contacts_not_in_group(group)
        contact_added = contacts_not_in_group[randrange(len(contacts_not_in_group))]
        app.contact.add_contact_to_group(contact_added.id, group.id)
        contact_in_group = db.get_contacts_in_group(group)

    contact = contact_in_group[randrange(len(contact_in_group))]
    old_contacts_in_group = db.get_contacts_in_group(group)

    app.contact.remove_contact_from_group(contact.id, group.id)

    #Сравниваем изменившиеся списки групп контакта (который добавляем или удаляем из группы), или списки контактов, состоящих в той группе, которую добавляли или удаляли контакт.
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)

