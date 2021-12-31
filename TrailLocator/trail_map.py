import folium # library to create interactive maps
import pandas # library to load dataframe

# load the hiking trail data
trail_data = pandas.read_csv("trail_information.txt")

# assigning lattitude, longitude, and difficulty to variables
latt = list(trail_data["LAT"])
long = list(trail_data["LON"])
diff = list(trail_data["DIFF"])
name = list(trail_data["NAME"])

# method to assign marker color to trails based on difficulty
def difficulty_color(difficulty):
    if difficulty == 'easy':
        return 'green'
    elif difficulty == 'medium':
        return 'orange'
    else:
        return 'red'

# adding coordinates for pennsylvania, zooming in on start, creating terrain map
map = folium.Map(location=[40.043626, -75.211839], zoom_start = 7, tiles = "Stamen Terrain")

# feature group for easy trails
fg_easy = folium.FeatureGroup(name = "Easy")

# feature group for medium trails
fg_medium = folium.FeatureGroup(name = "Medium")

# feature group for hard trails
fg_hard = folium.FeatureGroup(name = "Hard")

# add easy trail markers to map
for lattitude, longitude, difficulty, trail in zip(latt, long, diff, name):
    if difficulty == 'easy':
        # add elements to map
        fg_easy.add_child(folium.CircleMarker(location=[lattitude, longitude],
        radius = 6, popup = trail, fill_color = difficulty_color(difficulty),
        color = 'grey', fill_opacity = 0.9))

    elif difficulty == 'medium':
        # add elements to map
        fg_medium.add_child(folium.CircleMarker(location=[lattitude, longitude],
        radius = 6, popup = trail, fill_color = difficulty_color(difficulty),
        color = 'grey', fill_opacity = 0.9))

    else:
        # add elements to map
        fg_hard.add_child(folium.CircleMarker(location=[lattitude, longitude],
        radius = 6, popup = trail, fill_color = difficulty_color(difficulty),
        color = 'grey', fill_opacity = 0.9))

# add features to map
map.add_child(fg_easy)
map.add_child(fg_medium)
map.add_child(fg_hard)

# add layer control
map.add_child(folium.LayerControl())

# save features to map
map.save("TrailMap.html")
