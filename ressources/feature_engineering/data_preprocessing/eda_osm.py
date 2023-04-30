import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Define city
city = "Bremen"

if city=="Bremen":
    osm_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/5 OSM/OSM_{}.gpkg".format(city)).explode(index_parts=False).drop(columns=["name", "osm_id", "other_tags", "type"])
    osm_berlin = osm_berlin.to_crs(epsg=3035)
else:
    osm_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/5 OSM/OSM_{}.gpkg".format(city)).explode(index_parts=False).drop(columns=["name", "z_order", "osm_id", "other_tags", "man_made", "highway", "waterway", "aerialway", "railway"])
    osm_berlin = osm_berlin[osm_berlin["barrier"].notna()].drop(columns=["barrier"]).reset_index(drop=True).to_crs(epsg=3035)
print(osm_berlin)

land_g_price_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/1 Land Prices/Land_Prices_Neighborhood_{}.gpkg".format(city)).explode(index_parts=False)[["geometry", "Neighborhood_FID"]]
print(land_g_price_berlin)
print(land_g_price_berlin.columns)

# Overlay neighborhood polygons with OSM paths (highways, waterways, etc.)
connection_region = osm_berlin.sjoin(land_g_price_berlin, how="left").dropna().drop(columns=["index_right"])
print(connection_region)

# Aggregate features over neighbourhoods
count_region = connection_region.groupby(["Neighborhood_FID"]).count().reset_index()
print(count_region)
connection_region["length"] = connection_region["geometry"].length
length_region = connection_region.drop(columns=["geometry"]).groupby(["Neighborhood_FID"]).sum().reset_index()
print(length_region)

output_region = pd.merge(count_region, length_region, how="inner", on=["Neighborhood_FID"])
print(output_region)
output_region.to_csv("OSM_{}.csv".format(city))

