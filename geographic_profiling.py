import pandas
import osmnx as ox
import networkx as nx
#import osrm

transport_mode = 'walk'

vics = pandas.read_csv('victims.csv')

lat = vics['Latitude']
lon = vics['Longitude']

selection = (vics['Confirmed Axeman'] == 'Yes') | (vics['Confirmed Axeman'] == 'Maybe')

vicselect = vics.loc[selection,['Latitude','Longitude']]
vicselect
#vicselect.iloc[2,1] # third element, first second column

graph = ox.graph_from_place('New-Orleans, LA', network_type=transport_mode, simplify=True)
edges = ox.graph_to_gdfs(graph, nodes=False, edges=True)


#result = osrm.simple_route(
#                      [21.0566163803209,42.004088575972], [20.9574645547597, 41.5286973392856],
#                      output='route', overview="full", geometry='wkt')
