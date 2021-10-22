import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import RealDictCursor

#import data_secret

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database='schedule_project_database',
            user='db_Admin',
            password='db_Admin',
            host='localhost',
            port='5432',
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection()

#EXECUTE GENERIC QUERY
def execute_query(query):
    connection = create_connection()
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
        connection.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred")

#READ
def execute_read_query(query):
    connection = create_connection()
    cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

#users = execute_read_query(select_users)
##
#for user in users:
#    print(user)


#CREATE
#query_insert = '''INSERT INTO public.contact 
#(id, "name", email, age, "zipCode", cellphone, address, addressNumber, "creationDate", lat, long, state, district) 
#VALUES(?, '', '', 0, '', '', '', '', '', '', '', '', '');'''

'''
users = [
    ("James", 25, "male", "USA"),
    ("Leila", 32, "female", "France"),
    ("Brigitte", 35, "female", "England"),
    ("Mike", 40, "male", "Denmark"),
    ("Elizabeth", 21, "female", "Canada"),
]

user_records = ", ".join(["%s"] * len(users))

insert_query = (
    f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, users)

'''
#UPDATE
#query_update = '''UPDATE public.contact
#SET "name"='', email='', age=0, "zipCode"='', cellphone='', address='', complements='', "creationDate"='', lat='', long='', state='', district=''
#WHERE id=?;'''

#DELETE
#query_delete = '''DELETE FROM public.contact
#WHERE id=?;'''
