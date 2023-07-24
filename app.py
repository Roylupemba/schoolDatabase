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
    needed_password = "DBSS1234"
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


@app.route('/get', methods=['GET', 'POST'])
def get_pupil_page():
    return render_template('get_pupil.html')


@app.route('/get_pupil', methods=['POST'])
def get_pupil():
    pupil_id = request.form['pupil_id']
    name = request.form['name']
    school_db = SchoolDatabaseSQLite("school.db")
    if pupil_id and name:
        return "Please provide either the pupil ID or the name, not both."

    if pupil_id:
        pupil = school_db.get_pupil(pupil_id)
        if pupil:
            name = pupil[1]
            age = pupil[2]
            grade = pupil[3]
            return f"Pupil with ID {pupil_id}: {name}, Age: {age}, Grade: {grade}"
        else:
            return f"Pupil with ID {pupil_id} not found."
    elif name:
        pupils_by_name = school_db.get_pupils_by_name(name)
        if pupils_by_name:
            pupils_info = "\n".join(
                [f"Pupil with name '{name}': ID: {pupil[0]}, Age: {pupil[2]}, Grade: {pupil[3]}" for pupil in pupils_by_name])
            return pupils_info
        else:
            return f"Pupil with name '{name}' not found."
    else:
        return "Please provide either the pupil ID or the name."


@app.route('/pupil', methods=['GET', 'POST'])
def get_Pupil():
    pupil_id = request.form.get('pupil_id')
    if pupil_id is not None:
        school_db = SchoolDatabaseSQLite("school.db")
        school_db.delete_pupil(pupil_id)
        pupils = school_db.get_all_pupils()
        pupil = school_db.get_pupil(pupil_id)
        school_db.close_connection()
        return render_template('getPupil.html', pupils=pupils)
    return render_template('getPupil.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
