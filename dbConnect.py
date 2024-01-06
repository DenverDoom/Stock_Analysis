import cx_Oracle as db


def create_connection(username, password, server):
    try:
        con = db.connect(username + '/' + password + '@' + server)
        print("Database connection successful")
        return con
    except db.DatabaseError as er:
        print(er)
        return None


def create_cursor(connection):
    try:
        cursor = connection.cursor()
        print("Cursor creation successful")
        return cursor
    except db.DatabaseError as er:
        print(er)
        return None


def execute_query(cursor, query):
    try:
        cursor.execute(query)
        print("Query executed successfully")
        return cursor
    except db.DatabaseError as er:
        print(er)
        return None


def fetch_data(executor, flag):
    if flag >= 0:
        try:
            if flag == 0:
                rows = executor.fetchall()
                print(len(rows),'rows are fetched')
                return rows
            else:
                rows = executor.fetchmany(flag)
                print(len(rows),'row(s) is(are) fetched')
                return rows
        except db.DatabaseError as er:
            print(er)
            return None
    else:
        print("Flag should be greater than zero")
        return None

