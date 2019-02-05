import csv
import logging
import traceback

class CSVWriter(object):
    def __init__(self, filename):
        try:
            self.__file = open(filename, 'w')
            self.__writer = csv.writer(self.__file)
        except Exception as e:
            logging.error(traceback.format_exc())

    def write_row(self, data):
        self.__writer.writerow(data)

    def write_header(self, header):
        self.__writer.writerow(header)

    def __del__(self):
        self.__file.close()
