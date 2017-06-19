#Singapore Taxi Data Analysis

## Taxi data source
Singapore LTA provides an API to query the locations of all the taxis on the roads. This returns a list of lat long pairs for all taxis that are on the road at that instant and not hired/busy. This can be mapped to a simple grid to get area wise avialability or can be plotted on the map as it is.

The data is updated every 30 seconds and the recommended usage is to invoke the API every minute.

## Data processing
We assume the bounds of Singapore as lat and long bounds from Google Maps and for a given grid height, we calculate the width and map all the locations of the taxos to the grid. This data is then stored to SQLite DB in the form of Date-Time-X-Y-Value.

We can fetch the data for any date, time or both and we can use that to analyze the availability for that grid.