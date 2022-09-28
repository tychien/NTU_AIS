from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from datetime import datetime
import tkinter as tk
import gmplot
import webbrowser
import timesplit as sp
import rangesplit as rs
import countWithoutMoving as ct
import sql2csv
global entry_file_from_ran
global entry_file_to_ran
global entry_lat
global entry_lon
global entry_RAN
#global entry_FROM
#global entry_TO
global entry_file
global entry_split_FROM
global entry_split_TO
global entry_file_TO
global entry_file_counting
global entry_sql 
global entry_csv

class Gui(tk.Tk):
    def browseFile_from_ran(self):
        file_name = filedialog.askopenfilename()
        self.entry_file_from_ran.delete(0, END)
        self.entry_file_from_ran.insert(0, file_name) 

    def browseFile_to_ran(self):
        file_name = filedialog.askopenfilename()
        self.entry_file_to_ran.delete(0, END)
        self.entry_file_to_ran.insert(0, file_name)

    def drawMap(self,lat,lon,ran,folder='/home/tychien/mitseagrantauv/ais/AIS_gui'):
        gmapOne = gmplot.GoogleMapPlotter(lat,lon,12)
        gmapOne.marker(float(lat),float(lon),'blue')
        gmapOne.circle(lat,lon,ran)

        url = folder+"/target.html"
        if url != "/folder/path/target.html":
            gmapOne.draw(url)
            webbrowser.open(url)
        else:
            print("please fill in the path")

    def getInput(self):
        _lat = self.entry_lat.get()
        _lon = self.entry_lon.get()
        _ran = int(self.entry_RAN.get())*1000
        #_from= self.entry_FROM.get()
        #_to  = self.entry_TO.get()
        _file_from = self.entry_file_from_ran.get()
        _file_to   = self.entry_file_to_ran.get()

        drawit = True
        #if drawit:
        #    self.drawMap(_lat,_lon,_ran) 
        #    print(_lat, _lon, _ran, _from, _to, _dir)
        rs.splitByRange(_lat,_lon,_ran,_file_from, _file_to) 

    def browseFile(self):
        file_name = filedialog.askopenfilename()
        self.entry_file.delete(0, END)
        self.entry_file.insert(0, file_name) 
    
    def browseFile_TO(self):
        file_name = filedialog.askopenfilename()
        self.entry_file_TO.delete(0, END)
        self.entry_file_TO.insert(0, file_name)
   
    def splitByTime(self):
        path_r = self.entry_file.get()
        path_w = self.entry_file_TO.get()
        start_time = self.entry_split_FROM.get()
        end_time = self.entry_split_TO.get()
        print
        sp.splitByTime(start_time, end_time, path_r, path_w)
    
    def browseFile_counting(self):
        file_name = filedialog.askopenfilename()
        self.entry_file_counting.delete(0, END)
        self.entry_file_counting.insert(0, file_name)

    def counting(self):
        readfile = self.entry_file_counting.get()
        ct.countShip(readfile)

    def browseFile_from_sql(self):
        file_name = filedialog.askopenfilename()
        self.entry_sql.delete(0, END)
        self.entry_sql.insert(0, file_name) 

    def browseFile_to_csv(self):
        file_name = filedialog.askopenfilename()
        self.entry_csv.delete(0, END)
        self.entry_csv.insert(0, file_name)


    def convert(self):
        path_r = self.entry_sql.get()
        path_w = self.entry_csv.get()
        sql2csv.sqlToCsv(path_r, path_w)

    def __init__(self):
        
        super().__init__()
        self.title("NTU_AIS")
        self.geometry("700x400")
        self.resizable(0,0)
        self.config(background = "black")
        tabControl = ttk.Notebook(self)
        tab1    = ttk.Frame(tabControl)
        tab2    = ttk.Frame(tabControl)
        tab3    = ttk.Frame(tabControl)
        tab4    = ttk.Frame(tabControl)
        tabControl.add(tab1,    text= "Split by Range")
        tabControl.add(tab2,    text= "Split by Time")
        tabControl.add(tab3,    text= "Count Ships")
        tabControl.add(tab4,    text= "sql to csv")
        tabControl.pack(expand = 1, fill = "both")
        ##TAB Range #############################################################
        
        label_POS = Label(tab1,
                        text    = "Position",
                        ).grid(column = 1, row = 1, ipadx=5, pady=5, sticky=E)
            #----------------------------------------------------------
        label_lat = Label(tab1,
                        text    = "Lat:",
                        ).grid(column = 2, 
                                row = 1, 
                                ipadx =5 , 
                                pady = 5, 
                                sticky = W)
            #----------------------------------------------------------
        self.entry_lat = Entry(tab1, width = 10)
        self.entry_lat.insert(0, "24.04185")
        self.entry_lat.grid(column = 3, row = 1, ipadx = 5, pady = 5, sticky = W)
            #----------------------------------------------------------
        label_lon = Label(tab1,
                        text    = "Lon:",
                        ).grid(column = 4, 
                                row = 1, 
                                ipadx =5 , 
                                pady = 5, 
                                sticky = W)
            #----------------------------------------------------------
        self.entry_lon = Entry(tab1, width = 10)
        self.entry_lon.insert(0, "120.33571")
        self.entry_lon.grid(column = 5, row = 1, ipadx = 5, pady = 5, sticky = W)

        #################################################################

        label_RAN = Label(tab1,
                        text    = "Range(km)",
                        ).grid(column = 1, 
                                row = 2, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)
            #--------------------------------------------------------------
        self.entry_RAN = Entry(tab1, width = 20)
        self.entry_RAN.insert(0, "15")
        self.entry_RAN.grid(column = 2, row = 2, columnspan = 3)

        ##################################################################
        '''
        label_FROM = Label(tab1,
                        text    = "From(UTC)",
                        ).grid(column = 1, 
                                row = 3, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)
            #------------------------------------------------------------
        self.entry_FROM = Entry(tab1, width = 20)
        self.entry_FROM.insert(0, "2021-09-17 23:45:00")
        self.entry_FROM.grid(column = 2, row = 3, columnspan = 3)

            #------------------------------------------------------------
        label_FROM_eg   = Label(tab1, 
                            text    = "format: YYYY-MM-DD HH:MM:SS",
                            ).grid(column = 5, 
                                    row = 3, 
                                    ipadx = 5, 
                                    pady = 5, 
                                    sticky=W)
        ####################################################################

        label_TO = Label(tab1,
                        text    = "To(UTC)",
                        ).grid(column = 1, 
                                row = 4, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)
            #---------------------------------------------------------------
        self.entry_TO = Entry(tab1, width = 20)
        self.entry_TO.insert(0, "2021-09-17 23:59:59")
        self.entry_TO.grid(column = 2, row = 4, columnspan = 3)

        '''
        label_FOLDER = Label(tab1,
                        text    = "Split From File",
                        ).grid(column = 1, 
                                row = 3, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)

            #------------------------------------------------------------------

        self.entry_file_from_ran = Entry(tab1, width = 20)
        self.entry_file_from_ran.insert(0, "/folder/path/file.csv")
        self.entry_file_from_ran.grid(column = 2, row = 3, columnspan = 3)

            #-------------------------------------------------------------------

        button_exp = Button(tab1,
                            text    = "Browse File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile_from_ran
                            ).grid(column = 5, 
                                    row = 3,
                                    ipadx = 5,
                                    pady    = 5,
                                    sticky=W)



        label_File_from_ran = Label(tab1, 
                                text    = "Split to File",
                                ).grid(column = 1, 
                                        row = 4,
                                        ipadx =5,
                                        pady = 5,
                                        sticky = E)
            #--------------------------------------------------------------------
        self.entry_file_to_ran = Entry(tab1, width = 20)
        self.entry_file_to_ran.insert(0, "/folder/path/file.csv")
        self.entry_file_to_ran.grid(column = 2, row = 4, columnspan = 3)
            #--------------------------------------------------------------------
        button_exp_1= Button(tab1, 
                            text    = "Browse File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile_to_ran
                            ).grid(column = 5,
                                    row   = 4,
                                    ipadx = 5,
                                    pady  = 5,
                                    sticky=W)
                                    
        #########################################################################
        '''
        button_exit = Button(tab1,
                            text    = "Exit",
                            bg      = "red",
                            fg      = "white",
                            command = exit).grid(column = 3, row = 6)
        '''
        button_apply = Button(tab1,
                            text    = "Apply",
                            bg      = 'blue',
                            fg      = 'black',
                            command = self.getInput).grid(column = 1, row = 6)

        
        ##TAB Time#######################################################################
        label_split_FROM = Label(tab2,
                        text    = "From(UTC)",
                        ).grid(column = 1, 
                                row = 3, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E
                                )
            #------------------------------------------------------------
        self.entry_split_FROM = Entry(tab2, width = 20)
        self.entry_split_FROM.grid(column = 2,row = 3, columnspan = 3)
        label_FROM_eg   = Label(tab2, 
                            text    = "format: YYYY-MM-DD HH:MM:SS",
                            ).grid(column = 5, 
                                    row = 3, 
                                    ipadx = 5, 
                                    pady = 5, 
                                    sticky=W)
        self.entry_split_FROM.insert(0,"2021-09-01 01:25:00")
        ####################################################################

        label_splt_TO = Label(tab2,
                        text    = "To(UTC)",
                        ).grid(column = 1, 
                                row = 4, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E
                                )
            #---------------------------------------------------------------
        self.entry_split_TO = Entry(tab2, width = 20)
        self.entry_split_TO.grid(column = 2, row = 4, columnspan = 3)
        self.entry_split_TO.insert(0, "2021-09-01 01:26:00")

        ########################################################################
        label_FILE_R = Label(tab2,
                        text    = "From csv File",
                        ).grid(column = 1, 
                                row = 5, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)

            #------------------------------------------------------------------

        self.entry_file = Entry(tab2, width = 20)
        self.entry_file.insert(0, "/folder/path/file.csv")
        self.entry_file.grid(column = 2, row = 5, columnspan = 3)

            #-------------------------------------------------------------------
        ########################################################################
        label_FILE_W = Label(tab2,
                        text    = "New file path and name",
                        ).grid(column = 1, 
                                row = 6, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)

            #------------------------------------------------------------------

        self.entry_file_TO = Entry(tab2, width = 20)
        self.entry_file_TO.insert(0, "/folder/path/new.csv")
        self.entry_file_TO.grid(column = 2, row = 6, columnspan = 3)

            #-------------------------------------------------------------------

        button_file = Button(tab2,
                            text    = "Select File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile
                            ).grid(column = 5, 
                                    row = 5,
                                    ipadx = 5,
                                    pady  = 5,
                                    sticky=W) 

        button_file = Button(tab2,
                            text    = "Select File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile_TO
                            ).grid(column = 5, 
                                    row = 6,
                                    ipadx = 5,
                                    pady  = 5,
                                    sticky=W)

        button_file = Button(tab2,
                            text    = "Split File",
                            bg      = "blue",
                            fg      = "black",
                            command = self.splitByTime
                            ).grid(column = 1, 
                                    row = 7,
                                    )
        '''
        button_exit = Button(tab2,
                            text    = "Exit",
                            bg      = "red",
                            fg      = "white",
                            command = exit
                            ).grid(column = 3, 
                                    row = 7)
        '''
        #---TAB Counting Ships--------
        label_Count_R = Label(tab3,
                        text    = "Read File",
                        ).grid(column = 1, 
                                row = 1, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)

            #------------------------------------------------------------------

        self.entry_file_counting = Entry(tab3, width = 20)
        self.entry_file_counting.insert(0, "/folder/path/file.csv")
        self.entry_file_counting.grid(column = 2, row = 1, columnspan = 3)
       
        button_count_file = Button(tab3,
                            text    = "Browse File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile_counting
                            ).grid(column = 5, 
                                    row = 1,
                                    ipadx = 5,
                                    pady    = 5,
                                    sticky=W)
        
        button_count = Button(tab3,
                            text    = "Count",
                            bg      = "Blue",
                            fg      = "black",
                            command = self.counting
                            ).grid(column = 1, 
                                    row = 3)
                    
        '''                    
        button_exit = Button(tab3,
                            text    = "Exit",
                            bg      = "red",
                            fg      = "white",
                            command = exit
                            ).grid(column = 3, 
                                    row = 3)
        '''
         ##TAB sql to csv #############################################################
 
        label_FOLDER = Label(tab4,
                        text    = "Original sql file",
                        ).grid(column = 1, 
                                row = 3, 
                                ipadx=5, 
                                pady=5, 
                                sticky=E)

            #------------------------------------------------------------------

        self.entry_sql = Entry(tab4, width = 20)
        self.entry_sql.insert(0, "/folder/path/file.csv")
        self.entry_sql.grid(column = 2, row = 3, columnspan = 3)

            #-------------------------------------------------------------------

        button_exp = Button(tab4,
                            text    = "Browse File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile_from_sql
                            ).grid(column = 5, 
                                    row = 3,
                                    ipadx = 5,
                                    pady    = 5,
                                    sticky=W)



        label_File_from_sql = Label(tab4, 
                                text    = "New CSV File Destination",
                                ).grid(column = 1, 
                                        row = 4,
                                        ipadx =5,
                                        pady = 5,
                                        sticky = E)
            #--------------------------------------------------------------------
        self.entry_csv = Entry(tab4, width = 20)
        self.entry_csv.insert(0, "/folder/path/file.csv")
        self.entry_csv.grid(column = 2, row = 4, columnspan = 3)
            #--------------------------------------------------------------------
        button_exp_1= Button(tab4, 
                            text    = "Browse File",
                            bg      = "white",
                            fg      = "black",
                            command = self.browseFile_to_csv
                            ).grid(column = 5,
                                    row   = 4,
                                    ipadx = 5,
                                    pady  = 5,
                                    sticky=W)
                                    
        #########################################################################
   
        button_apply = Button(tab4,
                            text    = "Apply",
                            bg      = 'blue',
                            fg      = 'black',
                            command = self.convert).grid(column = 1, row = 6)


if __name__ == "__main__":
    gui = Gui()
    gui.mainloop()
