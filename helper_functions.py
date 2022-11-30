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


def is_in_bounding_box(bounding_coords: list, coord: tuple):
    """ This function calculates if coord is inside the geodesic rectangle or square formed by bounding_coords.
     Bounding_coords is a list in the form [A, B, C, D] where A must be the upper left vertex, B the upper right one,
      C the lower left and D lower right. The Box can't be """
    A_lat, A_lon = bounding_coords[0]
    B_lat, B_lon = bounding_coords[1]
    C_lat, C_lon = bounding_coords[2]
    D_lat, D_lon = bounding_coords[3]

    if A_lat != B_lat or C_lat != D_lat or A_lon != C_lon or B_lon != D_lon:
        raise ValueError(f'Bounding coords dont form a geodesic rectangle')

    x_lat, x_lon = coord[0], coord[1]
    if A_lon * B_lon < 0:
        B_lon = 360 + B_lon

    if C_lat < x_lat < A_lat and A_lon < x_lon < B_lon:
        return True
    else:
        return False
