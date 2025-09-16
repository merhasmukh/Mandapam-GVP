import math

def calculate_distance(lat1, lng1, lat2, lng2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees) using the Haversine formula.
    
    Returns distance in meters.
    """
    # Convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lng1_rad = math.radians(lng1)
    lat2_rad = math.radians(lat2)
    lng2_rad = math.radians(lng2)
    
    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlng = lng2_rad - lng1_rad
    
    a = (math.sin(dlat/2)**2 + 
         math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlng/2)**2)
    
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of earth in meters
    earth_radius = 6371000
    
    # Calculate the result
    distance = earth_radius * c
    
    return distance