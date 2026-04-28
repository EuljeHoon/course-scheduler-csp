from typing import Dict, List
from models import Course, Section, Metrics
from constraints import not_conflicting_with_selected_sections, time_conflict

class Solver:
    def __init__(self, courses: List[Course], mode: str = "basic"):
        self.courses = courses
        self.mode = mode
        self.metrics = Metrics()
    def solve(self):
        assignment = {}
        return self.backtrack(assignment)
    
    #Backtracking
    def backtrack(self, assignment: Dict[str, Section]):
        #When all the courses are assigned, success
        if len(assignment) == len(self.courses):
            return assignment.copy()
        
        self.metrics.nodes_visited += 1
        
        #choose first unassigned course by calling choose_unassigned_course
        course = self.choose_unassigned_course(assignment)
        #try all the sections of the chosen course
        for section in course.sections:
            if not_conflicting_with_selected_sections(section, assignment):
                assignment[course.course_id] = section
                result = self.backtrack(assignment)
                if result is not None:
                    return result

                #Remove the sectioin from the assignment if it fails
                del assignment[course.course_id]
        self.metrics.backtracks += 1
        return None
    
    def choose_unassigned_course(self, assignment: Dict[str, Section]):
        if self.mode == "basic":
            return self.choose_unassigned_course_basic(assignment)
        if self.mode == "mrv_degree":
            return self.choose_unassigned_course_mrv_degree(assignment)
        #Need Constraint Propagation for other modes
        raise ValueError("No unassigned courses found")

    #helper to get unassigned courses
    def get_unassigned_courses(self, assignment: Dict[str, Section]) -> List[Course]:
        unassigned_courses = []

        for course in self.courses:
            if course.course_id not in assignment:
                unassigned_courses.append(course)

        return unassigned_courses

    #[Backtracking] For chooding unassigned courses from the list of courses
    def choose_unassigned_course_basic(self, assignment: Dict[str, Section]):
        unassigned = self.get_unassigned_courses(assignment)
        return unassigned[0]
    
    #[Heuristics (MRV + Degree Heuristic)]
    def choose_unassigned_course_mrv_degree(self, assignment: Dict[str, Section]):
        unassigned = self.get_unassigned_courses(assignment)

        #get the min count of sections for the unassigned courses and choose the course
        min_section_count = float('inf')
        candidates = []

        for i in unassigned:
            section_count = self.get_section_count(i, assignment)
            if section_count < min_section_count:
                min_section_count = section_count
                candidates = [i]
            elif section_count == min_section_count:
                candidates.append(i)
        
        #if length of candidate is 1, return the course =
        if len(candidates) == 1:
            return candidates[0]
        #if not, apply degree heuristic
        result = None
        maximum = -1
        for i in candidates:
            degree = self.get_degree(i, unassigned)
            if degree > maximum:
                maximum = degree
                result = i
        return result
    
    def get_section_count(self, course: Course, assignment: Dict[str, Section]):
        count = 0
        for i in course.sections:
            if not_conflicting_with_selected_sections(i, assignment):
                count += 1
        return count
    
    #helper to get the degree of a course
    def get_degree(self, course: Course, unassigned: List[Course]):
        degree = 0
        for i in unassigned:
            if i.course_id == course.course_id:
                continue
            if self.number_of_conflicts(course, i):
                degree += 1
        return degree
    def number_of_conflicts(self, c1: Course, c2: Course):
        for i in c1.sections:
            for j in c2.sections:
                if time_conflict(i, j):
                    return True
        return False

    #[Constraints Propagation (MAC / AC-3)]