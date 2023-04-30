import pandas as pd
import geopandas as gpd

# Define city
city = "Frankfurt_am_Main"

land_g_price_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/1 Land Prices/Land_Prices_Neighborhood_{}.gpkg".format(city)).explode(index_parts=False)
print(land_g_price_berlin)
print(land_g_price_berlin.columns)

# Import all Zensus data from city
buildings_berlin = pd.read_csv("./ifoHack_DLR_Challenge_Data/2 Zensus/Zensus_{}_Buildings.csv".format(city), sep=";").drop(columns=["Unnamed: 0"])
families_berlin = pd.read_csv("./ifoHack_DLR_Challenge_Data/2 Zensus/Zensus_{}_Families.csv".format(city), sep=";").drop(columns=["Unnamed: 0"])
households_berlin = pd.read_csv("./ifoHack_DLR_Challenge_Data/2 Zensus/Zensus_{}_Households.csv".format(city), sep=";").drop(columns=["Unnamed: 0"])
population_berlin = pd.read_csv("./ifoHack_DLR_Challenge_Data/2 Zensus/Zensus_{}_Population.csv".format(city), sep=";").drop(columns=["Unnamed: 0"])
print(buildings_berlin)
print(buildings_berlin.columns)
print(families_berlin)
print(households_berlin)
print(population_berlin)

# Merge all Zensus data for city
total_berlin = pd.merge(pd.merge(pd.merge(buildings_berlin, families_berlin, how="inner", on=["Grid_Code"]), households_berlin, how="inner", on=["Grid_Code"]), population_berlin, how="inner", on=["Grid_Code"])
print(total_berlin)
print(total_berlin.columns)

# Overlay neighborhood polygons with Zensus grid
g_berlin = gpd.read_file("./ifoHack_DLR_Challenge_Data/2 Zensus/Zensus_{}_Grid_100m.gpkg".format(city))
total_position = pd.merge(total_berlin, g_berlin, how="left", on=["Grid_Code"])
overlay = gpd.overlay(gpd.GeoDataFrame(total_position[["Grid_Code", "geometry"]]), land_g_price_berlin[["Neighborhood_FID", "geometry"]], how="intersection")
overlay['area'] = overlay['geometry'].area/10**6
overlay.sort_values(by=['area'], inplace=True)
overlay.drop_duplicates(subset='Grid_Code', keep='last', inplace=True)
overlay.drop(['area', 'geometry'], inplace=True, axis=1)
total_position = pd.merge(total_position, pd.DataFrame(overlay), how="left", on=["Grid_Code"])

# Aggregate features over neighbourhoods
total_region = total_position.drop(columns=["Grid_Code", "City_Code", "geometry"]).groupby(["Neighborhood_FID"]).sum().reset_index()
zensus_price = pd.merge(total_region, land_g_price_berlin[["Neighborhood_FID", "Land_Value", "Area_Types", "Area_Count", "City_Name"]], how="left", on=["Neighborhood_FID"])
print(zensus_price)
print(zensus_price.columns)
zensus_price.to_csv("Zensus_{}_Value.csv".format(city))


