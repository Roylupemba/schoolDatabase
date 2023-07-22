from functions import SchoolDatabaseSQLite

if __name__ == "__main__":
    db_name = "school.db"
    school_db = SchoolDatabaseSQLite(db_name)

    while True:
        print("")
        pupil_id = input("Enter PUPIL_ID> ")
        pupil_info = school_db.get_pupil(pupil_id)
        if pupil_info:
            print(f"\nPupil {pupil_id} info:", pupil_info)
        else:
            print(f"Pupil {pupil_id} not found.")
        result = input("\n Type 'yes' to add another pupil \n Type 'no' to quit \n ")
        if result == "yes" or result == "YES":
            continue
        else:
            break
# Close the connection when done
    school_db.close_connection()