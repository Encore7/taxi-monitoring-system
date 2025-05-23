import pandas as pd
import os
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

# Load the data
file_path = 'C:/Users/Lenovo/bd24_project_m8_b/processed_taxi_data.csv'
data = pd.read_csv(file_path)

# Convert the timestamp column to datetime format
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Define the start and end dates for the interval
start_date = '2008-02-02'
end_date = '2008-02-08'

# Filter the data within the specified date range
filtered_data = data[(data['timestamp'] >= start_date) & (data['timestamp'] <= end_date)]

# Check if any taxi exists in multiple locations at the same time
duplicate_locations = filtered_data.groupby(['taxi_id', 'timestamp']).filter(lambda x: len(x) > 1)

# Define the output file path
output_file_path = 'C:/Users/Lenovo/bd24_project_m8_b/preprocessed_taxi_data.csv'

# Check if the file already exists
if os.path.exists(output_file_path):
    print("Data is processed.")
else:
    # Save the results to the CSV file
    duplicate_locations.to_csv(output_file_path, index=False)
    print(f"Results saved to {output_file_path}")

# Display the duplicate locations (if any)
if not duplicate_locations.empty:
    print("Taxis found in multiple locations at the same time:")
    print(duplicate_locations)
else:
    print("No taxis found in multiple locations at the same time.")

# Convert longitude and latitude to Point geometries
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
gdf = GeoDataFrame(data, geometry=geometry)

# Load a world map from GeoPandas datasets
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot your data on the world map
ax = world.plot(figsize=(10, 6), color='lightgray', edgecolor='black')
gdf.plot(ax=ax, marker='o', color='red', markersize=5)
plt.title('Taxi Data Visualization')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
