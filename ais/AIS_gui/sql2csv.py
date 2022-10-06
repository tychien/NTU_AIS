from asyncore import read
import os 
from datetime import datetime
from csv import DictReader, DictWriter, Sniffer

global NUM_OF_ROWS

def sqlToCsv(ORIGFILE,NEWFILE):
    print("Counting number of rows...")
    def countrows():
        counter = 0
        with open(ORIGFILE,'r') as read_obj:
            for line in read_obj:
                counter += 1
        return counter 
    
    NUM_OF_ROWS = countrows()
    print("Total rows: ", NUM_OF_ROWS)
    ###------check if column exist--------### 
    HAS_HEADER = False
    with open(ORIGFILE,'r') as read_obj, open(NEWFILE, 'a') as write_obj:
        sniffer = Sniffer()
        print('start sniffing')
        has_header = sniffer.has_header(read_obj.read(3000))
        print('end sniffing')
        read_obj.seek(0)
        dict_r = DictReader(read_obj,delimiter="\t")
        headers= dict_r.fieldnames
        print(headers)
        
        if has_header: 
            HAS_HEADER = True
            #print("HAS HEADER")
        else:
            HAS_HEADER = False
            #print("no header")
        
        print("Has header") if HAS_HEADER else print("No header.Converting...")
        
        if HAS_HEADER is False:

            read_obj.seek(0)

            write_obj.write("IMO_NUMBER,Call_Sign,ShipName,MMSI,Navigational_Status,ROT,SOG,Position_Accuracy,Longitude,Latitude,COG,True_Heading,Time_Stamp,Communication_Status,Ship_and_Cargo_Type,Reference_Position_A,Reference_Position_B,Reference_Position_C,Reference_Position_D,Fixing_Device,ETA,MAX_Draught,Destination,DTE,Gross_Tonnage,Record_Time,VSD,VSH,WMD,WMS\n")
            HAS_HEADER = True
            if HAS_HEADER == True:
                print("it has header now")
    


    with open(ORIGFILE, 'r') as read_file, open(NEWFILE, 'a') as write_file:
        counter = 0
        try:
            replace_delimiter = ','
            for line in read_file:
                counter += 1
                percentage = 100*counter/NUM_OF_ROWS
                print("{:.2f}% || {}/{}".format(percentage,counter, NUM_OF_ROWS))
                for element in line:
                    write_file.write(element.replace('\t',replace_delimiter))
                
        except:
            pass
            
        print("Converting Finished")
        return "Converting Complete!"
        



if __name__ == '__main__':
    convert = sqlToCsv()

    '''
    HOME = os.path.expanduser( '~' )
    orig_path = HOME+'/NTU_AIS/ais/AIS_gui/ais_201306_2.sql'
    #orig_path = '/Users/tychien/NTU_AIS/ais/AIS_gui/CHe1_5K.csv'
    new_path  = 'ais_new_2.csv'
    sqltest = sqlToCsv(orig_path, new_path)
    '''