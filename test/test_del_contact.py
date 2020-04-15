from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(name="Tim", middlename="John",lastname= "Smuth", homephone="89337774448", email="djdjk@dljkk.ru"))
    app.contact.del_contact()

