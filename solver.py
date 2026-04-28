from typing import Dict, List, Optional
from models import Course, Section, Metrics
from constraints import not_conflicting_with_selected_sections

class Solver:
    def __init__(self, courses: List[Course]):
        self.courses = courses
        self.metrics = Metrics()
    def solve(self):
        assignment = {}
        return self.backtrack(assignment)
    
    #[Backtracking] For chooding unassigned courses from the list of courses
    def choose_unassigned_course(self, assignment: Dict[str, Section]):
        for course in self.courses:
            if course.course_id not in assignment:
                return course
        raise ValueError("No unassigned courses found")
    
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