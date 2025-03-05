student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for mark in student_scores:
    print(student_scores[mark])
    if student_scores[mark]>=91:
        student_grades[mark] ="Outstanding"
    elif 91>student_scores[mark]>=81:
        student_grades[mark] ="Exceeds Expectations"
    elif 81>student_scores[mark]>=71:
        student_grades[mark] ="Acceptable"
    else:
        student_grades[mark] ="Fail"
print(student_grades)