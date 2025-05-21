from geofence import Geofence

class Phase1:
    def __init__(self, waypoints: list[tuple[float, float, float]], geofence: list[tuple[float, float]]):
        self.waypoints = waypoints
        self.geofence = geofence

    
