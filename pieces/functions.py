import sqlite3

class SchoolDatabaseSQLite:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS pupils (
            pupil_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade INTEGER
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_pupil(self, name, age, grade):
        query = 'INSERT INTO pupils (name, age, grade) VALUES (?, ?, ?)'
        self.conn.execute(query, (name, age, grade))
        self.conn.commit()

    def get_pupil(self, pupil_id):
        query = 'SELECT * FROM pupils WHERE pupil_id = ?'
        cursor = self.conn.execute(query, (pupil_id,))
        return cursor.fetchone()

    def update_pupil(self, pupil_id, name=None, age=None, grade=None):
        update_fields = []
        values = []

        if name is not None:
            update_fields.append('name = ?')
            values.append(name)
        if age is not None:
            update_fields.append('age = ?')
            values.append(age)
        if grade is not None:
            update_fields.append('grade = ?')
            values.append(grade)

        if not update_fields:
            return False

        query = 'UPDATE pupils SET ' + ', '.join(update_fields) + ' WHERE pupil_id = ?'
        values.append(pupil_id)

        self.conn.execute(query, tuple(values))
        self.conn.commit()
        return True

    def delete_pupil(self, pupil_id):
        query = 'DELETE FROM pupils WHERE pupil_id = ?'
        self.conn.execute(query, (pupil_id,))
        self.conn.commit()
        return True

    def get_all_pupils(self):
        query = 'SELECT * FROM pupils'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()