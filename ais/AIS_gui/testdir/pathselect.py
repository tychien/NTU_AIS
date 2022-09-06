from tkinter import *
from tkinter import filedialog
import gmplot
import webbrowser

def browseFiles():
    folder_name = filedialog.askdirectory()
    entry_folder.delete(0, END)
    entry_folder.insert(0, folder_name) 

def drawMap(lat,lon,ran,folder):
    gmapOne = gmplot.GoogleMapPlotter(lat,lon,12)
    gmapOne.circle(lat,lon,ran)
    url = folder+"/target.html"
    if url != "/folder/path/target.html":
        gmapOne.draw(url)
        webbrowser.open(url)
    else:
        print("please fill in the path")

def getInput():
    _lat = entry_lat.get()
    _lon = entry_lon.get()
    _ran = int(entry_RAN.get())*1000
    _from= entry_FROM.get()
    _to  = entry_TO.get()
    _dir = entry_folder.get()
    
    drawit = True
    if drawit:
        drawMap(_lat,_lon,_ran,_dir) 
        print(_lat, _lon, _ran, _from, _to, _dir)

window = Tk()
window.title("Select Folder")
window.geometry("800x800")
window.config(background = "black")

###############################################################

label_POS = Label(window,
                text    = "Position",
                bg      = "black",
                fg      = "white")
label_POS.grid(column = 1, row = 1, ipadx=5, pady=5, sticky=E)
    #----------------------------------------------------------
label_lat = Label(window,
                text    = "Lat:",
                bg      = "black",
                fg      = "white")
label_lat.grid(column = 2, row = 1, ipadx =5 , pady = 5, sticky = W)
    #----------------------------------------------------------
entry_lat = Entry(window, width = 10)
entry_lat.insert(0, "24.04185")
entry_lat.grid(column = 3, row = 1, ipadx = 5, pady = 5, sticky = W)
    #----------------------------------------------------------
label_lon = Label(window,
                text    = "Lon:",
                bg      = "black",
                fg      = "white")
label_lon.grid(column = 4, row = 1, ipadx =5 , pady = 5, sticky = W)
    #----------------------------------------------------------
entry_lon = Entry(window, width = 10)
entry_lon.insert(0, "120.33571")
entry_lon.grid(column = 5, row = 1, ipadx = 5, pady = 5, sticky = W)

#################################################################

label_RAN = Label(window,
                text    = "Range(km)",
                bg      = "black",
                fg      = "white")
label_RAN.grid(column = 1, row = 2, ipadx=5, pady=5, sticky=E)
    #--------------------------------------------------------------
entry_RAN = Entry(window, width = 20)
entry_RAN.insert(0, "15")
entry_RAN.grid(column = 2, row = 2, columnspan = 3)

##################################################################

label_FROM = Label(window,
                text    = "From(UTC)",
                bg      = "black",
                fg      = "white")
label_FROM.grid(column = 1, row = 3, ipadx=5, pady=5, sticky=E)
    #------------------------------------------------------------
entry_FROM = Entry(window, width = 20)
entry_FROM.insert(0, "YYYY/MM/DD/hh/mm/ss")
entry_FROM.grid(column = 2, row = 3, columnspan = 3)
####################################################################

label_TO = Label(window,
                text    = "To(UTC)",
                bg      = "black",
                fg      = "white")
label_TO.grid(column = 1, row = 4, ipadx=5, pady=5, sticky=E)
    #---------------------------------------------------------------
entry_TO = Entry(window, width = 20)
entry_TO.insert(0, "YYYY/MM/DD/hh/mm/ss")
entry_TO.grid(column = 2, row = 4, columnspan = 3)

#######################################################################

label_FOLDER = Label(window,
                text    = "File Folder",
                bg      = "black",
                fg      = "white")
label_FOLDER.grid(column = 1, row = 5, ipadx=5, pady=5, sticky=E)

    #------------------------------------------------------------------

entry_folder = Entry(window, width = 20)
entry_folder.insert(0, "/folder/path")
entry_folder.grid(column = 2, row = 5, columnspan = 3)

    #-------------------------------------------------------------------

button_exp = Button(window,
                    text    = "Browse Folders",
                    bg      = "white",
                    fg      = "black",
                    command = browseFiles)
button_exp.grid(column = 5, row = 5)

#########################################################################

button_exit = Button(window,
                    text    = "Exit",
                    bg      = "red",
                    fg      = "white",
                    command = exit)
button_exit.grid(column = 3, row = 6)

button_apply = Button(window,
                    text    = "Apply",
                    bg      = 'blue',
                    fg      = 'white',
                    command = getInput)
button_apply.grid(column = 1, row = 6)
window.mainloop()
