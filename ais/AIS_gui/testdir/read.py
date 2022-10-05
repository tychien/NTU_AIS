

class Read():
    
    
    def __init__(self):
        mydict  = []
        read_path = '/Users/a9114242/Downloads/allinfo_201305.sql'
        write_path= '/Users/a9114242/Downloads/201305.csv'
        with open(read_path,'r') as csvfile, open(write_path, 'a') as write_file:
            write_file.write("IMO_NUMBER\tCall_Sign\tShipName\tMMSI\tNavigational_Status\tROT\tSOG\tPosition_Accuracy\tLongitude\tLatitude\tCOG\tTrue_Heading\tTime_Stamp\tCommunication_Status\tShip_and_Cargo_Type\tReference_Position_A\tReference_Position_B\tReference_Position_C\tReference_Position_D\tFixing_Device\tETA\tMAX_Draught\tDestination\tDTE\tGross_Tonnage\tRecord_Time\tVSD\tVSH\tWMD\tWMS\n")
            try:
                for line in csvfile:
                    #line   = csvfile.readline()
                    print(line)
                    write_file.write(line)
            except:
                pass
    

if __name__ == '__main__':
    read = Read()

