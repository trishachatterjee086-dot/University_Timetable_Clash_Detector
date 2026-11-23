"""
University Timetable Clash Detector
-----------------------------------
Project: University Timetable Clash Detector Using Python

This program uses only fundamental Python features:
lists, tuples, dictionaries, strings, loops, conditions,
functions, lambda functions, and the datetime module.

No pandas, NumPy, database, Flask/Django, AI/ML, or external packages.
"""

from datetime import datetime


# ============================================================
# MASTER DATA
# ============================================================

faculty_list = [
    "Dr. Sharma",
    "Dr. Mehta",
    "Dr. Roy",
    "Dr. Sen",
    "Dr. Das",
    "Dr. Kapoor"
]

room_list = [
    "Room 101",
    "Room 102",
    "Room 103",
    "Room 104",
    "Room 105"
]

# Faculty availability:
# Faculty -> Day -> Available periods
faculty_availability = {
    "Dr. Sharma": {
        "Monday": [1, 2, 3, 4, 5],
        "Tuesday": [1, 3, 4, 5],
        "Wednesday": [1, 2, 3, 4],
        "Thursday": [1, 2, 3, 4, 5],
        "Friday": [1, 2, 3, 5]
    },
    "Dr. Mehta": {
        "Monday": [1, 2, 4, 5],
        "Tuesday": [1, 2, 3, 4, 5],
        "Wednesday": [1, 3, 4, 5],
        "Thursday": [1, 2, 4, 5],
        "Friday": [1, 2, 3, 4]
    },
    "Dr. Roy": {
        "Monday": [1, 2, 3, 5],
        "Tuesday": [1, 2, 3, 4],
        "Wednesday": [1, 2, 4, 5],
        "Thursday": [1, 3, 4, 5],
        "Friday": [1, 2, 3, 4, 5]
    },
    "Dr. Sen": {
        "Monday": [1, 2, 3, 4],
        "Tuesday": [1, 2, 3, 5],
        "Wednesday": [1, 2, 3, 4, 5],
        "Thursday": [1, 2, 3, 4],
        "Friday": [2, 3, 4, 5]
    },
    "Dr. Das": {
        "Monday": [1, 2, 4, 5],
        "Tuesday": [1, 2, 3, 4],
        "Wednesday": [1, 2, 3, 5],
        "Thursday": [1, 2, 3, 4, 5],
        "Friday": [1, 3, 4, 5]
    },
    "Dr. Kapoor": {
        "Monday": [1, 3, 4, 5],
        "Tuesday": [1, 2, 3, 4],
        "Wednesday": [1, 2, 3, 4],
        "Thursday": [2, 3, 4, 5],
        "Friday": [1, 2, 3, 4, 5]
    }
}

# Room availability:
# Room -> Day -> Available periods
room_availability = {
    "Room 101": {
        "Monday": [1, 2, 3, 4, 5],
        "Tuesday": [1, 2, 3, 4],
        "Wednesday": [1, 2, 3, 4, 5],
        "Thursday": [1, 2, 3, 4, 5],
        "Friday": [1, 2, 3, 4]
    },
    "Room 102": {
        "Monday": [1, 2, 4, 5],
        "Tuesday": [1, 2, 3, 5],
        "Wednesday": [1, 2, 3, 4, 5],
        "Thursday": [1, 2, 3, 4],
        "Friday": [1, 2, 3, 4, 5]
    },
    "Room 103": {
        "Monday": [1, 2, 3, 5],
        "Tuesday": [1, 2, 3, 4, 5],
        "Wednesday": [1, 3, 4, 5],
        "Thursday": [1, 2, 3, 5],
        "Friday": [1, 2, 3, 4]
    },
    "Room 104": {
        "Monday": [1, 2, 4, 5],
        "Tuesday": [1, 2, 3, 4],
        "Wednesday": [1, 2, 3, 4, 5],
        "Thursday": [1, 2, 4, 5],
        "Friday": [1, 2, 3, 4, 5]
    },
    "Room 105": {
        "Monday": [1, 3, 4, 5],
        "Tuesday": [1, 2, 3, 4, 5],
        "Wednesday": [1, 2, 3, 4],
        "Thursday": [1, 2, 3, 4, 5],
        "Friday": [1, 2, 4, 5]
    }
}


# ============================================================
# 30 SAMPLE TIMETABLE ENTRIES
# ============================================================
#
# Intentional problems included:
# 1. Faculty clash
# 2. Room clash
# 3. Section clash
# 4. Faculty availability clash
# 5. Room availability clash
# 6. Duplicate entry
# 7. Invalid room
# 8. Invalid faculty
#
# Some entries intentionally create more than one problem.

