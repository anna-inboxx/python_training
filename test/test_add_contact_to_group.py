from model.group import Group
from fixture.orm import ORMFixture


#добавляем контакт в группу
# На главной странице выбираем контакт (выбираем первый контакт или случайный)
#через интерфейс добавляем его в определенную группу (след нужно передать параметр групп?
#вызываем метод get contact in group указываем номер группы
# отлифльтровать список на главной странице по названию группы, открыть список в бд ерез assert  проверям, что совпадает

#или просто вызывам метод и выводим на экран спислк контактов в группе и смотрим

def test_add_contact_to_group(app, db):
    app.contact.add_contact_to_group()
    list_group_ui = app.contact.choose_group_from_main_page()
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    l = db.get_contacts_in_group(Group(id="203"))
    for item in l:
        print(item)



