from models import Course, Section


def get_forced_backtracking_dataset_5():
    """
    A stronger fixed dataset (5 courses) designed to force deeper backtracking.
    - C1~C4 have multiple early BAD options plus one SAFE option.
    - C5 has a tiny domain:
      * one section that conflicts with most early BAD patterns
      * one SAFE section that only fits when earlier choices move away from traps
    """
    return [
        Course("C1", "Course 1", 3, [
            Section("C1-B1", ("Mon",), 540, 620),
            Section("C1-B2", ("Tue",), 555, 635),
            Section("C1-B3", ("Wed",), 570, 650),
            Section("C1-B4", ("Thu",), 585, 665),
            Section("C1-B5", ("Fri",), 600, 680),
            Section("C1-SAFE", ("Mon",), 900, 960),
        ]),
        Course("C2", "Course 2", 3, [
            Section("C2-B1", ("Tue",), 545, 625),
            Section("C2-B2", ("Wed",), 560, 640),
            Section("C2-B3", ("Thu",), 575, 655),
            Section("C2-B4", ("Fri",), 590, 670),
            Section("C2-B5", ("Mon",), 605, 685),
            Section("C2-SAFE", ("Tue",), 900, 960),
        ]),
        Course("C3", "Course 3", 3, [
            Section("C3-B1", ("Wed",), 550, 630),
            Section("C3-B2", ("Thu",), 565, 645),
            Section("C3-B3", ("Fri",), 580, 660),
            Section("C3-B4", ("Mon",), 595, 675),
            Section("C3-B5", ("Tue",), 610, 690),
            Section("C3-SAFE", ("Wed",), 960, 1020),
        ]),
        Course("C4", "Course 4", 3, [
            Section("C4-B1", ("Thu",), 555, 635),
            Section("C4-B2", ("Fri",), 570, 650),
            Section("C4-B3", ("Mon",), 585, 665),
            Section("C4-B4", ("Tue",), 600, 680),
            Section("C4-B5", ("Wed",), 615, 695),
            Section("C4-SAFE", ("Thu",), 960, 1020),
        ]),
        Course("C5", "Course 5", 3, [
            # Both options are traps for the default early path:
            # C1-B1/C2-B1/... make C5 impossible unless earlier assignments change.
            Section("C5-T1", ("Mon",), 560, 610),
            Section("C5-T2", ("Tue",), 560, 610),
        ]),
    ]

def get_forced_backtracking_dataset_2():
    return [
        Course("C1", "Course 1", 3, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
            Section("C1-B2", ("Mon", "Wed",), 960, 1035),
            Section("C1-B3", ("Tue", "Thu",), 540, 615),
            Section("C1-B4", ("Tue", "Thu",), 960, 1035),
            Section("C1-B5", ("Wed", "Fri",), 900, 975),
        ]),
        Course("C2", "Course 2", 3, [
            Section("C2-B1", ("Mon", "Wed",), 540, 615),
            Section("C2-B2", ("Mon", "Wed",), 960, 1035),
            Section("C2-B3", ("Tue", "Thu",), 870, 945),
            Section("C2-B4", ("Tue", "Thu",), 1020, 1095),
        ]),
        Course("C3", "Course 3", 3, [
            Section("C3-B1", ("Mon", "Wed", "Fri",), 540, 590),
            Section("C3-B2", ("Mon", "Wed", "Fri",), 780, 830),
        ]),
        Course("C4", "Course 4", 3, [
            Section("C4-B1", ("Mon", "Wed", "Fri",), 600, 650),
        ]),
        Course("C5", "Course 5", 3, [
            Section("C5-B1", ("Wed", "Fri",), 660, 735),
            Section("C5-B2", ("Wed", "Fri",), 930, 1020),
        ]),
    ]