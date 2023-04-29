"""
In this file we have defined all Macro variables (similar to: enums) 
that concern constant String values such that we could make the code 
in other files cleaner.
"""

from shapely.geometry import Point

GERMAN_CITIES = ["Berlin", "Bremen", "Dresden", "Frankfurt", "Köln"]

DLR_LOGO = "assets/DLR_Logo.png"

BERLIN_HBF = Point(13.369398652505957, 52.52508850317093)

PATH_BERLIN_DATA = "./data/1 Land Prices/Land_Prices_Neighborhood_Berlin.gpkg"