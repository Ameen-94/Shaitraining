# Input: List of grades (numerical)
grades = [95, 85, 74, 63, 55, 88, 92, 70]

# Convert numerical grades to letter grades using map and lambda
letter_grades = list(map(lambda grade: "A" if grade >= 90 else
                                       "B" if grade >= 80 else
                                       "C" if grade >= 70 else
                                       "D" if grade >= 60 else
                                       "F", grades))

# Display the original grades and their corresponding letter grades
print("Numerical Grades:", grades)
print("Letter Grades:", letter_grades)