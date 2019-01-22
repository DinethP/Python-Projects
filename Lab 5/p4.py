
def get_average_grades(filename='grades.csv'):
    with open(filename) as f:
        marks = [line.strip().split(',') for line in f]

    lab1 = [float(val[0]) for val in marks if float(val[0]) > 0]
    lab2 = [float(val[1]) for val in marks if float(val[1]) > 0]
    lab3 = [float(val[2]) for val in marks if float(val[2]) > 0]
    lab4 = [float(val[3]) for val in marks if float(val[3]) > 0]
    lab_list = [lab1, lab2, lab3, lab4]

    average_grades_list = [sum(lab) / len(lab) for lab in lab_list]

    return average_grades_list
