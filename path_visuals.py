from geofence import Geofence
import matplotlib.pyplot as plt

class PathVisuals:
    def __init__(self, fence_veriticies:list[tuple[float, float]]):
        self.geofence = Geofence(fence_veriticies)

    def _display_fence(self, ax, fence: Geofence, color:str="orange"):
        x, y = fence.polygon.exterior.xy
        ax.plot(x, y, 'b-', label='Geofence', color=color)
        ax.fill(x, y, color, alpha=0.3)    
    
    def display(self):
        fig, ax = plt.subplots()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Local map')
        ax.grid()

        self._display_fence(ax, self.geofence, "red")
        self._display_fence(ax, self.geofence.shrink(0.5), "blue")

        plt.show()

if __name__=="__main__":
    pv = PathVisuals([(0, 0), (4, 0), (4, 4), (2, 2), (0, 4)])
    pv.display()
