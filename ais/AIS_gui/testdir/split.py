from datetime import datetime
from csv import DictReader


'''
global pre_day
global pre_hour
class splitByTime():
def __init__():
    pre_day = None
    pre_hour= None
    path    = '/home/tychien/Downloads/shipinformation_202109.csv'
    start_time  = '2021-09-01 00:00:01'
    end_time    = '2021-09-01 00:00:32'
    self.splitByTime(start_time, end_time, path)
'''

def splitByTime(start_time,end_time,path):
    pre_day = None
    pre_hour = None
    dtformat    = '%Y-%m-%d %H:%M:%S'
    start_time_d= datetime.strptime(start_time,dtformat)
    end_time_d= datetime.strptime(end_time,dtformat)
    counter = 0
    with open(path,'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            rec_time    = str(row['Record_Time'])
            if (rec_time != 'None'):
                rec_time_d  = datetime.strptime(rec_time, dtformat)
                if pre_day != rec_time_d.day:
                    print(str(rec_time_d.year)
                            +'-'+str(rec_time_d.month)
                            +'-'+str(rec_time_d.day)
                            +' '+str(rec_time_d.hour)
                            +':'+str(rec_time_d.minute)
                            +':'+str(rec_time_d.second))
                    pre_day = rec_time_d.day
                
                elif pre_hour != rec_time_d.hour:
                    print(str(rec_time_d.year)
                            +'-'+str(rec_time_d.month)
                            +'-'+str(rec_time_d.day)
                            +' '+str(rec_time_d.hour)
                            +':'+str(rec_time_d.minute)
                            +':'+str(rec_time_d.second))
                    pre_hour = rec_time_d.hour
                    
                if start_time_d < rec_time_d < end_time_d:
                    counter += 1
                    print(counter, rec_time)
                    if counter >20:
                        break
if __name__ == '__main__':
    split = splitByTime()
