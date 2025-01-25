import json

# 1. Read the JSON file
with open('test.json', 'r') as file:
    data = json.load(file)

# 2. Extract the list of students
students = data['students']

# 3. Iterate and print each student's details
for student in students:
    print(f"Student: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math: {student['grades']['math']}")
    print(f"Science: {student['grades']['science']}")
    print("-" * 20)

# 4. Calculate each student's average grade
for student in students:
    grades = student['grades']
    average = sum(grades.values()) / len(grades)
    print(f"{student['name']}'s average grade: {average}")

# 5. Add a new student
new_student = {
    "id": 3,
    "name": "Charlie",
    "age": 21,
    "grades": {
        "math": 88,
        "science": 92
    }
}
students.append(new_student)

# 6. Save the updated JSON
with open('updated_test.json', 'w') as file:
    json.dump(data, file, indent=4)