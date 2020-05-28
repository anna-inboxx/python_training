

def test_check_contacts_ui_with_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    for ui in contact_from_home_page:
        for db in contact_from_db:
            if ui.id == db.id:
                assert ui.lastname == db.lastname
                assert ui.address == db.address
                assert ui.all_emails_from_home_page == db.all_emails
                assert ui.all_phones_from_home_page == db.all_phones

#def test_email_on_home_page(app):
#    contact_from_home_page = app.contact.get_contact_list()[0]
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
 #   assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)





