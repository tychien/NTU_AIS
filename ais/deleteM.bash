#!/bin/bash 

for((i=25;i<29;i++))
    do 
        vim -s deleteM.vim 2019-02-$i\_10km.csv 
        vim -s deleteM.vim 2019-02-$i\_20km.csv
        vim -s deleteM.vim 2019-02-$i\_30km.csv
    done
for((i=1;i<10;i++))
    do 
        vim -s deleteM.vim 2019-03-0$i\_10km.csv
        vim -s deleteM.vim 2019-03-0$i\_20km.csv
        vim -s deleteM.vim 2019-03-0$i\_30km.csv
    done
for((i=10;i<32;i++))
    do 
        vim -s deleteM.vim 2019-03-$i\_10km.csv 
        vim -s deleteM.vim 2019-03-$i\_20km.csv
        vim -s deleteM.vim 2019-03-$i\_30km.csv
    done
for((i=1;i<10;i++))
   do 
       vim -s deleteM.vim 2019-04-0$i\_10km.csv
       vim -s deleteM.vim 2019-04-0$i\_20km.csv
       vim -s deleteM.vim 2019-04-0$i\_30km.csv
   done
