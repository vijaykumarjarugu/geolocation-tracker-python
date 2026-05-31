import requests
import folium
import webbrowser

# Get location information from IP
response = requests.get("http://ip-api.com/json/")
data = response.json()

# Extract details
city = data['city']
region = data['regionName']
country = data['country']
lat = data['lat']
lon = data['lon']

print("\n===== GEOLOCATION TRACKER =====")
print(f"City     : {city}")
print(f"Region   : {region}")
print(f"Country  : {country}")
print(f"Latitude : {lat}")
print(f"Longitude: {lon}")

# Create map
map_obj = folium.Map(location=[lat, lon], zoom_start=12)

# Add marker
folium.Marker(
    [lat, lon],
    popup=f"{city}, {country}"
).add_to(map_obj)

# Save map
map_obj.save("location_map.html")

print("\nMap generated successfully!")

# Open map automatically
webbrowser.open("location_map.html")