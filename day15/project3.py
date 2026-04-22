import csv 

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >=80:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=60:
        return "C"
    else:
        return "fail"

# read input files 
with open("input.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)

    # write output file 
    with open("report.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["name", "marks", "grade"])

        for row in reader:
            name = row[0]
            marks = int(row[1])
            grade = calculate_grade(marks)

            writer.writerow([name, marks, grade])

print("report generated successfully")