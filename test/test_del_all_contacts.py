
def test_del_all_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_all_contacts()
    app.session.logout()