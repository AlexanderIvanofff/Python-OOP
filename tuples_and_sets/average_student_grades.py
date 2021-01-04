def input_to_list(list_count):
    return [input() for _ in range(list_count)]


def count_student_mark(values):
    students_mark = {}

    for value in values:
        (student, mark) = value.split(' ')
        if student not in students_mark:
            students_mark[student] = []

        students_mark[student].append(float(mark))
    return students_mark


def avg(values):
    return sum(values) / len(values)


def print_results(student_mark):
    for (student_name, marks) in student_mark.items():
        average_mark = avg(marks)
        marks_string = ' '.join(f'{mark:.2f}' for mark in marks)
        print(f'{student_name} -> {marks_string} (avg: {average_mark:.2f})')


test_input = input_to_list(int(input()))
print_results(count_student_mark(test_input))