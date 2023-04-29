"""
In this file we have defined all Macro variables (similar to: enums) 
that concern constant String values such that we could make the code 
in other files cleaner.
"""

from shapely.geometry import Point

# List of cities
GERMAN_CITIES = ["Berlin", "Bremen", "Dresden", "Frankfurt", "Köln"]

# App Style Logo
DLR_LOGO = "assets/DLR_Logo.png"

# Constant Coordinates of the HbF
BERLIN_HBF = Point(13.369398652505957, 52.52508850317093)
BREMEN_HBF = Point(8.813293978426122, 53.08325214483858)
DRESDEN_HBF = Point(13.731504930570084, 51.04058047869031)
FRANKFURT_HBF = Point(8.662028121380025, 50.10671622956832)
KOELN_HBF = Point(6.958572139550114, 50.9433787324542)

# Relative Path to datasets
PATH_BERLIN_DATA = "./data/1 Land Prices/Land_Prices_Neighborhood_Berlin.gpkg"
PATH_KOLN_DATA = "data/1 Land Prices/Land_Prices_Neighborhood_Köln.gpkg"
PATH_DRESDEN_DATA = "data/1 Land Prices/Land_Prices_Neighborhood_Dresden.gpkg"
PATH_BREMEN_DATA = "data/1 Land Prices/Land_Prices_Neighborhood_Bremen.gpkg"
PATH_FRANKFURT_DATA = "data/1 Land Prices/Land_Prices_Neighborhood_Frankfurt_am_Main.gpkg"