from dataclasses import field
import json
from pathlib import Path
from csv import DictReader, DictWriter
from datetime import datetime
def countShip(readpath):
    datelist = []
    datedict = {}
    countdict= {}
    shiplist = []
    mmsilist = []
    
    dtformat = '%Y-%m-%d %H:%M:%S'
    with open(readpath,'r') as read_obj, open('/Users/a9114242/Downloads/report.csv','a') as write_obj:
        write_obj.write('date,ships\n')
        csv_dict_reader = DictReader(read_obj)
        
        for row in csv_dict_reader:
            shiplist.append(row)
            mmsi= row['MMSI']
            record_time   = row['Record_Time'][:19]
            if record_time == '-1':
                continue
            record_time_d = datetime.strptime(record_time,dtformat)
            year    = record_time_d.year
            month   = record_time_d.month
            day     = record_time_d.day
            date    = str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)
            if date in datelist:
                pass
            else:
                datelist.append(date)
        datedict = {key:[] for key in datelist}
        
        for ship in shiplist:
            record_time     = ship['Record_Time'][:19]
            sog             = float(ship['SOG'])
            if record_time == '-1' or sog < 0.5:
                continue
            record_time_b = datetime.strptime(record_time,dtformat)
            year    = record_time_b.year
            month   = record_time_b.month
            day     = record_time_b.day
            date    = str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)
            datedict[date].append(ship)
        
        for date in datedict:
            mmsilist.clear()
            for i in range(len(datedict[date])+1):
                tmmsi = datedict[date][i-1]['MMSI']
                if tmmsi in mmsilist:
                    pass
                else:
                    mmsilist.append(tmmsi)
            print(date, len(mmsilist))
            countdict[date] = len(mmsilist)
            write_obj.write(json.dumps(countdict))

                
    print(len(shiplist))
    print(countdict)
if __name__ == '__main__':
    countshipt = countShip()
    #countshipt = countShip(str(Path.home())+'/Downloads/201903test.csv')
    #countshipt = countShip(str(Path.home())+'/mitseagrantauv/ais/AIS_gui/CHs/CHs_5K.csv')
