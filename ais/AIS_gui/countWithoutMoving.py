from dataclasses import field
from itertools import count
import json
from pathlib import Path
from csv import DictReader, DictWriter
from datetime import datetime
def countShip(readpath,reportfile,speedthreshold,timeresolution):
    datelist = []
    datedict = {}
    countdict= {}
    shiplist = []
    mmsilist = []
    
    dtformat = '%Y-%m-%d %H:%M:%S'
    with open(readpath,'r') as read_obj, open(reportfile,'a') as write_obj:
        write_obj.write('date,ships\n')
        csv_dict_reader = DictReader(read_obj)
        print("timeresolution: "+timeresolution+ " type:" + str(type(timeresolution)))
        
        #### Read the csv file and sort them to the seperate date or hour list
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
            hour    = record_time_d.hour
            date    = str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)
            dateNtime = date+'{:02d}'.format(hour)
            if timeresolution == "hr": #hour
                if dateNtime in datelist:
                    pass
                else:
                    datelist.append(dateNtime)

            if timeresolution == "day": #date
                if date in datelist:
                    pass
                else:
                    datelist.append(date)
        print(datelist)
        datedict = {key:[] for key in datelist}
        
        for ship in shiplist:
            record_time     = ship['Record_Time'][:19]
            sog             = float(ship['SOG'])
            if record_time == '-1' or sog < float(speedthreshold):
                continue
            record_time_b = datetime.strptime(record_time,dtformat)
            year    = record_time_b.year
            month   = record_time_b.month
            day     = record_time_b.day
            hour    = record_time_b.hour
            date    = str(year)+'{:02d}'.format(month)+'{:02d}'.format(day)
            dateNtime = date+'{:02d}'.format(hour)
            if timeresolution == "hr": #hour
                datedict[dateNtime].append(ship)
            if timeresolution == "day": #date
                datedict[date].append(ship)
        

        ########################################################################


        def write_ships_report(format): #dateNtime or date 
            for format in datedict:
                mmsilist.clear()
                for i in range(len(datedict[format])):
                    print(i,len(datedict[format]))
                    tmmsi = datedict[format][i-1]['MMSI']
                    if tmmsi in mmsilist:
                        pass
                    else:
                        mmsilist.append(tmmsi)
                print(format, len(mmsilist))
                countdict[format] = len(mmsilist)
                write_obj.write(str(format)+','+str(len(mmsilist))+"\n")



        if timeresolution == "hr": #hour
            write_ships_report(dateNtime)


        if timeresolution == "day": #date
            write_ships_report(date)


    print("There are "+str(len(shiplist))+" ship messages.\n")
    return_msg = "Counting Complete!\n Total msgs:" +str(len(shiplist))+"\n"
    for k in countdict.items():
        return_msg+= str(k)+"\n"
    return return_msg

if __name__ == '__main__':
    countshipt = countShip()
    #countshipt = countShip(str(Path.home())+'/Downloads/201903test.csv')
    #countshipt = countShip(str(Path.home())+'/mitseagrantauv/ais/AIS_gui/CHs/CHs_5K.csv')
