from datetime import datetime
from csv import DictReader, DictWriter
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
def splitByTime(start_time,end_time,readpath,writepath):
    count = 0
    pre_day = None
    pre_hour = None
    dtformat    = '%Y-%m-%d %H:%M:%S'
    start_time_d= datetime.strptime(start_time,dtformat)
    end_time_d= datetime.strptime(end_time,dtformat)
    counter = 0
    with open(readpath,'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        try:
            for row in csv_dict_reader:
                count += 1
                rec_time    = str(row['Record_Time']).split('.')[0]
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
                        
                    if start_time_d <= rec_time_d <= end_time_d:
                        counter += 1
                        with open(writepath,'a') as wp:
                            fieldnames  = row.keys()
                            writer      = DictWriter(wp, fieldnames, delimiter=',')
                            if counter == 1:
                                writer.writeheader()
                            writer.writerow(row)
                        print(counter, rec_time)
                        #if counter >20:
                        #    print('new file saved in '+ writepath)
                        #    break
        except:
            print(count, row['Record_Time'],readpath, writepath)

        print("Finished")
        return "Split by Time Finished!"

if __name__ == '__main__':
    split = splitByTime()