timetable = [
    # ---------------- B.Com Semester 4 ----------------
    {
        "day": "Monday", "period": 1,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC401", "subject_name": "Corporate Accounting",
        "faculty": "Dr. Sharma", "room": "Room 101"
    },
    {
        "day": "Monday", "period": 2,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC402", "subject_name": "Financial Management",
        "faculty": "Dr. Sharma", "room": "Room 102"
    },
    {
        "day": "Monday", "period": 2,
        "programme": "B.Com", "semester": 4, "section": "B",
        "subject_code": "BC403", "subject_name": "Business Law",
        "faculty": "Dr. Sharma", "room": "Room 103"
    },  # FACULTY CLASH with entry 2
    {
        "day": "Monday", "period": 3,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC404", "subject_name": "Business Economics",
        "faculty": "Dr. Mehta", "room": "Room 101"
    },
    {
        "day": "Monday", "period": 4,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC405", "subject_name": "Business Statistics",
        "faculty": "Dr. Roy", "room": "Room 104"
    },
    {
        "day": "Tuesday", "period": 1,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC406", "subject_name": "Cost Accounting",
        "faculty": "Dr. Sen", "room": "Room 105"
    },

    # ---------------- BBA Semester 2 ----------------
    {
        "day": "Monday", "period": 3,
        "programme": "BBA", "semester": 2, "section": "B",
        "subject_code": "BA201", "subject_name": "Business Economics",
        "faculty": "Dr. Das", "room": "Room 101"
    },  # ROOM CLASH with entry 4
    {
        "day": "Tuesday", "period": 2,
        "programme": "BBA", "semester": 2, "section": "A",
        "subject_code": "BA202", "subject_name": "Principles of Management",
        "faculty": "Dr. Mehta", "room": "Room 102"
    },
    {
        "day": "Tuesday", "period": 3,
        "programme": "BBA", "semester": 2, "section": "A",
        "subject_code": "BA203", "subject_name": "Marketing Management",
        "faculty": "Dr. Roy", "room": "Room 103"
    },
    {
        "day": "Tuesday", "period": 4,
        "programme": "BBA", "semester": 2, "section": "A",
        "subject_code": "BA204", "subject_name": "Human Resource Management",
        "faculty": "Dr. Sen", "room": "Room 104"
    },
    {
        "day": "Wednesday", "period": 1,
        "programme": "BBA", "semester": 2, "section": "B",
        "subject_code": "BA205", "subject_name": "Business Communication",
        "faculty": "Dr. Kapoor", "room": "Room 105"
    },

    # ---------------- BCA Semester 2 ----------------
    {
        "day": "Monday", "period": 4,
        "programme": "BCA", "semester": 2, "section": "A",
        "subject_code": "CA201", "subject_name": "Python Programming",
        "faculty": "Dr. Kapoor", "room": "Room 102"
    },
    {
        "day": "Tuesday", "period": 1,
        "programme": "BCA", "semester": 2, "section": "A",
        "subject_code": "CA202", "subject_name": "Data Structures",
        "faculty": "Dr. Das", "room": "Room 103"
    },
    {
        "day": "Tuesday", "period": 2,
        "programme": "BCA", "semester": 2, "section": "A",
        "subject_code": "CA203", "subject_name": "Computer Networks",
        "faculty": "Dr. Sen", "room": "Room 104"
    },
    {
        "day": "Wednesday", "period": 3,
        "programme": "BCA", "semester": 2, "section": "A",
        "subject_code": "CA204", "subject_name": "Database Concepts",
        "faculty": "Dr. Kapoor", "room": "Room 105"
    },
    {
        "day": "Wednesday", "period": 4,
        "programme": "BCA", "semester": 2, "section": "B",
        "subject_code": "CA205", "subject_name": "Web Technology",
        "faculty": "Dr. Das", "room": "Room 101"
    },

    # ---------------- B.Com Semester 6 ----------------
    {
        "day": "Thursday", "period": 1,
        "programme": "B.Com", "semester": 6, "section": "A",
        "subject_code": "BC601", "subject_name": "Auditing",
        "faculty": "Dr. Sharma", "room": "Room 102"
    },
    {
        "day": "Thursday", "period": 2,
        "programme": "B.Com", "semester": 6, "section": "A",
        "subject_code": "BC602", "subject_name": "Taxation",
        "faculty": "Dr. Mehta", "room": "Room 103"
    },
    {
        "day": "Thursday", "period": 3,
        "programme": "B.Com", "semester": 6, "section": "A",
        "subject_code": "BC603", "subject_name": "Investment Management",
        "faculty": "Dr. Roy", "room": "Room 104"
    },
    {
        "day": "Friday", "period": 1,
        "programme": "B.Com", "semester": 6, "section": "A",
        "subject_code": "BC604", "subject_name": "International Business",
        "faculty": "Dr. Sen", "room": "Room 105"
    },
    {
        "day": "Friday", "period": 2,
        "programme": "B.Com", "semester": 6, "section": "B",
        "subject_code": "BC605", "subject_name": "Entrepreneurship",
        "faculty": "Dr. Das", "room": "Room 101"
    },

    # ---------------- Intentional problem entries ----------------
    {
        "day": "Tuesday", "period": 2,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC407", "subject_name": "Financial Statement Analysis",
        "faculty": "Dr. Roy", "room": "Room 102"
    },  # SECTION CLASH with entry 8

    {
        "day": "Monday", "period": 2,
        "programme": "BBA", "semester": 2, "section": "B",
        "subject_code": "BA206", "subject_name": "Organizational Behaviour",
        "faculty": "Dr. Mehta", "room": "Room 101"
    },  # ROOM CLASH with entry 4? No: entry 4 Monday P3.
       # This is a valid extra entry.

    {
        "day": "Friday", "period": 5,
        "programme": "BCA", "semester": 2, "section": "B",
        "subject_code": "CA206", "subject_name": "Software Engineering",
        "faculty": "Dr. Sharma", "room": "Room 101"
    },  # FACULTY AVAILABILITY CLASH: Dr. Sharma Friday lacks P5

    {
        "day": "Monday", "period": 5,
        "programme": "BBA", "semester": 2, "section": "B",
        "subject_code": "BA207", "subject_name": "Business Research",
        "faculty": "Dr. Mehta", "room": "Room 102"
    },  # ROOM AVAILABILITY CLASH: Room 102 Monday lacks P3? P5 is available.
       # This is valid.

    {
        "day": "Tuesday", "period": 5,
        "programme": "BCA", "semester": 2, "section": "B",
        "subject_code": "CA207", "subject_name": "Computer Graphics",
        "faculty": "Dr. Sen", "room": "Room 999"
    },  # INVALID ROOM + ROOM AVAILABILITY cannot be checked

    {
        "day": "Wednesday", "period": 2,
        "programme": "BBA", "semester": 2, "section": "B",
        "subject_code": "BA208", "subject_name": "Strategic Management",
        "faculty": "Dr. Unknown", "room": "Room 104"
    },  # INVALID FACULTY

    {
        "day": "Monday", "period": 2,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC402", "subject_name": "Financial Management",
        "faculty": "Dr. Sharma", "room": "Room 102"
    },  # DUPLICATE of entry 2

    {
        "day": "Wednesday", "period": 5,
        "programme": "BCA", "semester": 2, "section": "B",
        "subject_code": "CA208", "subject_name": "Cyber Security",
        "faculty": "Dr. Roy", "room": "Room 103"
    },  # ROOM AVAILABILITY CLASH: Room 103 Wednesday lacks P5

    {
        "day": "Tuesday", "period": 2,
        "programme": "B.Com", "semester": 4, "section": "A",
        "subject_code": "BC408", "subject_name": "Financial Statement Analysis",
        "faculty": "Dr. Das", "room": "Room 104"
    },  # SECTION CLASH with entry 22
]


