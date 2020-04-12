
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

    def del_contact(self):
        wd = self.app.wd
        # select contact by ID
        wd.find_element_by_id("39").click()
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm by pressing ok
        wd.switch_to_alert().accept()

