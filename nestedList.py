if __name__ == '__main__':
    # Read input from user
    n = int(input())
    student_list = []
    for i in range(n):
        name = input()
        score = float(input())
        student_list.append([name, score])

    # Sort the student_list based on the grades
    sorted_list = sorted(student_list, key=lambda x: x[1])

    # Find the second lowest grade
    second_lowest_grade = sorted(set([score for name, score in sorted_list]))[1]

    # Get the names of all students with the second lowest grade
    second_lowest_students = [name for name, score in sorted_list if score == second_lowest_grade]

    # Sort the names alphabetically
    second_lowest_students.sort()

    # Print the names of students with the second lowest grade
    for name in second_lowest_students:
        print(name)
