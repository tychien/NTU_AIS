from asyncore import read
import os 
from datetime import datetime
from csv import DictReader, DictWriter, Sniffer

def sqlToCsv(ORIGFILE,NEWFILE):
    #check if column exist 
    HAS_HEADER = False
    with open(ORIGFILE,'r') as read_obj, open(NEWFILE, 'w') as write_obj:
        sniffer = Sniffer()
        has_header = sniffer.has_header(read_obj.read(333333333333))
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
        
        print("Has header") if HAS_HEADER else print("No header")
        
        if HAS_HEADER is False:
            #with open(NEWFILE, 'a') as write_csv:
            #fieldnamesHeaders = {'IMO_NUMBER','Call_Sign','ShipName','MMSI','Navigational_Status','ROT','SOG','Position_Accuracy','Longitude','Latitude','COG','True_Heading','Time_Stamp','Communication_Status','Ship_and_Cargo_Type','Reference_Position_A','Reference_Position_B','Reference_Position_C','Reference_Position_D','Fixing_Device','ETA','MAX_Draught','Destination','DTE','Gross_Tonnage'}
            
            #writer = DictWriter(write_obj,fieldnames=fieldnamesHeaders, delimiter='\t')
            #writer.writeheader()
            read_obj.seek(0)
            content = read_obj.read()
            
            write_obj.write("IMO_NUMBER\tCall_Sign\tShipName\tMMSI\tNavigational_Status\tROT\tSOG\tPosition_Accuracy\tLongitude\tLatitude\tCOG\tTrue_Heading\tTime_Stamp\tCommunication_Status\tShip_and_Cargo_Type\tReference_Position_A\tReference_Position_B\tReference_Position_C\tReference_Position_D\tFixing_Device\tETA\tMAX_Draught\tDestination\tDTE\tGross_Tonnage\tRecord_Time\tVSD\tVSH\tWMD\tWMS\n"+content)
            #write_obj.write(content)
            HAS_HEADER = True

        print("shit")

    with open(NEWFILE, 'r') as read_obj:
        dict_r = DictReader(read_obj, delimiter='\t')
        for row in dict_r:
            long = (row['Latitude'])
            print(long)





        



if __name__ == '__main__':
    HOME = os.path.expanduser( '~' )

    orig_path = HOME+'/NTU_AIS/ais/AIS_gui/ais_201306_2.sql'
    #orig_path = '/Users/tychien/NTU_AIS/ais/AIS_gui/CHe1_5K.csv'
    new_path  = 'ais_new_2.csv'
    sqltest = sqlToCsv(orig_path, new_path)