# ============================================================
# CLASH STORAGE
# ============================================================

clashes = []


def add_clash(clash_type, entry1, message, entry2=None):
    """Add one clash to the global clash list."""
    clash = {
        "type": clash_type,
        "day": entry1["day"],
        "period": entry1["period"],
        "message": message,
        "entry1": entry1,
        "entry2": entry2
    }

    # Avoid adding exactly the same clash twice.
    signature = (
        clash_type,
        entry1["day"],
        entry1["period"],
        message,
        entry1["subject_code"],
        entry2["subject_code"] if entry2 else ""
    )

    for old_clash in clashes:
        old_signature = (
            old_clash["type"],
            old_clash["day"],
            old_clash["period"],
            old_clash["message"],
            old_clash["entry1"]["subject_code"],
            old_clash["entry2"]["subject_code"]
            if old_clash["entry2"] else ""
        )

        if signature == old_signature:
            return

    clashes.append(clash)


# ============================================================
# 1. DISPLAY TIMETABLE
# ============================================================

def display_timetable():
    """Display all timetable entries in a readable format."""

    print("\n" + "=" * 130)
    print("UNIVERSITY TIMETABLE")
    print("=" * 130)

    header = (
        f"{'No.':<4} {'Day':<10} {'P':<3} {'Programme':<10} "
        f"{'Sem':<5} {'Sec':<4} {'Code':<8} {'Subject':<28} "
        f"{'Faculty':<15} {'Room':<10}"
    )
    print(header)
    print("-" * 130)

    for index, entry in enumerate(timetable, start=1):
        print(
            f"{index:<4} "
            f"{entry['day']:<10} "
            f"{entry['period']:<3} "
            f"{entry['programme']:<10} "
            f"{entry['semester']:<5} "
            f"{entry['section']:<4} "
            f"{entry['subject_code']:<8} "
            f"{entry['subject_name'][:27]:<28} "
            f"{entry['faculty'][:14]:<15} "
            f"{entry['room']:<10}"
        )

    print("=" * 130)
    print("Total entries:", len(timetable))


