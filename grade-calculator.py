# grade_calculator.py
def average(marks):
    """Return the arithmetic mean of a list of subject marks (0-100)."""
    if not marks:
        raise ValueError("Marks list cannot be empty.")
    for m in marks:
        if m < 0 or m > 100:
            raise ValueError(f"Invalid mark: {m}. Must be between 0 and 100.")
    return round(sum(marks) / len(marks), 2)


def grade(avg):
    """Return letter grade based on average score (0-100)."""
    if avg < 0 or avg > 100:
        raise ValueError(f"Invalid average: {avg}. Must be between 0 and 100.")
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def is_pass(marks):
    """Return True if all marks >= 40 and overall average >= 50, else False."""
    avg = average(marks)
    return all(m >= 40 for m in marks) and avg >= 50

def gpa_point(avg):
    """Convert average marks (0-100) to a 10.0 GPA scale."""
    if avg < 0 or avg > 100:
        raise ValueError(f"Invalid average: {avg}. Must be between 0 and 100.")
    return round(avg / 10.0, 2)

if __name__ == "__main__":
    sample1 = [88, 92, 85, 90, 95]
    sample2 = [72, 68, 35, 80, 75]
    print("Marks:", sample1)
    print("Average:", average(sample1))
    print("Grade:", grade(average(sample1)))
    print("Passed:", is_pass(sample1))
    print("-" * 35)
    print("Marks:", sample2)
    print("Average:", average(sample2))
    print("Grade:", grade(average(sample2)))
    print("Passed:", is_pass(sample2))
