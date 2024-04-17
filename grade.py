#. The Grade Analyzer
#Objective: The aim of this assignment is to analyze a set of grades and provide statistics.
#Task 1: Code a function to calculate the average grade. 
#Task 2: Implement a function to find the highest and lowest grade. 
#Task 3 (BONUS): Create a feature that categorizes grades into letter grades (A, B, C, etc.).



def find_score (grades):
    if 90 <= grades <= 100:
        return 'A'
    elif 80 <= grades < 90:
        return 'B'
    elif 70 <= grades < 80:
        return 'C'
    elif 60 <= grades < 70:
        return 'D'
    else:
        return 'F'
def calculate_average(total):
    return total / 5                                             

scores = []
for numbers in range(1, 6):                                 
    score = int(input("Enter score {0}: ".format(numbers)))
    print("That's a(n): " + find_score(score))
    scores.append(score)
#I Had troubles with this part and used google to help me out I was forgetting to put calculate average with (total)and the same went for find_score(avg_marks)
total = sum(scores)
avg_marks = calculate_average(total) 
final_grade = find_score(avg_marks)
#I also hadnt converted this to string 
print("Average grade is: " + str(avg_marks))
print("That's a(n): " + str(final_grade))









    


