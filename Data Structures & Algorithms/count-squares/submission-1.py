class CountSquares:

    def __init__(self):
        self.points: Dict[int, int] = defaultdict(int)
        self.xs_at_y: Dict[int, List[int]] = defaultdict(list)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[1001 * x + y] += 1
        self.xs_at_y[y].append(x)

    def count(self, point: List[int]) -> int:
        x,y = point
        
        res = 0
        
        for new_x in self.xs_at_y.get(y, []):
            if new_x == x:
                continue

            side = abs(new_x - x)
            new_y1 = y + side
            new_y2 = y - side

            for k in [new_y1, new_y2]:
                count1 = self.points.get(1001 * x + k, 0)
                count2 = self.points.get(1001 * new_x + k, 0)
                res += count1 * count2

        return res