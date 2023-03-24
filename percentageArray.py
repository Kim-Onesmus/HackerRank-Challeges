if __name__ == '__main__':
    # Read input from user
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *marks = input().split()
        marks = list(map(float, marks))
        student_marks[name] = marks

    # Read the name of the student whose average marks is to be calculated
    query_name = input()

    # Get the marks for the student
    marks = student_marks[query_name]

    # Calculate the average of the marks
    average_marks = sum(marks) / len(marks)

    # Print the average of the marks, rounded to 2 decimal places
    print("{:.2f}".format(average_marks))