from model.contact import Contact
from random import randrange


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="John",lastname= "Smuth"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.del_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

