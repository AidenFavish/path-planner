from geofence import Geofence
import matplotlib.pyplot as plt
import numpy as np
from phase1 import Phase1

EDGE_DIST = 0.05

class PathVisuals:
    def __init__(self, fence_veriticies:list[tuple[float, float]], waypoints:list[tuple[float, float, float]]):
        self.geofence = Geofence(fence_veriticies)
        self.waypoints = waypoints
        self.phase1 = Phase1(waypoints, fence_veriticies, EDGE_DIST)

    def _display_fence(self, ax, fence: Geofence, color:str="orange"):
        x, y = fence.polygon.exterior.xy
        ax.plot(x, y, 'b-', label='Geofence', color=color)
        ax.fill(x, y, color, alpha=0.3)

    def _display_points(self, ax, points: list[tuple[float, float, float]], color:str="green", line_color:str="green"):
        points = np.array(points)
        x_points, y_points = points[:, 0], points[:, 1]

        # Plot each segment separately to apply different colors
        for i in range(len(points) - 1):
            ax.plot(
                [x_points[i], x_points[i+1]], 
                [y_points[i], y_points[i+1]], 
                color=line_color, 
                linewidth=2
            )

        # Plot waypoints
        ax.scatter(x_points, y_points, color=color, marker='o', label="Waypoints")

        ax.legend()

    
    def display(self):
        fig, ax = plt.subplots()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Local map')
        ax.grid()

        self._display_fence(ax, self.geofence, "red")
        self._display_fence(ax, self.geofence.shrink(EDGE_DIST), "blue")

        self._display_points(ax, self.phase1.generate_fixed_trajectory())

        plt.show()

if __name__=="__main__":
    pv = PathVisuals([(0, 0), (4, 0), (4, 4), (2, 2), (0, 4)], [(0.5, 2.5, 0), (3, 2.5, 0), (3.5, 3.0, 0), (3.0, 2.7, 0.0)])
    pv.display()
