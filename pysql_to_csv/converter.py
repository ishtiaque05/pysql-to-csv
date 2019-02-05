import mysql.connector
from mysql.connector import errorcode

class Converter(object):
    def __init__(self, options):
        self.__options = options

    def connect_to_sql(self):
        try:
            cnx = mysql.connector.connect(
                host=self.__options.host,
                username=self.__options.username,
                password=self.__options.password,
                database=self.__options.database
            )
            print("Connection Established {}".format(cnx))
            cursor = cnx.cursor()
            return cursor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def execute_query(self, cursor):
        query = ("SELECT * FROM %s")
        table_name = self.__options.tablename
        cursor.execute(query, (table_name))

        for row in cursor:
            print(row)

