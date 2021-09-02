import folium
import pandas

"""
Read the dataset and store lattitude, longitude and elevation data into respective variables
"""
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_differentiator(elevation):
    """[summary]
        This method will produce colar parameter which guide the color specification against different elevation levels
    Args:
        elevation ([int]): read the elevation number from dataset and return a string identifying colors based on elevation levels
    """
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red' 
    
map = folium.Map(location=None, zoom_start=5, title="Stamen")


map.save("map.html")