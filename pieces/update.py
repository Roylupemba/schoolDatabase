from functions import SchoolDatabaseSQLite

if __name__ == "__main__":
    db_name = "school.db"
    school_db = SchoolDatabaseSQLite(db_name)

    while True:
        print("")
        pupil_id = input("Enter PUPIL_ID")
        updated_name = input("Ente new name")
        updated_age = input("Ente new age")
        updated_grade = input("Ente new grade")
        school_db.update_pupil(pupil_id, name=updated_name,age=updated_age,grade=updated_grade )
        print(f"Updated info for pupil {pupil_id}:", school_db.get_pupil(pupil_id))

        result = input("\n Type 'yes' to edit another pupil \n Type 'no' to quit \n ")
        if result == "yes" or result == "YES":
            continue
        else:
            break
# Close the connection when done
    school_db.close_connection()