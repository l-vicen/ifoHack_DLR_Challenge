import pandas as pd
import numpy as np
import geopandas as gpd
import cv2
import matplotlib.pyplot as plt
import rasterio as rio
from shapely.geometry import Point
from rasterio.plot import show

# Define city
city = "Köln"

"""neighborhoods_g_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/3 Neighborhoods/Neighborhoods_Berlin.gpkg").explode(index_parts=False)
print(neighborhoods_g_berlin)
print(neighborhoods_g_berlin.columns)
"""
"""
img = rio.open("./ifoHack_DLR_Challenge_Data/6 Sentinel/Sentinel_Berlin.tif")
blue, green, red, nir = img.read()
show(img.read(4))
"""
# Mapping dictionary for numerical value to land type (Grassland, etc.)
mapping_dict = {10: "Tree Cover",
 20: "Shrubland",
 30: "Grassland",
 40: "Cropland",
 50: "Built-up",
 60: "Bare vegetation",
 70: "Snow and Ice",
 80: "Permanent water bodies",
 90: "Herbaceous wetland",
 95: "Mangroves",
 100: "Moss and lichen",
}

if city=="Köln":
    tif_world = rio.open("./ifoHack_DLR_Challenge_Data/7 WorldCover/WorldCover_{}.tif".format(city)).read()
    a = tif_world.flatten()
else:
    tif_world = np.array(cv2.imread("./ifoHack_DLR_Challenge_Data/7 WorldCover/WorldCover_{}.tif".format(city)))
    a = tif_world[:, :, 0].flatten()

"""cv2.imshow('TIF image', tif_world)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

a_map = np.vectorize(mapping_dict.get)(a)

# Get coordinates of each pixel in TIF image
data = rio.open("./ifoHack_DLR_Challenge_Data/7 WorldCover/WorldCover_{}.tif".format(city))
coor = []
for i in range(0, data.height):
    for j in range(0, data.width):
        coor.append(Point(data.transform * (i,j)))
land_type = gpd.GeoDataFrame({'Land Type': a_map, 'geometry': coor}, columns=['Land Type', 'geometry'])
print(land_type)

land_g_price_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/1 Land Prices/Land_Prices_Neighborhood_{}.gpkg".format(city)).explode(index_parts=False)[["geometry", "Neighborhood_FID"]]
print(land_g_price_berlin)
print(land_g_price_berlin.columns)

# Overlay neighborhood polygons with Pixel points and aggregate features over neighbourhoods
land_type_region = pd.DataFrame(land_type.sjoin(land_g_price_berlin, how="left").dropna()[["Neighborhood_FID", "Land Type"]]).groupby(["Neighborhood_FID"]).value_counts().unstack(fill_value=0)
land_type_region.to_csv("WorldCover_{}.csv".format(city))
print(land_type_region)
print(land_type_region.columns)
