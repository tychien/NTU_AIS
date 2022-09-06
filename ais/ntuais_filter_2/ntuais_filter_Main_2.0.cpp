/************************************************************/
/* Author: Tim TingYuan Chien 前定遠r07525118@ntu.edu.tw    */
/* Version 2                                                */
/* In Version 2, the speed has been replaced                */
/*      by average speed.                                   */ 
/************************************************************/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include "ntuais_filter_2.0.h"

using namespace std;


int main(int argc, char **argv)
{
    NTUAIS_filter ntuais_filter;
    for(int i=1; i<argc; i++){
        string argi = argv[i];
        if(argi.find("--date=")==0)
            ntuais_filter.GetSearchDate(argi.substr(7));
        if(argi.find("--range=")==0)
            ntuais_filter.GetSearchRange(argi.substr(8));
    } 
    
    if(ntuais_filter.ReturnDate()  == "" || (ntuais_filter.ReturnDate().size()!=10)){
        cout << "Usage: ./ntuais_filter --date=yyyy-mm-dd --range=km" << endl;
        exit(1);
    }
    
    if(ntuais_filter.ReturnRange() == ""){
        cout << "Usage: ./ntuais_filter --date=yyyy-mm-dd --range=km" << endl;
        exit(1);
    }

    string csvfile  = ntuais_filter.ReturnDate().substr(0,4)
                    + ntuais_filter.ReturnDate().substr(5,2)
                    + ".csv";
        /*******************//*DATE*//******從時間篩資料************/
    vector<string> ship_list = ntuais_filter.ReadFile(csvfile);//RAW Messages on that date
/*******************************************************************************/
    //Chop the String and Build the Ships and store them into a list;
    
    for(vector<string>::const_iterator i = ship_list.begin(); i!=ship_list.end(); i++){
        struct Ship ships   = ntuais_filter.BuildShip(*i);
        double ship_length  = stod(ships.ref_pA)+stod(ships.ref_pB);
        double ship_width   = stod(ships.ref_pC)+stod(ships.ref_pD);
        cout << ship_length << endl; 
        double ship_lat     = stod(ships.lat);
        double ship_lon     = stod(ships.lon);
        
        ships.ship_length   = ship_length;
        ships.ship_width    = ship_width;
        double distant = ntuais_filter.CalculateDistance(ntuais_filter.ReturnStationLat(),ntuais_filter.ReturnStationLon(), ship_lat, ship_lon);
        ships.dist  = distant; 
        /******************//*RANGE*//******從範圍篩資料**存到ship_array*********/
        if(distant< stod(ntuais_filter.ReturnRange())) 
            ntuais_filter.ship_array.push_back(ships); 
    }
/*******從ship_array找相同mmsi的msg存成string到mmsi_list中***********************/ 
    
    for(vector<struct Ship>::const_iterator i = ntuais_filter.ship_array.begin(); i!=ntuais_filter.ship_array.end(); i++){
        Ship ship = *i;
        bool same_ship = false; 
        for(vector<string>::const_iterator k = ntuais_filter.mmsi_list.begin(); k!=ntuais_filter.mmsi_list.end(); k++){
            if(ship.mmsi == *k)
               same_ship = true;
        }
        if(!same_ship)
            ntuais_filter.mmsi_list.push_back(ship.mmsi);
        cout << "time:"<<ship.recordtime<< endl;
        cout << "dist:" << ship.dist<< endl;
    }

/****************************從mmsi_list找相同mmsi的船存到ship_sameMMSI*******************/
    vector<string> file_ship_array;
    file_ship_array.push_back("mmsi,length,width,avgspeed,type,enterLAT,enterLON,enterTIME,leaveLAT,leaveLON,leaveTIME,BoundFor,shortest_dist,shortest_dist_time");
    vector<struct Ship> ship_sameMMSI;//這裏要建object 
    vector<vector<struct Ship> > ship_sameMMSIs; //分群的各MMSI們for the big circle under RANGE
    for(vector<string>::const_iterator i= ntuais_filter.mmsi_list.begin(); i!=ntuais_filter.mmsi_list.end(); i++){
        string shipi = *i;
        cout << "-----------------------------------------------------------"<< endl;
        cout << "shipi:" << shipi << endl;
        for(vector<struct Ship>::const_iterator k = ntuais_filter.ship_array.begin(); 
                k!=ntuais_filter.ship_array.end(); k++){
            if(shipi== k->mmsi){
                ship_sameMMSI.push_back(*k); 
            }
        }
        /*******************將ship_sameMMSI裡重疊的時間內的資料刪掉*****************/ 
        //ntuais_filter.CleanUpOverlapTime(ship_sameMMSI);
        cout << "We Have "<<ship_sameMMSI.size() <<" ship_sameMMSI msgs. " <<endl;
        bool has_previous_time = false;
        int previous_time = 0;
        for(vector<struct Ship>::const_iterator j = ship_sameMMSI.begin(); 
                j!=ship_sameMMSI.end();){
            cout << j->recordtime << endl;
            string now_recoredtime = j->recordtime;
            int t1_secs = ntuais_filter.ConvertTimeToSeconds(now_recoredtime);
            cout <<"previous_time:" << previous_time << " ,t1_secs:"<< t1_secs << endl;
            while(has_previous_time == false){
                previous_time = t1_secs;
                has_previous_time =true;
            }

            if((has_previous_time == true )&& (previous_time > t1_secs)){
                j=ship_sameMMSI.erase(j);
                cout << "erase("<<&j<<")"<< endl;
            }
            
            else
                j++; 
        }
       
        /***************************************************************************/
        //計算平均速度
        double avgspeed = ntuais_filter.AvgSpeedCalculate(ship_sameMMSI);
        //檢查算出來的平均速度是否為NaN
        if(isnan(avgspeed)){
            cout <<"Single AIS Msg"<< endl;
            vector<struct Ship>::const_iterator a=ship_sameMMSI.begin();
            Ship ship = *a;
            avgspeed = stod(a->sog);
        }
        cout << "AvgSpeed=" << avgspeed <<" knots "<< endl;
        cout << "-----------------------------------------------------------"<< endl;
        
        ship_sameMMSIs.push_back(ship_sameMMSI);
/******************************輸出到CSV********************************************/ 
        vector<struct Ship>::const_iterator z = ship_sameMMSI.begin();
        string file_mmsi = z->mmsi;
        cout << "file_mmsi:"<<file_mmsi << endl;
        string file_length = to_string(z->ship_length);
        cout << "file_length:"<<file_length<<endl;
        string file_width = to_string(z->ship_width);
        cout << "file_width:" << file_width<< endl;
        string file_avgspeed = to_string(avgspeed);
        cout << "file_avgspeed:"<<file_avgspeed<< endl;
        string file_type = z->ship_type;
        cout << "file_type:" << file_type << endl;
        cout << ship_sameMMSI.size() << endl;
        string file_enterLAT;
        string file_enterLON;
        string file_enterTIME;
        string file_leaLAT;
        string file_leaLON;
        string file_leaTIME;
        string file_bound; 
        string file_dist;
        string file_shortestdist= "";
        string file_shortestdist_time="";
        if(ship_sameMMSI.size()==1){
            file_enterLAT = z->lat;
            cout << "file_entLAT:" << file_enterLAT << endl;
            file_enterLON = z->lon;
            cout << "file_entLON:" << file_enterLON << endl;
            file_enterTIME = z->recordtime;
            cout << "file_enterTIME:" << file_enterTIME << endl;
            file_leaLAT = z->lat;
            file_leaLON = z->lon;
            file_leaTIME= z->recordtime;
            file_bound  = "SingleAISMsg";
            file_dist   = z->dist;
            file_shortestdist = to_string(z->dist);
            file_shortestdist_time = z->recordtime;
        }
        else if(ship_sameMMSI.size()>1){
            file_enterLAT = z->lat;
            cout << "file_entLAT:" << file_enterLAT << endl;
            file_enterLON = z->lon;
            cout << "file_entLON:" << file_enterLON << endl;
            file_leaLAT = (z+(ship_sameMMSI.size()-1))->lat;
            cout << "file_leaLAT:" << file_leaLAT << endl;
            file_leaLON = (z+ship_sameMMSI.size()-1)->lon;
            cout << "file_leaLON:" << file_leaLON << endl;
            file_enterTIME = z->recordtime;
            cout << "file_entTIME:" << file_enterTIME << endl;
            file_leaTIME = (z+ship_sameMMSI.size()-1)->recordtime;
            cout << "file_leaTIME:" << file_leaTIME << endl;
            if(stod(file_enterLAT)-stod(file_leaLAT)>0)
                file_bound = "South";
            if(stod(file_enterLAT)-stod(file_leaLAT)<0)
                file_bound = "North";
            if(stod(file_enterLAT)-stod(file_leaLAT)==0) 
                file_bound = "East-West";
            cout << file_bound << endl; 
            double shortest_dist = 0;
            string time ="";
            for(vector<struct Ship>::const_iterator i=ship_sameMMSI.begin(); i!= ship_sameMMSI.end(); i++){
                bool    init = true;
                while(init==true){
                    shortest_dist = i->dist;
                    time = i->recordtime;
                    init    = false;
                }
                if(((i->dist)<shortest_dist) && (init==false)){
                    shortest_dist = i->dist;
                    time = i->recordtime;
                }
            }
            file_shortestdist = to_string(shortest_dist);
            file_shortestdist_time = time;
            cout <<"shortest_dist:" << shortest_dist << endl; 
            cout <<"time:"<< time << endl;
        }
        file_ship_array.push_back(file_mmsi     +","
                                +file_length    +","
                                +file_width     +","   
                                +file_avgspeed  +","
                                +file_type      +","
                                +file_enterLAT  +","
                                +file_enterLON  +","
                                +file_enterTIME +","
                                +file_leaLAT    +","
                                +file_leaLON    +","
                                +file_leaTIME   +","
                                +file_bound     +","
                                +file_shortestdist +","
                                +file_shortestdist_time
                                );

/***********************************************************************************/
        ship_sameMMSI.clear(); 
    }



/***********************************************************************************/
    cout << "----------------------------------------------------------"<<endl;
    ntuais_filter.ShowStrSTL(ntuais_filter.mmsi_list);
    string outputfilecsv = "";
           outputfilecsv+= ntuais_filter.ReturnDate();
           outputfilecsv+="_";
           outputfilecsv+= ntuais_filter.ReturnRange();
           outputfilecsv+="km.csv";
    std::ofstream output_file(outputfilecsv);
    for(const string &e : file_ship_array) output_file << e << "\n";    

    return 0;
}
