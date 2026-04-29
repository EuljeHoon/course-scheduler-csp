import time
import csv
from course_data import get_forced_backtracking_dataset_5, get_forced_backtracking_dataset_2
from solver import Solver


def run_experiments():
    modes = ["basic", "mrv_degree", "mrv_degree_mac"]

    results = []

    for mode in modes:
        courses = get_forced_backtracking_dataset_2()

        solver = Solver(courses, mode=mode)

        start = time.time()
        solution = solver.solve()
        end = time.time()

        solver.metrics.runtime = end - start

        results.append({
            "courses": len(courses),
            "mode": mode,
            "runtime": solver.metrics.runtime,
            "nodes_visited": solver.metrics.nodes_visited,
            "backtracks": solver.metrics.backtracks,
            "solution_found": solution is not None
        })

    return results


def save_results(results, filename="results.csv"):
    with open(filename, "w", newline="") as f:
        fieldnames = [
            "courses",
            "mode",
            "runtime",
            "nodes_visited",
            "backtracks",
            "solution_found"
        ]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    results = run_experiments()

    for row in results:
        print(row)

    save_results(results)