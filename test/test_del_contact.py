from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="John",lastname= "Smuth"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

