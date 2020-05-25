from model.contact import Contact

#загрузить список с главной страницы
#загрузить список с бд
#соответствие записей в бд и ui
#сравнить через ассерт + сортировка

def test_check_contacts_ui_with_db(app,db):
    contact_from_home_page= app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname, name=contact.firstname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
