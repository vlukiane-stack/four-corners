# run_four_corners_embedded.py
import time
from four_corners_problem_embedded import FourCornersProblem
import search_embedded as search

# Embedded maze data (from your uploaded text files)
tinyCorners = """
*********
*P......*
*.*.****.
*.*....*.
*.****.*.
*......*.
*********
"""

mediumCorners = """
**************************
*P.......................*
*.*.********************.*
*.*.....................*.
*.*.********************.*
*.*.....................*.
**************************
"""

smallSearch = """
*******
*P....*
*.*.***
*.*...*
*.*.***
*.*...*
*******
"""

def run_maze(name, maze_text):
    problem = FourCornersProblem(maze_text)
    print("====================================")
    print("Maze:", name)

    t0 = time.time()
    bfs_path, bfs_nodes = search.breadth_first_search(problem)
    t1 = time.time()
    print("BFS  -> cost:", len(bfs_path), "nodes:", bfs_nodes, "time(s):", round(t1 - t0, 5))

    t0 = time.time()
    ucs_path, ucs_nodes = search.uniform_cost_search(problem)
    t1 = time.time()
    print("UCS  -> cost:", len(ucs_path), "nodes:", ucs_nodes, "time(s):", round(t1 - t0, 5))

    t0 = time.time()
    astar_path, astar_nodes = search.a_star_search(problem, lambda s, p=problem: search.four_corners_heuristic(s, p))
    t1 = time.time()
    print("A*   -> cost:", len(astar_path), "nodes:", astar_nodes, "time(s):", round(t1 - t0, 5))

if __name__ == "__main__":
    run_maze("tinyCorners", tinyCorners)
    run_maze("mediumCorners", mediumCorners)
    run_maze("smallSearch", smallSearch)
