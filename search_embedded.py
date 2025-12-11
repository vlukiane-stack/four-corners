# search_embedded.py
from collections import deque
import heapq

def reconstruct_path(parent, goal_state):
    path = []
    cur = goal_state
    while True:
        prev, act = parent[cur]
        if prev is None:
            break
        path.append(act)
        cur = prev
    path.reverse()
    return path

def breadth_first_search(problem):
    start = problem.get_start_state()
    parent = {start: (None, None)}
    frontier = deque([start])
    nodes = 0
    while frontier:
        s = frontier.popleft()
        nodes += 1
        if problem.is_goal_state(s):
            return reconstruct_path(parent, s), nodes
        for nxt, act, _ in problem.get_successors(s):
            if nxt not in parent:
                parent[nxt] = (s, act)
                frontier.append(nxt)
    return None, nodes

def uniform_cost_search(problem):
    start = problem.get_start_state()
    parent = {start: (None, None)}
    g = {start: 0}
    pq = [(0, start)]
    nodes = 0
    while pq:
        cost, s = heapq.heappop(pq)
        nodes += 1
        if problem.is_goal_state(s):
            return reconstruct_path(parent, s), nodes
        for nxt, act, step in problem.get_successors(s):
            nc = cost + step
            if nxt not in g or nc < g[nxt]:
                g[nxt] = nc
                parent[nxt] = (s, act)
                heapq.heappush(pq, (nc, nxt))
    return None, nodes

def manhattan(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)

def four_corners_heuristic(state, problem):
    (x, y), eaten = state
    pos = (x, y)
    h = 0
    for flag, corner in zip(eaten, problem.corners):
        if not flag:
            h += manhattan(pos, corner)
    return h

def a_star_search(problem, heuristic):
    start = problem.get_start_state()
    parent = {start: (None, None)}
    g = {start: 0}
    pq = [(0, start)]
    nodes = 0
    while pq:
        f, s = heapq.heappop(pq)
        nodes += 1
        if problem.is_goal_state(s):
            return reconstruct_path(parent, s), nodes
        for nxt, act, step in problem.get_successors(s):
            ng = g[s] + step
            if nxt not in g or ng < g[nxt]:
                g[nxt] = ng
                parent[nxt] = (s, act)
                h = heuristic(nxt, problem)
                heapq.heappush(pq, (ng + h, nxt))
    return None, nodes
