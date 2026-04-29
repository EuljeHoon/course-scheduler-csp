from models import Course, Section


def get_forced_backtracking_dataset():
    return [
        Course("C1", "Course 1", 4, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
        ]),
        Course("C2", "Course 1", 4, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
        ]),
        Course("C3", "Course 2", 3, [
            Section("C2-B1", ("Mon", "Wed",), 540, 615),
            Section("C2-B2", ("Mon", "Wed",), 960, 1035),
            Section("C2-B3", ("Tue", "Thu",), 870, 945),
            Section("C2-B4", ("Tue", "Thu",), 1020, 1095),
        ]),
        Course("C4", "Course 1", 3, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
        ]),
        Course("C5", "Course 1", 4, [
            Section("C1-B3", ("Tue", "Thu",), 840, 915),

        ]),
        Course("C6", "Course 1", 4, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
            Section("C1-B3", ("Tue", "Thu",), 960, 1035),

        ]),
        Course("C7", "Course 1", 3, [
            Section("C1-B3", ("Tue", "Thu",), 840, 915),

        ]),
        Course("C8", "Course 1", 4, [
            Section("C1-B3", ("Mon", "Wed",), 540, 615),
        ]),
        Course("C9", "Course 1", 3, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
            Section("C1-B3", ("Tue", "Thu",), 840, 915),

        ]),
        Course("C10", "Course 1", 4, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
            Section("C1-B2", ("Mon", "Wed",), 960, 1035),
            Section("C1-B3", ("Tue", "Thu",), 540, 615),
            Section("C1-B4", ("Tue", "Thu",), 960, 1035),
            Section("C1-B5", ("Wed", "Fri",), 900, 975),
        ]),
        Course("C11", "Course 2", 3, [
            Section("C2-B1", ("Mon", "Wed",), 540, 615),
            Section("C2-B2", ("Mon", "Wed",), 960, 1035),
            Section("C2-B3", ("Tue", "Thu",), 870, 945),
            Section("C2-B4", ("Tue", "Thu",), 1020, 1095),
        ]),
        Course("C12", "Course 3", 4, [
            Section("C3-B1", ("Mon", "Wed", "Fri",), 540, 590),
            Section("C3-B2", ("Mon", "Wed", "Fri",), 780, 830),
        ]),
        Course("C13", "Course 4", 3, [
            Section("C4-B1", ("Mon", "Wed", "Fri",), 600, 650),
        ]),
        Course("C14", "Course 5", 3, [
            Section("C5-B1", ("Wed", "Fri",), 660, 735),
            Section("C5-B2", ("Wed", "Fri",), 930, 1020),
        ]),
        Course("C15", "Course 1", 4, [
            Section("C1-B1", ("Mon","Wed",), 540, 615),
            Section("C1-B2", ("Mon", "Wed",), 960, 1035),
            Section("C1-B3", ("Tue", "Thu",), 540, 615),
            Section("C1-B4", ("Tue", "Thu",), 960, 1035),
            Section("C1-B5", ("Wed", "Fri",), 900, 975),
        ]),
    ]