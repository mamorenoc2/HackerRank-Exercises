'''
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
Examples

 grade = 84 round to 85 (85 - 84 is less than 3)
 grade = 29 do not round (result is less than 40)
 grade = 57 do not round (60 - 57 is 3 or higher)
Given the initial value of grade for each of Sam's  students, write code to automate the rounding process.

Function Description

Complete the function gradingStudents in the editor below.

gradingStudents has the following parameter(s):

int grades[n]: the grades before rounding
Returns

int[n]: the grades after rounding as appropriate
Input Format

The first line contains a single integer, , the number of students.
Each line  of the  subsequent lines contains a single integer, .

Constraints


'''

def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_multiple = grade + (5 - (grade % 5))
            if (next_multiple - grade) < 3:
                rounded_grades.append(next_multiple)
            else:
                rounded_grades.append(grade)
    
    return rounded_grades