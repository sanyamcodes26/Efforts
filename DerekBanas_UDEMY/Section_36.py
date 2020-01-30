import sqlite3
import sys
import csv


def create_table(db_connect, table_name):
    try:
        db_connect.execute(f'''CREATE TABLE {table_name}(
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                f_name TEXT NOT NULL,
                                l_name TEXT NOT NULL,
                                age INT NOT NULL,
                                address TEXT,
                                salary REAL,
                                hire_date TEXT);''')
        db_connect.commit()
    except sqlite3.OperationalError as e:
        print(">> ! Table could not be created")
        print(e)
    else:
        print(">> Table Created")
    return


def insert_data(db_connect, table_name):
    try:
        db_connect.execute(f'''INSERT INTO {table_name}(
                                f_name, l_name, age, address, salary, hire_date)
                                VALUES('Akash', 'Sengupta', 21, 'Road Link', 5000, date('now'));''')
        db_connect.commit()
    except sqlite3.OperationalError as e:
        print(">> ! Employee could not be entered")
        print(e)
    else:
        print(">> Employee Entered")
    return


def drop_table(db_connect, table_name):
    db_connect.execute(f"DROP TABLE IF EXISTS {table_name}")
    return


def print_db(the_cursor, table_name):
    try:
        result = the_cursor.execute(f'''SELECT id, f_name, l_name, age, address, salary, hire_date
                                        FROM {table_name};''')
        for row in result:
            print(">> ID\t\t\t\t:\t", row[0])
            print(">> F_Name\t\t\t:\t", row[1])
            print(">> L_Name\t\t\t:\t", row[2])
            print(">> AGE\t\t\t\t:\t", row[3])
            print(">> ADDRESS\t\t\t:\t", row[4])
            print(">> SALARY\t\t\t:\t", row[5])
            print(">> HIRE DATE\t\t:\t", row[6])
    except sqlite3.OperationalError:
        print(">> ! Table doesn't exist.")
    except:
        print(">> ! Could not retrieve data.")
    else:
        print(">> Here is your data")
    return


def update_db(db_connect, table_name, key, value, attribute, condition):
    try:
        db_connect.execute(f'''UPDATE {table_name}
                                SET {key} = '{value}'
                                WHERE {attribute} = {condition};''')
        db_connect.commit()
    except sqlite3.OperationalError as e:
        print(">> ! Database could not be updated.")
        print(e)
    else:
        print(">> Database Updated.")
    return


def delete_data(db_connect, table_name, attribute, condition):
    try:
        db_connect.execute(f'''DELETE FROM {table_name}
                                WHERE {attribute} = {condition}''')
        db_connect.commit()
    except sqlite3.OperationalError:
        print(">> ! Data could not be updated.")
    else:
        print(">> Data Updated.")
    return


def alter_table(db_connect, table_name):
    try:
        db_connect.execute(f'''ALTER TABLE {table_name}
                                ADD COLUMN 'image' BLOB DEFAULT NULL''')
        db_connect.commit()
    except sqlite3.OperationalError as e:
        print(">> ! Table Could not be altered")
        print(e)
    else:
        print(">> Table altered")
    return


if __name__ == "__main__":
    db_connect = sqlite3.connect('Section_36_test.db')
    print(">> Database Created")
    the_cursor = db_connect.cursor()

    the_cursor.execute("SELECT SQLITE_VERSION();")
    print(the_cursor.fetchone())
    table_name = "employees"
    create_table(db_connect, table_name)
    insert_data(db_connect, table_name)
    print_db(the_cursor, table_name)

    update_db(db_connect, table_name, 'address', '48 A/1 UMR', 'id', 1)
    print_db(the_cursor, table_name)

    with db_connect:
        db_connect.row_factory = sqlite3.Row
        the_cursor = db_connect.cursor()
        the_cursor.execute("SELECT * FROM employees")
        rows = the_cursor.fetchall()
        for row in rows:
            print("{} {}".format(row["f_name"], row["l_name"]))

    with open('Section_36_dump.txt', 'a') as f:
        for line in db_connect.iterdump():
            f.write("%s\n" % line)

    delete_data(db_connect, table_name, 'id', 1)
    print_db(the_cursor, table_name)

    db_connect.rollback()
    print_db(the_cursor, table_name)

    alter_table(db_connect, table_name)
    print_db(the_cursor, table_name)

    the_cursor.execute(f"PRAGMA TABLE_INFO({table_name})")
    row_names = [nameTuple[1] for nameTuple in the_cursor.fetchall()]
    print(row_names)

    the_cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    print(the_cursor.fetchall()[0][0])

    db_connect.close()
    # drop_table(db_connect, table_name)
