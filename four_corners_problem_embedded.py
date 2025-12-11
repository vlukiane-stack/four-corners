# four_corners_problem_embedded.py
# Fully standalone version of the Four Corners problem definition.

class FourCornersProblem:
    def __init__(self, maze_text):
        self.maze = [list(line) for line in maze_text.strip().splitlines()]
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        self.start_pos = None

        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 'P':
                    self.start_pos = (x, y)

        corners_raw = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
        ]
        self.corners = [c for c in corners_raw if self.maze[c[1]][c[0]] != '*']
        self.start_state = (self.start_pos, tuple(False for _ in self.corners))

    def get_start_state(self):
        return self.start_state

    def is_goal_state(self, state):
        _, eaten = state
        return all(eaten)

    def get_successors(self, state):
        (x, y), eaten = state
        moves = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        successors = []
        for act, (dx, dy) in moves.items():
            nx, ny = x + dx, y + dy
            if self._is_valid(nx, ny):
                new_eaten = list(eaten)
                for i, c in enumerate(self.corners):
                    if (nx, ny) == c:
                        new_eaten[i] = True
                successors.append((((nx, ny), tuple(new_eaten)), act, 1))
        return successors

    def _is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.maze[y][x] != '*'
