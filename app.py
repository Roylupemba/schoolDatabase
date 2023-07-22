from flask import Flask, render_template, request

from functions import SchoolDatabaseSQLite

app = Flask(__name__)


@app.route('/')
def index():
    school_db = SchoolDatabaseSQLite("school.db")
    pupils = school_db.get_all_pupils()
    school_db.close_connection()
    return render_template('allPupilsUSER.html', pupils=pupils)


@app.route('/adminLogin', methods=['GET', 'POST'])
def adminLogin():
    password = request.form.get('password')
    needed_password = "MOGE1234"
    if password == needed_password:
        school_db = SchoolDatabaseSQLite("school.db")
        pupils = school_db.get_all_pupils()
        school_db.close_connection()
        return render_template('allPupils.html', pupils=pupils)
    return render_template('adminLogin.html')


@app.route('/admin', methods=['GET'])
def adminIndex():
    school_db = SchoolDatabaseSQLite("school.db")
    pupils = school_db.get_all_pupils()
    school_db.close_connection()
    return render_template('allPupils.html', pupils=pupils)


@app.route('/add', methods=['GET', 'POST'])
def add_pupil():
    name = request.form.get('name')
    age = request.form.get('age')
    grade = request.form.get('grade')

    if name is not None:
        school_db = SchoolDatabaseSQLite("school.db")
        school_db.add_pupil(name, age, grade)
        pupils = school_db.get_all_pupils()
        school_db.close_connection()

        return render_template('addPupil.html', pupils=pupils)
    return render_template('addPupil.html')


@app.route('/update', methods=['GET', 'POST'])
def update_pupil():
    pupil_id = request.form.get('pupil_id')
    name = request.form.get('name')
    age = request.form.get('age')
    grade = request.form.get('grade')

    if pupil_id is not None:
        school_db = SchoolDatabaseSQLite("school.db")
        school_db.update_pupil(pupil_id, name, age, grade)
        pupils = school_db.get_all_pupils()
        school_db.close_connection()

        return render_template('updatePupil.html', pupils=pupils)
    return render_template('updatePupil.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_pupil():
    pupil_id = request.form.get('pupil_id')

    if pupil_id is not None:
        school_db = SchoolDatabaseSQLite("school.db")
        school_db.delete_pupil(pupil_id)
        pupils = school_db.get_all_pupils()
        school_db.close_connection()

        return render_template('deletePupil.html', pupils=pupils)
    return render_template('deletePupil.html')

    pupil_id = request.form.get('pupil_id')

    if pupil_id is not None:
        school_db = SchoolDatabaseSQLite("school.db")
        school_db.get_pupil(pupil_id)
        pu


if __name__ == "__main__":
    app.run(debug=True)
