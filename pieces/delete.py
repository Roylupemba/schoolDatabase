from functions import SchoolDatabaseSQLite

if __name__ == "__main__":
    db_name = "school.db"
    school_db = SchoolDatabaseSQLite(db_name)

    while True:
        print("")
        pupil_id = input("Enter PUPIL_ID")
        if school_db.delete_pupil(pupil_id):
            print(f"Pupil {pupil_id} has been removed from the database.")
        else:
            print(f"Pupil {pupil_id} not found.")

        result = input("\n Type 'yes' to edit another pupil \n Type 'no' to quit \n ")
        if result == "yes" or result == "YES":
            continue
        else:
            break
# Close the connection when done
    school_db.close_connection()