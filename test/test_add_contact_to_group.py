from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random


#добавляем контакт в группу
# На главной странице выбираем контакт (выбираем первый контакт или случайный)
#через интерфейс добавляем его в определенную группу (след нужно передать параметр групп?
#вызываем метод get contact in group указываем номер группы
# отлифльтровать список на главной странице по названию группы, открыть список в бд ерез assert  проверям, что совпадает

#или просто вызывам метод и выводим на экран спислк контактов в группе и смотрим

#def test_add_contact_to_group(app, db):
#    app.contact.add_contact_to_group()
#    list_group_ui = app.contact.choose_group_from_main_page()
#    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#    l = db.get_contacts_in_group(Group(id="203"))
#    for item in l:
#        print(item)


#добавляем новый контакт, добавлякм контакт в опр группу (id 226), затем сравниваем количество по БД общее количество контактов с контактами в группе и вне ее

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(name="John", lastname="Smuth"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group_by_id(contact.id)
    assert len(old_contacts) == len(db.get_contacts_in_group(Group(id="226"))) + len(db.get_contacts_not_in_group(Group(id="226")))


def test_delete_contact_from_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(name="John", lastname="Smuth"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_group(contact.id)
    assert len(old_contacts) == len(db.get_contacts_in_group(Group(id="226"))) + len(db.get_contacts_not_in_group(Group(id="226")))



