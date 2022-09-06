/****************************************/ 
/*  NAME: tychien                       */
/*  FILE: ntuais_filter_2.0.h           */ 
/*  DATE: September 18th, 2020          */ 
/****************************************/
#ifndef ntuais_filter_HEADER
#define ntuais_filter_HEADER 

#include <string>

using namespace std;

struct Ship
{
            string mmsi;
            string sog;
            string lon;
            string lat;
            string cog;
            string ship_type;
            string ref_pA;
            string ref_pB;
            string ref_pC;
            string ref_pD;
            string recordtime;
            double ship_length;
            double ship_width;  
            double avgspeed; 
            double dist;
};

struct ShipOutPut
{
    string  mmsi;
    string  avgspeed; 
    string  ship_length;
    string  ship_width;
    string  ship_type;
    string  avgRange;
    string  entering_LAT;
    string  entering_LON;
    string  leaving_LAT;
    string  leaving_LON;
    string  entering_TIME;
    string  leaving_TIME;
    string  boundDIR; 
};



class NTUAIS_filter 
{
    public:
        NTUAIS_filter();
        ~NTUAIS_filter();
        
        bool    GetSearchDate(string input);
        bool    GetSearchRange(string input);
        string  ReturnDate();
        string  ReturnRange();
        vector<string>  ReadFile(string csvfile);
        string  GetString(string line, int m);

        double  toRad(double degree);
        double  CalculateDistance(double lat1, double long1, double lat2, double long2);
        //double  TimeCalculate(string t0, string t1); 
        double  TimeCalculate(string t0, string t1);
        double  AvgSpeedCalculate(vector<struct Ship> ship);
        int     ConvertTimeToSeconds(string time);
        void    CleanUpOverlapTime(vector<struct Ship> ship);
        void    ShowSTL(vector<struct Ship> ship);
        void    ShowStrSTL(vector<string> ship);

        vector<struct Ship> ship_array;
        vector<string> mmsi_list;
        vector<struct Ship> ship_sameMMSI;
        vector<vector<struct Ship> > ship_sameMMSIs;
        vector<string> vShipOutPut;
        struct Ship BuildShip(string s);
        void BuildupMMSIList(vector<struct Ship> vector1, vector<string> vector2); 

        double ReturnStationLat(){return station_Latitude;};
        double ReturnStationLon(){return station_Longitude;};

    protected:
        
        string  m_search_date;
        string  m_search_range;
        double  station_Latitude;
        double  station_Longitude; 
        double  lat_now; 
        double  lon_now;
        double  lat_previous;
        double  lon_previous;
        string  time_now;
        string  time_previous;
    private:
};
#endif
