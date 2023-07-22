from functions import SchoolDatabaseSQLite

if __name__ == "__main__":
    db_name = "school.db"
    school_db = SchoolDatabaseSQLite(db_name)

# Adding pupils
    while True:
        print("")
        name = input("What is the pupils name> ")
        age = input("How old is the pupil> ")
        grade = input("In which grade is the pupil going to> ")

        school_db.add_pupil(name,age,grade)
            
        print("")
        quit = input(" Type 'yes' to add another pupil \n Type 'no' to quit \n ")
        if quit == "yes" or quit == "YES":
            continue
        else:
            break
# Close the connection when done
    school_db.close_connection()