from datetime import datetime
from csv import DictReader, DictWriter, Sniffer

def sqlToCsv(ORIGFILE,NEWFILE):
    #check if column exist 
    with open(ORIGFILE,'r') as read_obj:
        sniffer = Sniffer()
        has_header = sniffer.has_header(read_obj.read(13333))
        read_obj.seek(0)
        dict_r = DictReader(read_obj)
        headers= dict_r.fieldnames
        print(headers)
        
        if has_header: 
            print("HAS HEADER")
            print()
        else:
            print("no header")




        





if __name__ == '__main__':
    orig_path = '/Users/tychien/NTU_AIS/ais/AIS_gui/ais_201306_2.sql'
    #orig_path = '/Users/tychien/NTU_AIS/ais/AIS_gui/CHe1_5K.csv'
    new_path  = 'ais_new_1.csv'
    sqltest = sqlToCsv(orig_path, new_path)