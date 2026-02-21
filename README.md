# grade_analyzer
---
A modular Python script that processes student test scores, calculates averages, assigns letter grades, and generates a formatted performance report.

## 🚀 Features

* **Data Processing:** Automatically calculates student averages from raw score lists.
* **Grade Classification:** Categorizes performance into A, B, C, or F based on internal thresholds.
* **Formatted Reporting:** Outputs a clean, tabular summary including pass/fail status.
* **Customizable Passing Grade:** Supports a flexible passing threshold (defaulting to 70).

## 📂 File Structure

* `grade_analyzer.py`: The main script containing the logic for Tasks 1, 2, and 3.

## 📊 Logic Flow

The system follows a linear data pipeline where the output of one function serves as the input for the next:

1. **`process_scores()`**: Raw Data  Averages
2. **`classify_grades()`**: Averages  Letter Grades
3. **`generate_report()`**: Letter Grades  Visual Summary

---

Thank You
