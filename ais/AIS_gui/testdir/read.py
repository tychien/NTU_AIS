import csv

class Read():
    
    
    def __init__(self):
        mydict  = []
        path = '/home/tychien/Downloads/shipinformation_202109.csv'
        with open(path,'r') as csvfile:
            
            for i in range(3):
                line   = csvfile.readline()
                print(line)
    

if __name__ == '__main__':
    read = Read()

