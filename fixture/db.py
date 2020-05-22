import pymysql.cursors


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

    def destroy(self):
        self.connection.close()

