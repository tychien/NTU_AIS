import split as sp

path    = '/home/tychien/Downloads/shipinformation_202109.csv'
start_time  = '2021-09-01 00:00:01'
end_time    = '2021-09-01 00:00:32'
sp.splitByTime(start_time,end_time,path)
