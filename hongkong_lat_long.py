import pandas as pd
from hk1980 import HK80

# Read the file 
input_file = 'C:/Users/Linus/Documents/Python Scripts/HK_input.csv' 
df = pd.read_csv(input_file)

# Function to convert northing & easting values to latitude & longitude
def convert_to_wgs84(row):
    hku = HK80(northing=row['northing'], easting=row['easting']).to_wgs84()
    return pd.Series({'latitude': hku.latitude, 'longitude': hku.longitude})

# Apply the conversion function to each row
df[['latitude', 'longitude']] = df.apply(convert_to_wgs84, axis=1)

# Export the final file 
output_file = 'HK_output.csv'
df.to_csv(output_file, index=False)