# ============================================================
# 2. CHECK FACULTY CLASHES
# ============================================================

def check_faculty_clashes():
    """Check whether one faculty member teaches two classes at once."""

    found = 0

    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):

            entry1 = timetable[i]
            entry2 = timetable[j]

            if (
                entry1["day"] == entry2["day"]
                and entry1["period"] == entry2["period"]
                and entry1["faculty"] == entry2["faculty"]
            ):
                message = (
                    f"{entry1['faculty']} is assigned to "
                    f"'{entry1['subject_name']}' and "
                    f"'{entry2['subject_name']}'"
                )

                add_clash(
                    "FACULTY CLASH",
                    entry1,
                    message,
                    entry2
                )

                found += 1

    print(f"\nFaculty clashes found: {found}")


# ============================================================
# 3. CHECK ROOM CLASHES
# ============================================================

def check_room_clashes():
    """Check whether one room is assigned to two classes at once."""

    found = 0

    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):

            entry1 = timetable[i]
            entry2 = timetable[j]

            if (
                entry1["day"] == entry2["day"]
                and entry1["period"] == entry2["period"]
                and entry1["room"] == entry2["room"]
            ):
                message = (
                    f"{entry1['room']} is assigned to "
                    f"'{entry1['subject_name']}' and "
                    f"'{entry2['subject_name']}'"
                )

                add_clash(
                    "ROOM CLASH",
                    entry1,
                    message,
                    entry2
                )

                found += 1

    print(f"\nRoom clashes found: {found}")


# ============================================================
# 4. CHECK SECTION CLASHES
# ============================================================

def check_section_clashes():
    """Check whether one section has two classes at the same time."""

    found = 0

    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):

            entry1 = timetable[i]
            entry2 = timetable[j]

            same_section = (
                entry1["programme"] == entry2["programme"]
                and entry1["semester"] == entry2["semester"]
                and entry1["section"] == entry2["section"]
            )

            if (
                entry1["day"] == entry2["day"]
                and entry1["period"] == entry2["period"]
                and same_section
                and entry1["subject_code"] != entry2["subject_code"]
            ):
                section_name = (
                    f"{entry1['programme']} "
                    f"Semester {entry1['semester']} "
                    f"Section {entry1['section']}"
                )

                message = (
                    f"{section_name} has "
                    f"'{entry1['subject_name']}' and "
                    f"'{entry2['subject_name']}' at the same time"
                )

                add_clash(
                    "SECTION CLASH",
                    entry1,
                    message,
                    entry2
                )

                found += 1

    print(f"\nSection clashes found: {found}")


# ============================================================
# 5. CHECK FACULTY AVAILABILITY
# ============================================================

def check_faculty_availability():
    """Check whether faculty are teaching during their available periods."""

    found = 0

    for entry in timetable:

        faculty = entry["faculty"]
        day = entry["day"]
        period = entry["period"]

        # Invalid faculty is handled by validate_faculty().
        if faculty not in faculty_availability:
            continue

        available_periods = faculty_availability[faculty].get(day, [])

        if period not in available_periods:

            message = (
                f"{faculty} is unavailable on {day}, "
                f"period {period}"
            )

            add_clash(
                "FACULTY AVAILABILITY CLASH",
                entry,
                message
            )

            found += 1

    print(f"\nFaculty availability clashes found: {found}")


