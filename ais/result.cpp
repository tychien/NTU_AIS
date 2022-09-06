#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string GetString(string line, int m){
    for(int n=1; n<=m; n++){
        size_t pos_comma = line.find(",");
        line.erase(0,pos_comma+1);
    } 
    string get_line = line.substr(0,line.find(","));
    return get_line;
}

int main(int argc, char **argv)
{
    string m_date, m_range, m_time; 
    for(int i=1; i<argc; i++){
            string argi = argv[i];
            if(argi.find("--date=")==0)
                m_date = argi.substr(7);
            if(argi.find("--time=")==0)
                m_time = argi.substr(7);
            if(argi.find("--range=")==0)
                m_range=argi.substr(8);
    } 

    string csvfile = ""
        +m_date
        +"_"
        +m_range
        +"km.csv";

    fstream file;
    //file.open("2019-02-26_50km.csv");
    file.open(csvfile);
    string line;
   
    /*mmsi, length, width, avgspeed, type, enterLAT, enterLON, enterTIME, leaveLAT, leaveLON, leaveTIME, Boundfor, shortest_dist, shortest_dist_time */ 
    int     type;
    double  length, width, avgspeed, enterLAT, enterLON, leaveLAT, leaveLON, shortest_dist;
    string  mmsi, enterTIME, leaveTIME, BoundFor, shortest_dist_time;
   
    string  time, enterTIMEhh, leaveTIMEhh; 
    int i = 1;
    bool firstline = true;
    string title = "";
    string output = "";
    vector<string> shiplist; 
    
    while(getline(file,line)){
        if (firstline==true){
            title = line;
            firstline = false;
            output = title;
        }

        else{
            mmsi    = GetString(line,0);
            length  = stod(GetString(line,1));
            width   = stod(GetString(line,2));
            avgspeed= stod(GetString(line,3));
            type    = stoi(GetString(line,4));
            enterLAT= stod(GetString(line,5));
            enterLON= stod(GetString(line,6));
            enterTIME=GetString(line,7);
            leaveLAT= stod(GetString(line,8));
            leaveLON= stod(GetString(line,9));
            leaveTIME=GetString(line,10);
            BoundFor= GetString(line,11);
            shortest_dist=stod(GetString(line,12));
            shortest_dist_time=GetString(line,13);
            

            enterTIMEhh = enterTIME.substr(11,2);
            leaveTIMEhh = leaveTIME.substr(11,2);

            time = shortest_dist_time.substr(11,2); 
            if(m_time<=leaveTIMEhh && m_time>=enterTIMEhh)
               shiplist.push_back(line); 
            output = leaveTIMEhh;
        }
        cout <<i << ":" << m_date << "_"<< m_time << "_" <<m_range << endl;
        i++;
    } 
    for(vector<string>::const_iterator i = shiplist.begin(); i!=shiplist.end(); i++)
        cout << *i << endl;

    string  outputfilecsv = "";
            outputfilecsv+= m_date+"_"+m_time+"_"+ m_range+"km.csv";
    std::ofstream output_file(outputfilecsv);
    for(const string &e : shiplist) output_file << e << "\n";

    return 0;
}
