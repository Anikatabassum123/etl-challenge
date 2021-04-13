import logging
import csv
import os

from database import Database

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


class EtlScript:
    def __init__(self):
        self.database_conn = Database("acme")
        self.header_file = "headers.txt"
        self.data_file = "data.csv"
        self.out_file = "output.csv"

    def load_file_to_database(self, file_path: str):
        self.database_conn.load_file(file_path)

    def run(self):
        # Your code starts here

        hf = open('../'+self.header_file)
        df = open('../'+ self.data_file)

        #Headers
        hlist = []
        while line := hf.readline():
            hlist.append(line.strip("\n"))
        print(hlist)

        #Data

        data = []
        data.append(hlist)  
        while line := df.readline():
            tmp = []
            for e in line.split("|"):
                tmp.append(e.strip("\n"))
            data.append(tmp)
        print(data)

        #Write to csv File

        file = open('filterData.csv','w')

        writer = csv.writer(file)
        writer.writerows(data)

        #Write to DB
        self.load_file_to_database(os.path.abspath(file.name))
        

if __name__ == "__main__":
    EtlScript().run()
