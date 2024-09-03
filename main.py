def default_grade(grade):
    if grade == 'O':
        return 10
    elif grade == 'A+':
        return 9
    elif grade == 'A':
        return 8
    elif grade == 'B+':
        return 7
    elif grade == 'B':
        return 6
    elif grade == 'C':
        return 5
    elif grade == 'U':
        return 0
    elif grade == 'SA':
        return 0
    elif grade == 'W':
        return 0
    elif grade == 'WH':
        return 0
    else:
        return None

maths = default_grade(input("DISCRETE MATHEMATICAL STRUCTURES(U19MAT401D): ").upper())
ids = default_grade(input("INTRODUCTION TO DATA SCIENCE(U19ADS402): ").upper())
dbms = default_grade(input("DATABASE MANAGEMENT SYSTEMS(U19ADS401): ").upper())
cn = default_grade(input("COMPUTER NETWORK(U19ADS404): ").upper())
jp = default_grade(input("JAVA PROGRAMMING(U19ADS403): ").upper())
asd = default_grade(input("AGILE SOFTWARE DEVELOPMENT (U19ADS405): ").upper())
jp_lab = default_grade(input("JAVA PROGRAMMING LABORATORY(U19ADS407): ").upper())
dbms_lab = default_grade(input("DATABASE MANAGEMENT SYSTEMS LABORATORY(U19ADS406): ").upper())
ss2 = default_grade(input("SOFTSKILLS AND APTITUDE - II(U19GE401): ").upper())
 

gpa = (4 * maths) + (3 * ids) + (3 * dbms) + (3 * cn) + (3 * jp) + (4 * asd) + (2 * jp_lab) + (2 * dbms_lab) + (1 *ss2)
sgpa = gpa / 25
print("SGPA:", sgpa)