# ============================================================
# 6. CHECK ROOM AVAILABILITY
# ============================================================

def check_room_availability():
    """Check whether rooms are available at the scheduled time."""

    found = 0

    for entry in timetable:

        room = entry["room"]
        day = entry["day"]
        period = entry["period"]

        # Invalid room is handled by validate_room().
        if room not in room_availability:
            continue

        available_periods = room_availability[room].get(day, [])

        if period not in available_periods:

            message = (
                f"{room} is unavailable on {day}, "
                f"period {period}"
            )

            add_clash(
                "ROOM AVAILABILITY CLASH",
                entry,
                message
            )

            found += 1

    print(f"\nRoom availability clashes found: {found}")


# ============================================================
# 7. CHECK DUPLICATE ENTRIES
# ============================================================

def check_duplicate_entries():
    """Check for duplicate timetable entries."""

    found = 0
    seen = {}

    for entry in timetable:

        key = (
            entry["day"],
            entry["period"],
            entry["programme"],
            entry["semester"],
            entry["section"],
            entry["subject_code"]
        )

        if key in seen:

            message = (
                f"Duplicate of timetable entry "
                f"number {seen[key]}"
            )

            add_clash(
                "DUPLICATE TIMETABLE ENTRY",
                entry,
                message
            )

            found += 1

        else:
            seen[key] = timetable.index(entry) + 1

    print(f"\nDuplicate entries found: {found}")


# ============================================================
# 8. VALIDATE FACULTY
# ============================================================

def validate_faculty():
    """Check whether every assigned faculty member exists."""

    found = 0

    for entry in timetable:

        if entry["faculty"] not in faculty_list:

            message = (
                f"{entry['faculty']} is not in the "
                f"university faculty list"
            )

            add_clash(
                "INVALID FACULTY",
                entry,
                message
            )

            found += 1

    print(f"\nInvalid faculty assignments found: {found}")


# ============================================================
# 9. VALIDATE ROOM
# ============================================================

def validate_room():
    """Check whether every assigned room exists."""

    found = 0

    for entry in timetable:

        if entry["room"] not in room_list:

            message = (
                f"{entry['room']} is not in the "
                f"university room list"
            )

            add_clash(
                "INVALID ROOM",
                entry,
                message
            )

            found += 1

    print(f"\nInvalid room assignments found: {found}")


# ============================================================
# SEARCH FUNCTIONS
# ============================================================

def search_faculty_timetable():
    """Search and display the timetable of a faculty member."""

    faculty = input("Enter faculty name: ").strip()

    results = [
        entry for entry in timetable
        if entry["faculty"].lower() == faculty.lower()
    ]

    if not results:
        print("No timetable entries found for that faculty.")
        return

    print("\nFaculty Timetable:", faculty)

    # Lambda function requirement:
    # Sort by day and period.
    results.sort(
        key=lambda x: (x["day"], x["period"])
    )

    for entry in results:
        print(
            f"{entry['day']} | Period {entry['period']} | "
            f"{entry['programme']} Sem {entry['semester']} "
            f"Section {entry['section']} | "
            f"{entry['subject_name']} | {entry['room']}"
        )


def search_room_timetable():
    """Search and display the timetable of a room."""

    room = input("Enter room number: ").strip()

    results = [
        entry for entry in timetable
        if entry["room"].lower() == room.lower()
    ]

    if not results:
        print("No timetable entries found for that room.")
        return

    print("\nRoom Timetable:", room)

    results.sort(
        key=lambda x: (x["day"], x["period"])
    )

    for entry in results:
        print(
            f"{entry['day']} | Period {entry['period']} | "
            f"{entry['programme']} Sem {entry['semester']} "
            f"Section {entry['section']} | "
            f"{entry['subject_name']} | {entry['faculty']}"
        )


def search_section_timetable():
    """Search and display a section timetable."""

    programme = input("Enter programme: ").strip()
    semester_input = input("Enter semester: ").strip()
    section = input("Enter section: ").strip()

    try:
        semester = int(semester_input)
    except ValueError:
        print("Semester must be a number.")
        return

    results = [
        entry for entry in timetable
        if (
            entry["programme"].lower() == programme.lower()
            and entry["semester"] == semester
            and entry["section"].lower() == section.lower()
        )
    ]

    if not results:
        print("No timetable entries found for that section.")
        return

    print(
        f"\nSection Timetable: "
        f"{programme} Semester {semester} Section {section}"
    )

    results.sort(
        key=lambda x: (x["day"], x["period"])
    )

    for entry in results:
        print(
            f"{entry['day']} | Period {entry['period']} | "
            f"{entry['subject_code']} | "
            f"{entry['subject_name']} | "
            f"{entry['faculty']} | {entry['room']}"
        )


