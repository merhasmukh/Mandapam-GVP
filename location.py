import math
from geopy.distance import geodesic
import folium
from IPython.display import HTML, display
import matplotlib.pyplot as plt

# Default location (Ahmedabad, India)
default_lat, default_lng = 23.042648586168678, 72.569132388004022

# User location (also in Ahmedabad, but different coordinates)
user_lat, user_lng = 23.042623641940949,72.569229770332726

def get_distance(lat1, lon1, lat2, lon2):
    R = 6371e3  # Earth's radius in meters
    φ1 = lat1 * math.pi/180
    φ2 = lat2 * math.pi/180
    Δφ = (lat2-lat1) * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180

    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2) + math.sin(Δλ/2) * math.sin(Δλ/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c  # Distance in meters
def calculate_geodesic_distance(coord1, coord2):
    """Calculate accurate distance using geodesic method"""
    return geodesic(coord1, coord2).km

def calculate_haversine_distance(coord1, coord2):
    """Calculate distance using Haversine formula"""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in kilometers
    r = 6371
    return c * r

def create_map(coord1, coord2, distance):
    """Create a map visualization with both locations"""
    # Calculate center point
    center_lat = (coord1[0] + coord2[0]) / 2
    center_lng = (coord1[1] + coord2[1]) / 2
    
    # Create map
    m = folium.Map(location=[center_lat, center_lng], zoom_start=12)
    
    # Add markers
    folium.Marker(
        coord1, 
        popup=f"Default Location<br>{coord1[0]}, {coord1[1]}",
        tooltip="Default Location",
        icon=folium.Icon(color="blue", icon="home")
    ).add_to(m)
    
    folium.Marker(
        coord2, 
        popup=f"User Location<br>{coord2[0]}, {coord2[1]}",
        tooltip="User Location",
        icon=folium.Icon(color="red", icon="user")
    ).add_to(m)
    
    # Add line between points
    folium.PolyLine(
        [coord1, coord2],
        color="green",
        weight=2.5,
        opacity=0.7,
        popup=f"Distance: {distance:.2f} km"
    ).add_to(m)
    
    return m

# Calculate distances
default_coord = (default_lat, default_lng)
user_coord = (user_lat, user_lng)

geodesic_dist = calculate_geodesic_distance(default_coord, user_coord)
haversine_dist = calculate_haversine_distance(default_coord, user_coord)
difference = abs(geodesic_dist - haversine_dist)

# Create visualization

# Display results
print("=" * 50)
print("DISTANCE CALCULATION RESULTS")
print("=" * 50)
print(f"Default Location: {default_lat}, {default_lng}")
print(f"User Location:    {user_lat}, {user_lng}")
print("-" * 50)
print(f"Geodesic Distance: {geodesic_dist:.4f} km (Most Accurate)")
print(f"Haversine Distance: {haversine_dist:.4f} km (Approximation)")
print(f"Difference: {difference:.6f} km")
print("=" * 50)


# Additional comparison for context
print("\nDISTANCE COMPARISON:")
print(f"{geodesic_dist:.2f} km is approximately:")
print(f"- {geodesic_dist * 1000:.0f} meters")
print(f"- {geodesic_dist * 0.621371:.2f} miles")
print(f"- {geodesic_dist / 1.852:.2f} nautical miles")
print(get_distance(default_lat, default_lng, user_lat, user_lng), "meters (Using basic formula)")
