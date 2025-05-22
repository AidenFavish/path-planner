from geofence import Geofence
import matplotlib.pyplot as plt
import numpy as np
from phase1 import Phase1

EDGE_DIST = 15

class PathVisuals:
    def __init__(self, fence_veriticies:list[tuple[float, float]], waypoints:list[tuple[float, float, float]]):
        self.geofence = Geofence(fence_veriticies)
        self.waypoints = waypoints
        self.phase1 = Phase1(waypoints, fence_veriticies, EDGE_DIST)

    def _display_fence(self, ax, fence: Geofence, color:str="orange", name:str="Geofence"):
        x, y = fence.polygon.exterior.xy
        ax.plot(x, y, 'b-', label=name, color=color)
        ax.fill(x, y, color, alpha=0.3)

    def _display_points(self, ax, points: list[tuple[float, float, float]], color:str="green", line_color:str="green", name:str="Waypoints"):
        points = np.array(points)
        x_points, y_points = points[:, 0], points[:, 1]

        # Plot each segment separately to apply different colors
        for i in range(len(points) - 1):
            ax.plot(
                [x_points[i], x_points[i+1]], 
                [y_points[i], y_points[i+1]], 
                color=line_color, 
                linewidth=2,
                alpha=0.5
            )

        # Plot waypoints
        ax.scatter(x_points, y_points, color=color, marker='o', label=name)

        ax.legend()

    
    def display(self):
        fig, ax = plt.subplots()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Local map')
        ax.grid()

        self._display_fence(ax, self.geofence, "red")
        self._display_fence(ax, self.geofence.shrink(EDGE_DIST), "yellow", "Inset Geofence")

        self._display_points(ax, self.phase1.waypoints, "blue", "blue", "Original Lap")
        self._display_points(ax, self.phase1.generate_fixed_trajectory(), name="Adjusted Lap")

        plt.show()

if __name__=="__main__":
    geofence = [[216, 416], [200, 174], [779, 175], [812, 599], [726, 606], [705, 271], [276, 259], [276, 325], [650, 326], [657, 590], [580, 590], [582, 391], [440, 396], [437, 587], [263, 584]]
    pv = PathVisuals(geofence, [(609, 529, 0), (774, 526, 0)])
    pv.display()
