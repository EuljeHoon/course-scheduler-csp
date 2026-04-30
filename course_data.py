from models import Course, Section


def get_forced_backtracking_dataset():
    return [
        Course("C1", "Internet Programming", 3, [
            Section("C1-B1", ("Mon","Wed",), 675, 750),
        ]),
        Course("C2", "Computer Architecture", 3, [
            Section("C1-B1", ("Tue","Thu",), 675, 750),
        ]),
        Course("C3", "Computer Architecture Lab", 1, [
            Section("C2-B1", ("Fri",), 610, 660),
            Section("C2-B2", ("Fri",), 675, 725),
            Section("C2-B3", ("Fri",), 740, 790),
        ]),
        Course("C4", "Software Development Process", 3, [
            Section("C1-B1", ("Tue","Thu",), 585, 660),
        ]),
        Course("C5", "Software Development Process Lab", 1, [
            Section("C1-B1", ("Fri",), 610, 660),
            Section("C1-B2", ("Fri",), 675, 735),
            Section("C1-B3", ("Fri",), 750, 800),
            Section("C1-B4", ("Fri",), 815, 865),

        ]),
        Course("C6", "Introduction to Artificial Intelligence", 3, [
            Section("C1-B1", ("Mon","Wed",), 780, 855),
            Section("C1-B2", ("Mon","Wed",), 960, 1035),
        ]),
        Course("C7", "Introduction to Artificial Intelligence Lab", 1, [
            Section("C1-B1", ("Fri",), 675, 725),
            Section("C1-B2", ("Fri",), 740, 790),
            Section("C1-B3", ("Fri",), 805, 855),
            Section("C1-B4", ("Fri",), 870, 920),
        ]),
        Course("C8", "Human Biology", 3, [
            Section("C1-B1", ("Mon","Wed","Fri"), 740, 790),
            Section("C1-B2", ("Mon","Wed","Fri"), 805, 855),
        ]),
        Course("C9", "Human Biology Lab", 1, [
            Section("C1-B1", ("Thu"), 740, 855),
            Section("C1-B2", ("Thu"), 870, 985),
            Section("C1-B3", ("Thu"), 1000, 1115),
            Section("C1-B4", ("Wed"), 480, 595),
            Section("C1-B5", ("Wed"), 610, 725),
            Section("C1-B6", ("Wed"), 870, 985),
            Section("C1-B7", ("Wed"), 1000, 1115),
        ]),
        Course("C10", "Automata Theory", 3, [
            Section("C1-B1", ("Tue","Thu",), 495, 570),
        ]),
        Course("C11", "Automata Theory Discussion", 1, [
            Section("C2-B1", ("Fri",), 740, 790),
            Section("C2-B2", ("Fri",), 805, 855),
            Section("C2-B3", ("Fri",), 870, 920),
        ]),
        Course("C12", "User Interface Design and Prototyping", 3, [
            Section("C1-B1", ("Mon","Wed",), 585, 660),
        ]),
        Course("C13", "User Interface Design and Prototyping Discussion", 1, [
            Section("C2-B1", ("Thu",), 545, 595),
            Section("C2-B2", ("Thu",), 610, 660),
            Section("C2-B3", ("Thu",), 675, 725),
        ]),
    ]