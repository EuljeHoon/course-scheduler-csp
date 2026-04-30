# Course Scheduler (CSP)

Experimental code for a **constraint satisfaction problem (CSP)**. The algorithm tries to build a **timetable that includes every course in the dataset**: each course is a variable, each of its sections is a possible value, and the solver picks **one section per course** so that **no two chosen sections overlap in time**. (If no such full assignment exists, it returns failure.) It solves this with **backtracking** and compares **heuristics** and **constraint propagation (MAC / AC-3)**.

---

## Files

| File | Role |
|------|------|
| **`models.py`** | Dataclasses: `Section` (days, start, end), `Course` (id, name, credits, sections), and `Metrics` for experiments. |
| **`constraints.py`** | `time_conflict` (two sections overlap on a shared day), `not_conflicting_with_selected_sections` (new section vs current assignment). |
| **`course_data.py`** | `get_forced_backtracking_dataset()` — sample courses/sections designed to stress backtracking. |
| **`solver.py`** | `Solver`: backtracking with modes — plain, MRV+degree, or combined with MAC (AC-3). |
| **`experiment.py`** | Runs all three modes on the same data; prints runtime, nodes visited, backtracks; saves **`results.csv`**. |

---

## `solver.py` — `Solver` class and methods

**`__init__(self, courses, mode="basic")`** — Stores the course list and mode; initializes `Metrics()`.

| Method | Role |
|--------|------|
| **`solve(self)`** | If `mode` is `"mrv_degree_mac"`, builds per-course domain dicts and calls `backtrack_mac`. Otherwise calls `backtrack`. Returns a `{course_id: Section}` assignment on success, or `None`. |
| **`backtrack(self, assignment)`** | If every course is assigned, returns the solution. Otherwise picks an unassigned course, tries non-conflicting sections, recurses. If all branches fail, increments backtrack count and returns `None`. |
| **`backtrack_mac(self, assignment, domains)`** | MAC-style backtracking: copies domains, restricts current course to chosen section, runs `ac3`; if `ac3` fails, undoes. |
| **`choose_unassigned_course(self, assignment)`** | Dispatches to `choose_unassigned_course_basic` or `choose_unassigned_course_mrv_degree` by mode. (`mrv_degree_mac` uses `choose_unassigned_course_mrv_degree_mac` inside `backtrack_mac` only.) |
| **`choose_unassigned_course_mrv_degree_mac(self, assignment, domains)`** | Among unassigned courses, picks smallest **domain size (MRV)**; ties broken by **degree** (more potential conflicts with other unassigned courses). |
| **`get_unassigned_courses(self, assignment)`** | Returns `Course` objects not yet in `assignment`. |
| **`choose_unassigned_course_basic(self, assignment)`** | Takes the **first** unassigned course (fixed order). |
| **`choose_unassigned_course_mrv_degree(self, assignment)`** | **MRV**: fewest sections still consistent with the assignment; ties broken with **degree** heuristic. |
| **`get_section_count(self, course, assignment)`** | Counts sections of `course` that do not time-conflict with any assigned section (for MRV). |
| **`get_degree(self, course, unassigned)`** | Counts other unassigned courses that can time-conflict with `course` via **some** section pair. |
| **`number_of_conflicts(self, c1, c2)`** | `True` if any section of `c1` time-conflicts with any section of `c2`. |
| **`ac3(self, domains, assignment)`** | AC-3: queue of arcs `(i,j)`, `revise` to shrink domains; returns `False` if any domain becomes empty. |
| **`revise(self, course_one, course_two, domains)`** | Removes values from `course_one`’s domain that conflict with **every** value in `course_two`’s domain. Returns whether the domain changed. |

---

## How to run

**Python 3** only; no third-party packages.

### Experiment script (recommended)

Runs `basic`, `mrv_degree`, and `mrv_degree_mac` in order, prints rows to the terminal, and writes **`results.csv`**.

```bash
cd /path/to/course-scheduler-csp
python3 experiment.py
```

### Using the solver from another script

```python
from course_data import get_forced_backtracking_dataset
from solver import Solver

courses = get_forced_backtracking_dataset()
solver = Solver(courses, mode="mrv_degree")  # or "basic", "mrv_degree_mac"
solution = solver.solve()
print(solution)
print(solver.metrics.nodes_visited, solver.metrics.backtracks)
```

To record wall-clock time like `experiment.py`, wrap `solve()` with `time.time()` and set `solver.metrics.runtime`.

---

## Solver `mode` summary

- **`basic`**: unassigned variable order = list order; plain backtracking.
- **`mrv_degree`**: MRV (fewest feasible sections) + degree tie-break for variable order.
- **`mrv_degree_mac`**: similar variable ordering with explicit domains; **`ac3`** after each step for arc consistency (MAC).