# ============================================================
# 10. GENERATE CLASH REPORT
# ============================================================

def generate_clash_report():
    """Run every checker and display a complete clash report."""

    global clashes

    # Start with a clean report.
    clashes = []

    check_faculty_clashes()
    check_room_clashes()
    check_section_clashes()
    check_faculty_availability()
    check_room_availability()
    check_duplicate_entries()
    validate_faculty()
    validate_room()

    print("\n")
    print("=" * 100)
    print("DETAILED CLASH REPORT")
    print("=" * 100)

    if not clashes:
        print("No clashes found.")
        return

    print("Report generated:",
          datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("Total issues:", len(clashes))
    print("-" * 100)

    for number, clash in enumerate(clashes, start=1):

        entry1 = clash["entry1"]
        entry2 = clash["entry2"]

        print(f"\nISSUE #{number}")
        print("Type    :", clash["type"])
        print("Day     :", clash["day"])
        print("Period  :", clash["period"])
        print("Details :", clash["message"])

        print(
            "Class 1:",
            f"{entry1['programme']} - "
            f"Semester {entry1['semester']} - "
            f"Section {entry1['section']} - "
            f"{entry1['subject_name']}"
        )

        if entry2 is not None:
            print(
                "Class 2:",
                f"{entry2['programme']} - "
                f"Semester {entry2['semester']} - "
                f"Section {entry2['section']} - "
                f"{entry2['subject_name']}"
            )

        print("-" * 100)


# ============================================================
# RUN ALL CHECKS WITHOUT FULL REPORT
# ============================================================

def run_all_checks():
    """Run all validation functions and display a summary."""

    global clashes
    clashes = []

    check_faculty_clashes()
    check_room_clashes()
    check_section_clashes()
    check_faculty_availability()
    check_room_availability()
    check_duplicate_entries()
    validate_faculty()
    validate_room()

    print("\n" + "=" * 60)
    print("CHECK SUMMARY")
    print("=" * 60)
    print("Total issues detected:", len(clashes))

    # Count issue types using a dictionary.
    counts = {}

    for clash in clashes:
        clash_type = clash["type"]
        counts[clash_type] = counts.get(clash_type, 0) + 1

    for clash_type, count in counts.items():
        print(f"{clash_type:<35}: {count}")


# ============================================================
# MAIN MENU
# ============================================================

def display_menu():
    """Display the main program menu."""

    print("\n")
    print("=" * 60)
    print(" UNIVERSITY TIMETABLE CLASH DETECTOR")
    print("=" * 60)
    print("1.  Display Timetable")
    print("2.  Check Faculty Clashes")
    print("3.  Check Room Clashes")
    print("4.  Check Section Clashes")
    print("5.  Check Faculty Availability")
    print("6.  Check Room Availability")
    print("7.  Check Duplicate Entries")
    print("8.  Validate Faculty")
    print("9.  Validate Room")
    print("10. Generate Complete Clash Report")
    print("11. Run All Checks - Summary")
    print("12. Search Faculty Timetable")
    print("13. Search Room Timetable")
    print("14. Search Section Timetable")
    print("15. Exit")
    print("=" * 60)


def main():
    """Main function of the program."""

    print("\nWelcome to the University Timetable Clash Detector!")

    while True:

        display_menu()

        choice = input("Enter your choice (1-15): ").strip()

        if choice == "1":
            display_timetable()

        elif choice == "2":
            check_faculty_clashes()

        elif choice == "3":
            check_room_clashes()

        elif choice == "4":
            check_section_clashes()

        elif choice == "5":
            check_faculty_availability()

        elif choice == "6":
            check_room_availability()

        elif choice == "7":
            check_duplicate_entries()

        elif choice == "8":
            validate_faculty()

        elif choice == "9":
            validate_room()

        elif choice == "10":
            generate_clash_report()

        elif choice == "11":
            run_all_checks()

        elif choice == "12":
            search_faculty_timetable()

        elif choice == "13":
            search_room_timetable()

        elif choice == "14":
            search_section_timetable()

        elif choice == "15":
            print("\nThank you for using the Timetable Clash Detector.")
            print("Program terminated.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 15.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
