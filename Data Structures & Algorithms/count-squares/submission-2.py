class CountSquares:

    def __init__(self):
        self.points: Counter[tuple[int, int]] = Counter()
        self.xs_at_y: defaultdict[int, Counter[int]] = defaultdict(Counter)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.xs_at_y[y][x] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        res = 0
        for new_x, cnt in self.xs_at_y.get(y, {}).items():
            if new_x == x:
                continue
            side = abs(new_x - x)
            for k in (y + side, y - side):
                res += cnt * self.points[(x, k)] * self.points[(new_x, k)]
        return res