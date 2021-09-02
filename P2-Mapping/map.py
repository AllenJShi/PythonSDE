import folium
import pandas

"""
Read the dataset and store lattitude, longitude and elevation data into respective variables
"""
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_differentiator(elevation):
    """
        This method will produce colar parameter which guide the color specification against different elevation levels
    Args:
        elevation ([int]): read the elevation number from dataset and return a string identifying colors based on elevation levels
    """
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red' 
    
"""
Create a map object using folium.Map() as our base layer
"""
map = folium.Map(location=[39,-99], zoom_start=5, tiles="Stamen Terrain")

"""
Create two layers for volcanoes and populations
"""
volcanoes = folium.FeatureGroup(name="Volcanoes")
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
for at, on, el, na in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html%(na,na,el),width=200, height=100)
    volcanoes.add_child(folium.Marker(location=[at, on], popup=folium.Popup(iframe), icon = folium.Icon(color = color_differentiator(el))))
    # volcanoes.add_child(folium.CircleMarker(location=[at,on], radius=8, 
    #                                         popup=str(el)+" m", fill_color=color_differentiator(el), 
    #                                         color='grey',fill=True, fill_opacity=0.7))

populations = folium.FeatureGroup(name="Populations")
populations.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(), 
                                     style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(volcanoes)
map.add_child(populations)
map.add_child(folium.LayerControl())
map.save("map.html")