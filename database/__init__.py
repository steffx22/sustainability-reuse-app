from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2
#import libpq-dev
#database = SQLAlchemy()


def init_table_posts():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
    cur.execute("CREATE TABLE donations (id SERIAL PRIMARY KEY, name VARCHAR, title VARCHAR, category VARCHAR, description VARCHAR, location VARCHAR, reserved VARCHAR);")
    cur.execute("CREATE TABLE requests (id SERIAL PRIMARY KEY, name VARCHAR, description VARCHAR, reserved VARCHAR);")
    conn.commit()
    cur.close()
    conn.close()

# Create database Model

class Postt(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(200), nullable=False)
    date_created = database.Column(database.DateTime, default=datetime.utcnow)

    def repr(self):
        return '<Name %r>' % self.id
