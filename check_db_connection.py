import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    contacts = db.get_contacts_in_group(Group(id="203"))
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    pass#db.destroy()




#    l = db.get_contacts_in_group(Group(id="203"))



#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

#try:
 #   cursor = connection.cursor()
  #  cursor.execute("select*from group_list")
   # for row in cursor.fetchall():
    #    print(row)
#finally:
#    connection.close()