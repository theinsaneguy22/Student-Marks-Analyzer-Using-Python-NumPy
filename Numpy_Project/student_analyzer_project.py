#student analyser using python numpy
import numpy as np

students = ["Amit", "Chandu", "Virat", "Jagdish"]
subjects = ["maths", "science", "history"]
arr = np.array([[60, 55, 50],
                [65, 50, 96],
                [70, 85, 55],
                [85, 95, 90]])
outofMarks = 300
#print(arr)

#calculate total marks (per student)
total_marks = np.sum(arr, axis=1)
#print(total_marks)

#Calculate Average Marks (Per Student)
avg_marks = np.mean(arr, axis=1)
#print(avg_marks)


#Find the topper of the class

max_marks=np.max(total_marks)
#print(max_marks)

topper_index = np.argmax(total_marks) # find the highest marks from total_marks array & returns index(0 / 1 / 2)
topper_name = students[topper_index] #index-2 in total_marks corresponds to the student at index-2 in the students list
topper_marks = total_marks[topper_index] #retrieves the actual score from the original array
# print("Topper name is: ", topper_name)
# print("Topper Score is: ", topper_marks, "out of", outofMarks)


#toppers scorecard

topper_scorecard = arr[topper_index]
#print(topper_scorecard)


#Subject-wise highest marks

subject_highest = np.max(arr, axis=0)
#print(subject_highest)
for i in range(len(subjects)):
    highest_mark = np.max(arr[:, i])          # Highest mark in subject
    topper_indices = np.where(arr[:, i] == highest_mark)[0]

    topper_names = [students[idx] for idx in topper_indices]

    #print(f"{subjects[i]}: {', '.join(topper_names)} ({highest_mark})")



#Grade calculation
grades = []
for avg in avg_marks:
    if avg >= 90:
        grades.append("Grade A")
    elif avg >= 75:
        grades.append("Grade B")
    elif avg >= 60:
        grades.append("Grade C")
    else:
        grades.append("Grade D")
#print(grades)



# Final Result Report

print("\n--- Student Marks Report ---")

print("Name\tTotal\tAverage\tGrade")

for i in range(len(students)):
    print(f"{students[i]}\t{total_marks[i]}\t{avg_marks[i]:.2f}\t{grades[i]}")


print("\n---Class Topper:---")
print(topper_name, "with marks of", topper_marks, "out of", outofMarks)

print("\n---Class Toppers",topper_name ,"Scorecard: ---")
for i in range(len(topper_scorecard)):
    print(f"{subjects[i]}\t{topper_scorecard[i]}")


print("\n---Topper in Each Subject:---")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {', '.join(topper_names)} ({highest_mark})")