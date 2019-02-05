import mysql.connector
from mysql.connector import errorcode
from pysql_to_csv.csv_writer import CSVWriter

class Converter(object):
    def __init__(self, options):
        self.__options = options
        self.conn = self.connect_to_sql()
        self.cur = self.conn.cursor()

    def connect_to_sql(self):
        try:
            cnx = mysql.connector.connect(
                host=self.__options.host,
                user=self.__options.user,
                passwd=self.__options.passwd,
                database=self.__options.db
            )
            print("Connection Established Successfully!")
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def execute_query(self):
        query = "SELECT * FROM " + self.__options.tblname
        self.cur.execute(query)

        field_names = [i[0] for i in self.cur.description]
        csv = CSVWriter(self.__options.tblname+".csv")
        csv.write_header(field_names)
        for row in self.cur:
            csv.write_row(row)
        print("Successfully Converted table {} to csv".format(self.__options.tblname+".sql"))

    def __del__(self):
        self.conn.close()
