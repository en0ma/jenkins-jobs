import sqlite3

class JobRepository(object):

    def __init__(self):
        self.connect()

    def insert(self, db_data):
        cursor = self.db_conn.cursor()
        cursor.executemany("INSERT into jobs(title, status, checked_at) VALUES(?, ?, ?)", db_data);
        self.disconnect()

    def connect(self):
        db_conn = sqlite3.connect('src/database/jenkins_jobs.db')
        self.db_conn = db_conn
        self.createJobsTable()

    def disconnect(self):
        self.db_conn.close()

    def createJobsTable(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS jobs
                        (id INTEGER PRIMARY KEY, title text, status text, checked_at text)
                      ''')
