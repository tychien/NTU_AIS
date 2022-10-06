from csv import DictReader, DictWriter, Sniffer

def finding(ORIGFILE):
        ###------check if column exist--------### 
    HAS_HEADER = False
    with open(ORIGFILE,'r') as read_obj:

        dict_r = DictReader(read_obj,delimiter="\t")
        for row in dict_r:
            lat = float(row['Latitude'])
            print(lat)


if __name__ == '__main__':
    convert = finding('/Users/a9114242/Downloads/allinfo_201305.csv')