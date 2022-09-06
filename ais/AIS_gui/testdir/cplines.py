from csv import DictWriter
from csv import DictReader
from datetime import datetime
class Copy():

    def __init__(self):
        path = "/home/tychien/Downloads/shipinformation_202109.csv"
        with open(path,'r') as read_obj:        
            csv_dict_reader = DictReader(read_obj)
            counter = 0
            for row in csv_dict_reader:
                counter += 1
                if counter <=20:
                    with open('out_file.csv','a') as csv_file:
                        fieldnames = row.keys()
                        writer = DictWriter(csv_file, fieldnames, delimiter=',')
                        if counter == 1:
                            writer.writeheader()
                        writer.writerow(row)
                    
                    
                    print(row['MMSI'],row['Record_Time'])
                    row_t = str(row['Record_Time'])
                    print(row_t)
                    row_d = datetime.strptime(row_t, '%Y-%m-%d %H:%M:%S')
                    print(row_d.day)
                    print('2021-08-31 23:54:22')
                else:
                    break
if __name__ == '__main__':
    copy = Copy()
