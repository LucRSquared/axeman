import pandas
import geopandas
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


transport_mode = 'walk'

vics = pandas.read_csv('victims.csv')

selection = (vics['Confirmed Axeman'] == 'Yes') | (vics['Confirmed Axeman'] == 'Maybe')

vicselect = vics.loc[selection,['Latitude','Longitude']]
vicselect.head()
#vicselect.iloc[2,1] # third element, first second column
lat = vicselect['Latitude']
lon = vicselect['Longitude']


graph = ox.graph_from_place('New-Orleans, LA', network_type=transport_mode, simplify=True)
nodes, edges = ox.graph_to_gdfs(graph, nodes=True, edges=True)

vorig = 0 
vtarget = 6 
orig_node = ox.get_nearest_node(graph, (lat[vorig], lon[vorig]))
target_node = ox.get_nearest_node(graph, (lat[vtarget], lon[vtarget]))

length = nx.shortest_path_length(G=graph, source=orig_node, target=target_node, weight='length')

print(length)

#gdf = geopandas.GeoDataFrame(vicselect, geometry=geopandas.points_from_xy(vicselect['Longitude'], vicselect['Latitude']))
gdf = geopandas.GeoDataFrame(vicselect, geometry=geopandas.points_from_xy(lon, lat))
#fig, ax = ox.plot_graph(graph, fig_height=20, fig_width=None, close =False, show =False)


#plt.show()
