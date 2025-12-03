# 📘 Gradebook Analyzer (Python Project)

This is a beginner-friendly Python Gradebook Analyzer program.  
It allows users to input student marks manually or upload them through a CSV file.  
The program then calculates:

- Average score  
- Median score  
- Highest and lowest marks  
- Grades for each student  
- Pass/Fail list  
- A clean table using **Pandas**

---

**## 🚀 Features**
✔ Manual entry of student names and marks  
✔ CSV file upload support  
✔ Average and median calculation  
✔ Highest & lowest scorer detection  
✔ Automatic grade assignment (A–F)  
✔ Pass/Fail classification  
✔ Pandas table for clean output  
✔ Beginner-friendly, simple to understand

---

**🧠 How It Works (Logic Summary)**
input_manual() → take student data from the user
input_csv() → read a CSV file using Python's csv module
average_score() → uses sum() and len()
median_score() → manually calculates median
max_scored() / min_scored() → uses key=marks.get
grades_given() → assigns A–F
passed_failed() → marks >= 40 pass
pandas_table() → displays a clean DataFrame

**📌 Notes**
Only integer marks should be entered
CSV file must have name and mark on each line
Avoid duplicate names in the CSV
Program loops until the user selects Exit

**👤 Author:**
Aadit Prashar
BTech CSE
2501010073
