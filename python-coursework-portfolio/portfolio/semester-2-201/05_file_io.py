'''
Topic: File I/O -- reading CSV/TXT student records, computing averages,
writing letter grades and processed text back out to new files
'''

##############################################
def get_info(csv_file, student_name):
##############################################

    file = open(csv_file, 'r')
    file.readline()

    for line in file:
        parts = line.strip().split(',')

        if parts[1].lower() == student_name.lower():
            zip_code = parts[2]
            college = parts[5]
            file.close()
            return parts[1] + " is a student in " + college + " college with a " + zip_code + " ZIP code"

    file.close()
    return "Could not find any information about " + student_name

##############################################
def list_courses(csv_file, college_name):
##############################################

    file = open(csv_file, 'r')
    file.readline()

    unique_courses = []

    for line in file:
        parts = line.strip().split(',')

        if parts[5] == college_name and parts[4] not in unique_courses:
            unique_courses.append(parts[4])

    file.close()
    return unique_courses

##############################################
def find_students(txt_file, threshold):
##############################################

    file = open(txt_file, 'r')
    passing_students = []

    for line in file:
        parts = line.strip().split()

        total = 0
        count = 0

        for i in range(4, len(parts)):
            total += int(parts[i])
            count += 1

        avg = total / count

        if avg >= threshold:
            passing_students.append(parts[0] + " " + parts[1])

    file.close()
    return passing_students

##############################################
def final_grade(incsv_file, outcsv_file):
##############################################
    infile = open(incsv_file, 'r')
    outfile = open(outcsv_file, 'w')

    infile.readline()

    for line in infile:
        parts = line.strip().split(',')

        student_id = parts[0]
        name = parts[1]
        grades = parts[6].split()

        total = 0
        for g in grades:
            total += int(g)

        avg = total / len(grades)

        if avg < 60:
            letter = 'F'
        elif avg < 70:
            letter = 'D'
        elif avg < 80:
            letter = 'C'
        elif avg < 90:
            letter = 'B'
        else:
            letter = 'A'

        outfile.write(student_id + "," + name + "," + letter + "\n")

    infile.close()
    outfile.close()

##############################################
def read_paragraph(intxt_file, outtxt_file, word):
##############################################

    infile = open(intxt_file, 'r')
    text = infile.read().lower()
    infile.close()

    word = word.lower()
    result = ""

    i = 0
    while i < len(text):
        match = True

        if i + len(word) <= len(text):
            for j in range(len(word)):
                if text[i + j] != word[j]:
                    match = False
                    break
        else:
            match = False

        if match:
            result += "*"
            i += len(word)
        else:
            result += text[i]
            i += 1

    outfile = open(outtxt_file, 'w')
    outfile.write(result)
    outfile.close()
