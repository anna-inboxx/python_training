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
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # submit new contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_edit_entry_page()
        self.contact_cache = None

    def del_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self,index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm by pressing ok
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def select_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        self.select_contact_by_index(0)

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

    def modify_first_contact(self):
        self.modify_contact_by_index(0)
        self.contact_cache = None

    def modify_contact_by_index(self,index, new_contact_data):
         wd = self.app.wd
         self.select_contact_by_index(index)
         wd.find_element_by_xpath("//img[@alt='Edit']").click()
            # delete and put new values
         self.fill_contact_form(new_contact_data)
            # click update
         wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
         wd.find_element_by_link_text("home page").click()
         self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_edit_entry_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_edit_entry_page()
            rows = wd.find_elements_by_name("entry")
            self.contact_cache = []
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                name = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, name=name, id=id))
        return list(self.contact_cache)



