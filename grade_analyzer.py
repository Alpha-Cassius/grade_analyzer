def process_scores(students):
    # Calculates the average score for each student.
    averages = {}
    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg
    return averages

def classify_grades(averages):
    # Assigns letter grades based on internal thresholds.
    GRADE_A = 90
    GRADE_B = 75
    GRADE_C = 60
    
    classified = {}
    for name, avg in averages.items():
        if avg >= GRADE_A:
            grade = 'A'
        elif avg >= GRADE_B:
            grade = 'B'
        elif avg >= GRADE_C:
            grade = 'C'
        else:
            grade = 'F'
        
        classified[name] = (avg, grade)
    return classified

def generate_report(classified, passing_avg=70):
    # Prints a formatted report and returns the count of passing students.
    print("===== Student Grade Report =====")
    
    passed_count = 0
    total_students = len(classified)
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
            
        print(f"{name:<9} | Avg: {avg:>5.2f} | Grade: {grade} | Status: {status}")
    
    print("=" * 32)
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")
    
    return passed_count

if __name__ == "__main__":
    student_data = {
        "Alice": [85, 90, 78, 92],
        "Bob": [60, 65, 70, 55],
        "Clara": [95, 98, 92, 100]
    }
    
    student_averages = process_scores(student_data)
    
    graded_data = classify_grades(student_averages)
    
    generate_report(graded_data)
