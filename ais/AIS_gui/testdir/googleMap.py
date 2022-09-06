import gmplot
import webbrowser

lat = [24.04185, 24.0496, 24.04329]
lon = [120.33571, 120.33581, 120.33591]



gmapOne = gmplot.GoogleMapPlotter(24.04185,120.33571,15)
gmapOne.scatter(lat,lon, "blue", size = 50, marker =True)
gmapOne.plot(lat, lon, 'red',edge_width = 2.5)



gmapOne.draw("map.html")
webbrowser.open("map.html")


