students = ["Ali", "Sara", "Ahmed"]
marks = [45, 88, 67]

report = [
    f"{name}: {'Pass' if mark >= 50 else 'Fail'}"
    for name, mark in zip(students, marks)
]

print(report)