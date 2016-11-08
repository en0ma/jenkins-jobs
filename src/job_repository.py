import sqlite3

class JobRepository(object):

    def __init__(self):
        self.db_conn = self.connect()

    def insert(self, db_data):
        cursor = self.db_conn.cursor()
        cursor.executemany(db_data);
        self.disconnect()

    def connect(self):
        db_conn = sqlite3.connect('database/jenkins_jobs.db')
        return db_conn

    def disconnect(self):
        self.db_conn.close()
