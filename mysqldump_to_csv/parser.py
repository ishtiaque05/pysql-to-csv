import csv
import re
import ast
import logging
import traceback

class Parser(object):
    def __init__(self, options):
        self.__options = options
        self.__target = None
        self.__writer = None

    def is_insert_statement(self, line):
        return line.startswith('INSERT INTO')

    def get_table_headers(self, line):
        result = re.findall(r'\`([^\`]*)\`', line)
        if result and len(result):
            self.initialize_writer(result[0]+".csv")         
            return result[1:]
        else:
            return None   

    def initialize_writer(self, filename):
        try:
            if filename:
                self.__target = open(filename, 'w')
                self.__writer = csv.writer(self.__target)
            else:
                raise Exception('Target filename not set')   
        except Exception as e:
            logging.error(traceback.format_exc()) 

    def is_writer_set(self):
        return self.__writer != None

    def is_target_file_initialized(self):
        return self.__target != None           

    def get_values(self, line):
        values = line.strip().replace('NULL', "''")
        values = values[:-1]
        values = list(ast.literal_eval(values))
        return values

    def write_data(self, data):
        if(self.is_writer_set() and self.is_target_file_initialized()):
            self.__writer.writerow(data)     

    def parse(self, output_directory):
        is_insert = False
        with open(self.__options.filename, 'r') as read_file:
            for line in read_file:
                if(self.is_insert_statement(line)):
                    is_insert = True
                    headers = self.get_table_headers(line)
                    if headers:
                        self.write_data(headers)
                elif(is_insert):
                    data = self.get_values(line)
                    self.write_data(data)

