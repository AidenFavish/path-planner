from dataclasses import dataclass

class Djikstras:
    @dataclass
    class NodeInfo:
        shortest_dist: float | None
        shortest_node: tuple[float, float] | None

    def __init__(self, fence_points: list[tuple[float, float]]):
        self.fence_points = fence_points
        self.d_table: dict[tuple[float, float], Djikstras.NodeInfo] = {}

        for point in self.fence_points:
            self.d_table[point] = Djikstras.NodeInfo(None, None)

    def get_path(self, start:tuple[float, float], end: tuple[float, float]) -> list[tuple[float, float]]:
        self.start_node = start
        self.end_node = end
        self.d_table[start] = Djikstras.NodeInfo(0.0, None)
        self.d_table[end] = Djikstras.NodeInfo(None, None)
        self._populate_table()
        return self._shortest_path()

    @staticmethod
    def _dist(start:tuple[float, float], end: tuple[float, float]) -> float:
        return ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5
    
    def _populate_table(self):
        nodes = list(self.d_table.keys())
        nodes.remove(self.start_node)
        nodes.insert(0, self.start_node)

        for node in nodes:
            past_dist = self.d_table[node].shortest_dist
            for neighbor in self.d_table:
                if neighbor is not node:
                    dist = Djikstras._dist(node, neighbor) + past_dist
                    if self.d_table[neighbor].shortest_node is None or dist < self.d_table[neighbor].shortest_dist:
                        self.d_table[neighbor] = Djikstras.NodeInfo(dist, node)

    def _shortest_path(self) -> list[tuple[float, float]]:
        tmp = self.end_node
        path = []
        print("entering")
        ctr = len(self.d_table)
        while tmp != self.start_node and ctr > 0:
            ctr -= 1
            print(path)
            print(self.d_table)
            print(self.start_node)
            path.append(tmp)
            tmp = self.d_table[tmp].shortest_node
        path.append(tmp)
        
        path.reverse()
        return path
