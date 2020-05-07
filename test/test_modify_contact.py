# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Modify",lastname="Smuth"))
    contact = Contact(lastname="New lastname")
    # сохраняем старый идентификатор, те присваиваем значение новому параметру
    contact.id = old_contacts[0].id
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    #проводим замену, нового идентификатора на страй
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



