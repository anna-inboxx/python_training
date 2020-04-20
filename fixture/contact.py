
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_edit_entry_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

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






