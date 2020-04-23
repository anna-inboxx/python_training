from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_edit_entry_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.find_element_by_link_text("home").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in contact data
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # submit new contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_edit_entry_page()

    def del_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_name("selected[]").click()
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm by pressing ok
        wd.switch_to_alert().accept()

    def fill_contact_form(self,contact):
        wd = self.app.wd
        self.change_field_value("name",contact.name)
        self.change_field_value("middlename",contact.middlename)
        self.change_field_value("lastname",contact.lastname)
        self.change_field_value("homephone",contact.homephone)
        self.change_field_value("email",contact.email)

    def select_first_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self,field_name,text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
         wd = self.app.wd
            # select contact
         self.select_first_contact()
            # click edit
         wd.find_element_by_xpath("//img[@alt='Edit']").click()
            # delete and put new values
         self.fill_contact_form(new_contact_data)
            # click update
         wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
         wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.return_to_edit_entry_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_edit_entry_page()
        list = []
        for element in wd.find_elements_by_css_selector("tr"):
            # получаем текст
            text = element.text
            #получаем идентификатор - внутри элемента span находим другой элемент, кот имеет имя селектед, т.е. чекбокс нах-ся внутри элемента спан, и у этого чекбокса полуаем значение атрибута вэлью
            # ошибка в селектед
            id = element.find_element_by_name("selected[]").get_attribute("value")
            #по этим двум свойствам мы строим объект типа групп и добавить его в список, кот будет возвращаться
            list.append(Contact(name=text, id=id))
        return list







