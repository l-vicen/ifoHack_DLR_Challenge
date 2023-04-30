import pandas as pd

cities = ["Berlin", "Bremen", "Dresden", "Frankfurt_am_Main", "Köln"]
total_df = pd.DataFrame()
# Merge all relevant Dataframes to output co
for i in cities:
    zensus = pd.read_csv("Zensus/Zensus_{}_Value.csv".format(i)).drop(columns=["Unnamed: 0"])
    cover = pd.read_csv("WorldCover/WorldCover_{}.csv".format(i))
    osm = pd.read_csv("OSM/OSM_{}.csv".format(i)).drop(columns=["Unnamed: 0"])
    osm.columns = ["Neighborhood_FID", "Number_ways", "Length_ways"]
    distance = pd.read_csv("Distance/Distance_{}.csv".format(i), header=None)
    distance.columns = ["Neighborhood_FID", "Distance_station"]
    monuments = pd.read_csv("Monuments/Monuments_{}.csv".format(i), header=None)
    monuments.columns = ["Neighborhood_FID", "Distance_monuments"]
    poi = pd.read_csv("POI/POI_{}.csv".format(i), header=None)
    poi.columns = ["Neighborhood_FID", "Distance_POI"]
    university = pd.read_csv("University/University_{}.csv".format(i), header=None)
    university.columns = ["Neighborhood_FID", "Distance_University"]
    park1 = pd.read_csv("Park1/Park1_{}.csv".format(i), header=None)
    park1.columns = ["Neighborhood_FID", "Park_1"]
    park2 = pd.read_csv("Park2/Park2_{}.csv".format(i), header=None)
    park2.columns = ["Neighborhood_FID", "Park_2"]
    oper = pd.read_csv("Oper/Oper_{}.csv".format(i), header=None)
    oper.columns = ["Neighborhood_FID", "Distance_Oper"]
    temp1 = pd.merge(pd.merge(pd.merge(university, park1, how="inner", on=["Neighborhood_FID"]), park2, how="inner", on=["Neighborhood_FID"]), oper, how="inner", on=["Neighborhood_FID"])
    temp2 = pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(zensus, cover, how="inner", on=["Neighborhood_FID"]), osm, how="inner", on=["Neighborhood_FID"]), distance, how="inner", on=["Neighborhood_FID"]), monuments, how="inner", on=["Neighborhood_FID"]), poi, how="inner", on=["Neighborhood_FID"])
    df = pd.merge(temp1, temp2, how="inner", on=["Neighborhood_FID"])
    total_df = pd.concat([total_df, df], ignore_index=True)
print(total_df)
# Export total df as CSV
total_df.to_csv("total_df.csv")