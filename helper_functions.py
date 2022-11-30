import math


def calculate_distance(origin_lat: float, origin_lon: float, dest_lat: float, dest_lon: float):
    """ Calculate distance using Haversine formula.
    reference: https://stackoverflow.com/questions/44743075/calculate-the-distance-between-two-coordinates-with-python"""
    origin_lat, origin_lon, dest_lat, dest_lon = \
        map(math.radians, [origin_lat, origin_lon, dest_lat, dest_lon])
    d_lat = dest_lat - origin_lat
    d_lng = dest_lon - origin_lon
    temp = (
            math.sin(d_lat / 2) ** 2
            + math.cos(origin_lat)
            * math.cos(dest_lat)
            * math.sin(d_lng / 2) ** 2
    )
    return 6373.0 * (2 * math.atan2(math.sqrt(temp), math.sqrt(1 - temp)))
