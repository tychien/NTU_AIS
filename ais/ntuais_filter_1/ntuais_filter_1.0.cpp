#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>


using namespace std;


//1     toRad()
//2     calculateDistance()
//3.    main()
// 3.a  找日期
// 3.b  找MMSI
// 3.b.1檢查是否為同一艘船
// 3.c  找Longitude, Latitude
// 3.d  calculatedistance
// 3.e  如果非同船且小於指定範圍，加入暫存
// 3.f  輸出暫存



double toRad(double degree)
{
    return degree/180*3.1415926;
}

double calculateDistance(double lat1, double long1, double lat2, double long2) 
{
    double dist;
    dist =  sin(toRad(lat1)) * sin(toRad(lat2)) + 
            cos(toRad(lat1)) * cos(toRad(lat2)) * cos(toRad(long1 - long2));
    dist = acos(dist);
    dist = 6371 * dist;
    return dist;
}

int main(int argc, char **argv)
{
    //----------------------------------
    //handling input words
    string search_date;
    string search_range;
    for(int i=1; i<argc; i++) {
     string argi = argv[i];
     if(argi.find("--date=") == 0)
       search_date = argi.substr(7);
     if(argi.find("--range=")== 0)
       search_range= argi.substr(8); 
    }
    if(search_date == "") {
     cout << "Usage: ./ntuais_filter --date=yyyy-mm-dd --range=km" << endl;
     exit(1);
    }
    if(search_range== ""){
        cout << "Usage: ./ntuais_filter --date=yyyy-mm-dd --range=km" << endl;
        exit(1);
    }
    
    string csvfile = search_date.substr(0,4)+search_date.substr(5,2)+".csv";



    //readfile
    fstream file;
    file.open(csvfile);    //輸入檔案名稱
    //string date = "2019-04-15"; //輸入欲查詢日期
    string date = search_date;
    string line;
    size_t pos=0;
    size_t pos_comma=0;
    string token;
    string mmsi,sog,longitude,latitude,cog,ship_type,
           reference_position_A,reference_position_B,reference_position_C,reference_position_D,
           maxDraught,grossTonnage,recordTime;
    double station_position_longitude = 120.273155; //輸入基點精度
    double station_position_latitude = 24.000825;   //輸入基點緯度
    double range = stod(search_range);               //輸入欲查詢半徑（公里）
    vector<string> mmsi_array;
    vector<string> ship_array;
    int j = 1;  //數第幾行
    
    

    //如果有找到該日期，算一筆
    
    while(getline(file,line)){
        bool same_ship = false;
        pos = line.find(date);
        if(pos != string::npos){
            token = line.substr(0,pos+29);
        
            //找到MMSI
            for(int n=1; n<=3; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1); 
            }
            mmsi = line.substr(0,line.find(","));
            cout << "MMSI: "<< mmsi << endl;            

                //檢查有沒有相同船名，若無就加入新船----------------- 
            for(vector<string>::iterator it=mmsi_array.begin(); it != mmsi_array.end(); ++it){
                if( *it == mmsi) {
                    same_ship = true;
                    cout << same_ship << endl;
                }
            }
           
                //~檢查有沒有相同船名，若無就加入新船-----------------
            //~MMSI
        
            cout << j << "/ " << token << endl; 
            j++; 
            
            //-----------------------------------
            //find SOG
            for(int n=1; n<=3; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            sog = line.substr(0,line.find(","));
            cout << "SOG: "<< sog << endl;
            
            //-----------------------------------
            //find longitude             
            for(int n=1; n<=2; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);     
            }
            longitude = line.substr(0,line.find(","));
            double longitude_d = stod(longitude);
            cout << "Lon: " << to_string(longitude_d) << endl;
            
            //--------------------------------------- 
            //find latitude 
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            latitude = line.substr(0,line.find(","));
            double latitude_d = stod(latitude);
            cout << "Lat: "<< to_string(latitude_d) << endl;

            //----------------------------------------
            //find COG (Course On Ground)
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            cog = line.substr(0,line.find(","));
            cout << "COG: "<< cog << endl;
            
            //----------------------------------------
            //find ship and cargo type
            for(int n=1; n<=4; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            } 
            ship_type = line.substr(0,line.find(","));
            cout << "Type: "<< ship_type << endl;
            
            //----------------------------------------
            //find reference_position_A
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            reference_position_A = line.substr(0,line.find(","));
            //---------------------------------------
            //find reference_position_B
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            reference_position_B = line.substr(0,line.find(","));
            //-----------------------------------------
            //find reference_position_C
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            reference_position_C = line.substr(0,line.find(","));
            
            //-----------------------------------------
            //find reference_position_D 
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            reference_position_D = line.substr(0,line.find(","));
            //-----------------------------------------
            //find MAX_Draught
            for(int n=1; n<=3; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            maxDraught = line.substr(0,line.find(","));
            cout << "MAX_Draught: " << maxDraught << endl;
            //----------------------------------------
            //find Gorss_Tonnage
            for(int n=1; n<=3; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            grossTonnage = line.substr(0,line.find(","));
            cout << "GrossTonnage: " << grossTonnage << endl;
            //-------------------------------------------
            //RecordTime
            for(int n=1; n<=1; n++){
                pos_comma = line.find(",");
                line.erase(0,pos_comma+1);
            }
            recordTime = line;
            cout << "RecordTime: " << recordTime << endl; 
            //----------------------------------------
            //Calculate the distance between station and the ship  
            double distance_in_KM = calculateDistance(latitude_d,longitude_d,
                    station_position_latitude, station_position_longitude);
            cout <<"Distance: "<< distance_in_KM <<" km. "<< "\n" << endl; 

            //-------------------------------------------
            //Calculate the ship_length & ship_width
            double ship_length  = stod(reference_position_A)+stod(reference_position_B);
            double ship_width   = stod(reference_position_C)+stod(reference_position_D); 
            //--------------------------------------------
            //filter out by range and same shipname  
            if(!same_ship && (distance_in_KM <range)){
                mmsi_array.push_back(mmsi);//+"\n"+token+"\n\n");
                //shipname_array.push_back(token); //如果用token就會找不到shipname
                ship_array.push_back("MMSI:"+mmsi+"\t"
                                    +"Distance:"+to_string(distance_in_KM)+"\t"
                                    +"Speed:"+sog+"\t"
                                    +"Course:"+cog+"\t"
                                    +"Type:"+ship_type+"\t"
                                    +"ShipLength:"+to_string(ship_length)+"\t"
                                    +"ShipWidth:"+to_string(ship_width)+"\t"
                                    //+"MAX_Draught:"+maxDraught+"\t"
                                    //+"GrossTonnage:"+grossTonnage+"\t"
                                    +"RecordTime:"+recordTime);
                same_ship = false;
            }
        }
    }
    
    //印出所有船---------------
    int shipcount = 1; 
    for(vector<string>::iterator it = mmsi_array.begin(); it !=mmsi_array.end(); ++it){
        cout << shipcount << "/ " << *it <<"\n"<< endl;
        shipcount ++;
    }
    cout << "filename=" << csvfile << endl;
    cout << "search_range=" << search_range << endl;
    //~印出所有船--------------

    //輸出到.csv檔案
        string outputfilecsv = "";
                outputfilecsv+= date;
                outputfilecsv+="_";
                outputfilecsv+= to_string(int(range));
                //outputfilecsv+=to_string(range);
                outputfilecsv+="km.csv";
        std::ofstream output_file(outputfilecsv);
        for(const auto &e : ship_array) output_file << e << "\n";            
    //~輸出到.csv檔案
    return 0;
}
