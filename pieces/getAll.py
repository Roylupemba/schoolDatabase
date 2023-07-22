from functions import SchoolDatabaseSQLite

if __name__ == "__main__":
    db_name = "school.db"
    school_db = SchoolDatabaseSQLite(db_name)
    all_pupils = school_db.get_all_pupils()
    print("All pupils in the database:", all_pupils)

    # Close the connection when done
    school_db.close_connection()