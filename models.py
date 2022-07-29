
import psycopg2

DB_HOST = "ec2-99-80-200-225.eu-west-1.compute.amazonaws.com"
DB_NAME = "d8t87nco360qgb"
DB_USER = "tkkjfwcewyiyyy"
DB_PASS = "45ffc56f105bf668e1ecb8e089261e5d827cd1a43b00f069c75cbf2d2101ca99"

req_fields = "id, name, email, password"
table = "users"


class User:

    def __init__(self, id, name, email, rating, password):
        self.user_id = id
        self.email = email
        self.name = name
        self.password = password

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    @staticmethod
    def get(user_id):
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()

        cur.execute("SELECT " + req_fields + " FROM " + table + " WHERE email = '" + user_id + "';")

        user = cur.fetchall()[0]

        conn.commit()
        cur.close()
        conn.close()

        user_id = user[0]
        name = user[1]
        email = user[2]
        password = user[3]
        return User(user_id, name, email, 0, password)

    @staticmethod
    def get_by_email(email):
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor()

        cur.execute("SELECT " + req_fields + " FROM " + table + " WHERE email = '" + email + "';")

        users = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()

        if len(users) == 0:
            return None

        user = users[0]
        user_id = user[0]
        name = user[1]
        email = user[2]
        password = user[3]
        return User(user_id, name, email, 0, password)
