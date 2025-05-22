from geofence import Geofence
from djikstras import Djikstras

class Phase1:
    def __init__(self, waypoints: list[tuple[float, float, float]], geofence: list[tuple[float, float]], shrink_edge_dist:float=0.5):
        self.waypoints = waypoints
        self.geofence_points = geofence
        self.shrink_edge_dist = shrink_edge_dist
        self.geofence = Geofence(self.geofence_points)
        self.shrunken_geofence = self.geofence.shrink(shrink_edge_dist)
    
    def generate_fixed_trajectory(self) -> list[tuple[float, float, float]]:
        tmp = {}
        for i in range(0, len(self.waypoints) - 1):
            p1 = self.waypoints[i][:-1]
            p2 = self.waypoints[i+1][:-1]
            if self.geofence.intersect(p1, p2):
                dj = Djikstras(self.shrunken_geofence.get_coords(), self.geofence)
                path = dj.get_path(p1, p2)
                tmp[i] = [(p[0], p[1], self.waypoints[i][-1]) for p in path]

        fixed_waypoints = []
        for i in range(0, len(self.waypoints)):
            if i in tmp:
                fixed_waypoints += tmp[i][:-1]
            else:
                fixed_waypoints.append(self.waypoints[i])

        return fixed_waypoints


