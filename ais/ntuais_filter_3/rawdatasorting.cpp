#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string getString(string line, int m)
{
    for(int n = 1; n<=m; n++){
        size_t pos_comma = line.find(",");
        line.erase(0,pos_comma+1);
    } 
    string getline = line.substr(0,line.find(","));
    return getline;
}

string monthToString(int month)
{
    string strmonth;
    if(month<10)
        strmonth = "0"+to_string(month);
    else if(month > 9 && month<13)
        strmonth = to_string(month);
    return strmonth;
}

int readFile(string year, string month, vector<string> ship_list)
{
    fstream file;
    file.open(year+month+".csv");
    string line;
    while(getline(file,line)){
        string recordtime = getString(line,25); 
        string linemonth = recordtime.substr(0,7);
        if(linemonth==month)
            ship_list.push_back(line);
    }
    return 0;
}




int main(int argc, char **argv)
{
    string month = "";
    int intmonth = 0;
    int intyear  = 0;
    for(int i =1; i<argc; i++){
        
        string argi = argv[i];
        if(argi.find("--month=")==0)
            month = argi.substr(8);
            intyear = stoi(month.substr(0,4));
            intmonth= stoi(month.substr(5,2)); 
            cout << "month = " << month << " intyear = "<< intyear << " intmonth = " << intmonth << endl;
    }
    
    if(month == "" || month.size()!=7){
        cout << "Usage: ./rawdatasorting --month=yyyy-mm" << endl;
        exit(1);
    }
    string strmonth = "";
    string stryear = to_string(intyear); 
    
    int monthbefore = intmonth-1;
    int monthafter  = intmonth+1;
    

    cout << "month = " << month << " stringmonth = "<<strmonth << endl;
    vector<string> ship_list; 
    
    if(intmonth==1){
        readFile(stryear, monthToString(intmonth),ship_list);
        readFile(stryear, monthToString(monthafter),ship_list);
    }
    if(intmonth==12){
        readFile(stryear,monthToString(monthbefore),ship_list);
        readFile(stryear,monthToString(intmonth),ship_list);
    }

    else{
        readFile(stryear, monthToString(monthbefore), ship_list);
        readFile(stryear, monthToString(intmonth), ship_list);
        readFile(stryear, monthToString(monthafter), ship_list);
    }
    std::ofstream output_file("new"+month+".csv");
    for(const string &e : ship_list) output_file << e << "\n";

    return 0;
}
