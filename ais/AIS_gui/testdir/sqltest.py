from datetime import datetime
from csv import DictReader, DictWriter


class SqlTest:
    def __init__(self):
        path = '/Users/a9114242/Downloads/allinfo_201306_2.sql'
        self.sqltest(path)

    def sqltest(self, readpath):
        with open(readpath,'r') as read_obj:
            count = 0
            for line in read_obj:
                count += 1
                #print("Line{}: {}".format(count, line.strip()))
                split_str = line.split("\t")
#               print(split_str)
                print(split_str[3])
if __name__ == '__main__':
	split = SqlTest()

    
		
