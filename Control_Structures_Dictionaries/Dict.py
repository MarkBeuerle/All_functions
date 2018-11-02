students = {
    "Henk": 2,
    "Freek": 8,
    "Willem": 10,
    "Jan": 8.4,
    "Jaap": 9.5,
    "Luuk": 7.3,
    "Daan": 8.9,
    "Bram": 5.2
}

[print("{0} heeft een: {1}".format(student, grade) if grade >= 9 else None) for student, grade in students.items()]